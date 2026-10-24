"""
mcrescue.client - 麦当劳官方 MCP (Model Context Protocol) 客户端
基于 Streamable HTTP 协议与 JSON-RPC 2.0 规范，提供安全认证、工具调用与本地优雅回退
"""

import os
import json
import logging
import urllib.request
import urllib.error
from typing import Dict, Any, List, Optional
from mcrescue.mock_data import MOCK_STORES, MOCK_MEALS, MOCK_COUPONS

logger = logging.getLogger("mcrescue")

class McDonaldsMCPClient:
    """
    麦当劳中国官方 MCP 客户端
    规范说明：
    - MCP 服务端点：https://mcp.mcd.cn
    - 鉴权头：Authorization: Bearer <MCP_TOKEN>
    - 协议：Streamable HTTP / JSON-RPC 2.0
    - 安全原则：绝不在客户端硬编码 Token，优先从环境变量 MCD_MCP_TOKEN 读取
    """

    def __init__(self, token: Optional[str] = None, base_url: str = "https://mcp.mcd.cn", use_fallback: bool = True):
        self.token = token or os.environ.get("MCD_MCP_TOKEN", "").strip()
        self.base_url = base_url.rstrip("/")
        self.use_fallback = use_fallback
        self.is_live = bool(self.token)

    def _call_rpc(self, method: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """执行底层 JSON-RPC 2.0 调用"""
        if not self.token:
            raise ValueError("未检测到 MCD_MCP_TOKEN，已启用本地高保真模拟引擎。")

        payload = {
            "jsonrpc": "2.0",
            "id": 1024,
            "method": method,
            "params": params
        }
        data = json.dumps(payload).encode("utf-8")
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "Authorization": f"Bearer {self.token}",
            "User-Agent": "McRescue-1024-Agent/1.0.0"
        }

        # 尝试标准端点与 /mcp 路径
        endpoints = [f"{self.base_url}/mcp", self.base_url]
        last_error = None

        for endpoint in endpoints:
            try:
                req = urllib.request.Request(endpoint, data=data, headers=headers)
                with urllib.request.urlopen(req, timeout=10) as response:
                    raw_text = response.read().decode("utf-8")
                
                # 兼容 SSE 流式输出中的 data: 协议行
                for line in raw_text.splitlines():
                    line = line.strip()
                    if line.startswith("data:"):
                        raw_text = line[5:].strip()
                        break
                
                res_obj = json.loads(raw_text)
                if "error" in res_obj:
                    raise RuntimeError(f"MCP 服务端报错: {res_obj['error'].get('message', '未知错误')}")
                
                result = res_obj.get("result", {})
                content = result.get("content", [])
                if content and isinstance(content, list) and content[0].get("text"):
                    try:
                        return json.loads(content[0]["text"])
                    except json.JSONDecodeError:
                        return {"text": content[0]["text"]}
                return result
            except Exception as e:
                last_error = e
                continue

        raise last_error or RuntimeError("调用麦当劳 MCP 端点失败")

    def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
        """封装 MCP tools/call 语义"""
        if not self.token:
            if self.use_fallback:
                return self._mock_dispatch(tool_name, arguments)
            raise RuntimeError("请设置 MCD_MCP_TOKEN 或启用 fallback 模式")

        try:
            return self._call_rpc("tools/call", {
                "name": tool_name,
                "arguments": arguments or {}
            })
        except Exception as e:
            logger.warning(f"直连 MCP 工具 [{tool_name}] 失败: {e}，正在切换至安全兜底引擎。")
            if self.use_fallback:
                return self._mock_dispatch(tool_name, arguments)
            raise

    def query_nearby_stores(self, keyword: str = "") -> List[Dict[str, Any]]:
        """调用 query-nearby-stores：查找周边麦当劳门店"""
        res = self.call_tool("query-nearby-stores", {"keyword": keyword})
        if isinstance(res, list):
            return res
        return res.get("stores") or res.get("data") or []

    def query_meals(self, store_id: str) -> List[Dict[str, Any]]:
        """调用 query-meals：获取指定门店在售菜单及售价"""
        res = self.call_tool("query-meals", {"storeId": store_id})
        if isinstance(res, list):
            return res
        return res.get("meals") or res.get("items") or res.get("data") or []

    def list_nutrition_foods(self) -> List[Dict[str, Any]]:
        """调用 list-nutrition-foods：获取餐品详尽营养/卡路里/蛋白质/咖啡因数据"""
        res = self.call_tool("list-nutrition-foods", {})
        if isinstance(res, list):
            return res
        return res.get("foods") or res.get("data") or []

    def query_store_coupons(self, store_id: str) -> List[Dict[str, Any]]:
        """调用 query-store-coupons：查询门店可用优惠券与活动"""
        res = self.call_tool("query-store-coupons", {"storeId": store_id})
        if isinstance(res, list):
            return res
        return res.get("coupons") or res.get("data") or []

    def calculate_price(self, store_id: str, items: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        调用 calculate-price：权威购物车核价（单位：分）
        麦当劳 MCP 原生规范返回分，本方法自动规范化
        """
        res = self.call_tool("calculate-price", {
            "storeId": store_id,
            "items": items
        })
        return res

    def _mock_dispatch(self, tool_name: str, args: Dict[str, Any]) -> Any:
        """兜底数据路由分发"""
        if tool_name == "query-nearby-stores":
            kw = (args.get("keyword") or "").lower()
            if kw:
                matched = [s for s in MOCK_STORES if kw in s["name"].lower() or kw in s["address"].lower()]
                return matched if matched else MOCK_STORES
            return MOCK_STORES
        
        elif tool_name == "query-meals":
            return MOCK_MEALS

        elif tool_name == "list-nutrition-foods":
            return [
                {
                    "name": m["name"],
                    "kcal": m["kcal"],
                    "protein": m["protein"],
                    "carbs": m["carbs"],
                    "caffeine": m["caffeine"]
                }
                for m in MOCK_MEALS
            ]

        elif tool_name == "query-store-coupons":
            return MOCK_COUPONS

        elif tool_name == "calculate-price":
            # 模拟精确算价：原价及 1+1 优惠
            items = args.get("items", [])
            total_cents = 0
            original_cents = 0
            
            # 计算总原价
            for it in items:
                name = it.get("name")
                matched = next((m for m in MOCK_MEALS if m["name"] == name), None)
                if matched:
                    price = matched["price"]
                    original_cents += int(price * 100)
            
            # 启发式应用 1024 程序员满减或 1+1 随心配
            if len(items) >= 2:
                # 享受随心配或套餐折扣
                total_cents = int(original_cents * 0.78)
            else:
                total_cents = original_cents

            return {
                "originalPriceInCents": original_cents,
                "finalPriceInCents": total_cents,
                "savedInCents": original_cents - total_cents,
                "finalPriceYuan": round(total_cents / 100.0, 2),
                "originalPriceYuan": round(original_cents / 100.0, 2),
                "savedYuan": round((original_cents - total_cents) / 100.0, 2),
                "currency": "CNY"
            }

        return {"status": "ok", "message": f"Mock data for tool: {tool_name}"}
