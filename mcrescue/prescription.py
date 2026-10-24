"""
mcrescue.prescription - 1024 程序员代码续命与能量诊断处方引擎
将程序员代码/工作状态、Bug 严重度、加班疲劳度转化为精准的麦当劳营养与餐品处方
"""

import math
from typing import Dict, Any, List, Optional
from mcrescue.client import McDonaldsMCPClient

DIAGNOSES = {
    "FATAL_CRASH": {
        "title": "🚨 生产环境 P0 级宕机 (Panic Level 5)",
        "symptom": "NullPointerException 连环引爆，老板站在身后两眼放光，心率 160+",
        "burnout": "极度虚脱 (HP: 5%)",
        "need": "多巴胺超量灌注 + 极限高能复活",
        "recommended_tags": ["经典图腾·万物起源", "甜酸酱信仰·一口一个", "无糖气泡·爽口回血"],
        "motto": "服务可以挂，麦门信徒的心态不能挂。吃完巨无霸，重启能解万般难。"
    },
    "REBASE_CONFLICT": {
        "title": "🌀 Git Rebase 冲突 500 行 (Conflict Shock)",
        "symptom": "HEAD detached，修改被覆盖，手抖心慌，不敢看 git log",
        "burnout": "焦虑过载 (HP: 25%)",
        "need": "温润碳水抚慰 + 神经安抚",
        "recommended_tags": ["极客高蛋白·低脂首选", "温暖酥脆·治愈胃袋", "温润醇香·抚慰神经"],
        "motto": "代码终会合并，热气腾腾的香芋派才是现实世界永不冲突的主分支。"
    },
    "REQUIREMENT_CHANGED": {
        "title": "⚡ 需求发版前第 7 次突变 (Scope Creep)",
        "symptom": "原本说只改个按钮颜色，现在要重写底层架构，键盘火星四溅",
        "burnout": "脑力透支 (HP: 15%)",
        "need": "强劲咖啡因超频 + 暴击辣意除虫",
        "recommended_tags": ["提神爆辣·代码除虫", "碳水炸弹·多巴胺狂欢", "超频核心·CPU超载防御"],
        "motto": "没有一个 Bug 能逃脱麦辣鸡腿堡的制裁，150mg 咖啡因强开认知超频！"
    },
    "POOR_GUY_OVERTIME": {
        "title": "🪙 月底穷鬼深夜加班 (Budget Underflow)",
        "symptom": "钱包只剩两位数，饥肠辘辘，却还在为公司的万亿梦想写脚本",
        "burnout": "饥寒交迫 (HP: 20%)",
        "need": "1+1 随心配极致省钱抗熵解",
        "recommended_tags": ["1+1穷鬼顶梁柱", "无糖气泡·爽口回血"],
        "motto": "13.9 元随心配，是资本世界里麦门留给无产阶级程序员最后的温柔。"
    },
    "FIT_HACKER": {
        "title": "💪 极客久坐抗衰减脂 (Clean Eating)",
        "symptom": "日行 200 步，颈椎僵硬，既想抗疲劳又严防脂肪肝",
        "burnout": "亚健康预警 (HP: 50%)",
        "need": "低升糖优质蛋白质 + 零糖燃脂",
        "recommended_tags": ["极客高蛋白·低脂首选", "超频核心·CPU超载防御"],
        "motto": "板烧去酱加美式，代码健壮腹肌在。自律的程序员掌控系统掌控人生。"
    }
}

class PrescriptionEngine:
    """处方生成与营养对冲引擎"""

    def __init__(self, client: Optional[McDonaldsMCPClient] = None):
        self.client = client or McDonaldsMCPClient()

    def generate_prescription(
        self,
        case_key: str = "FATAL_CRASH",
        user_name: str = "麦门极客",
        store_keyword: str = "",
        custom_bug_msg: str = ""
    ) -> Dict[str, Any]:
        """
        全流程串联麦当劳官方 MCP 能力：
        1. query-nearby-stores 门店定位
        2. query-meals 菜单检索
        3. list-nutrition-foods 营养与卡路里核对
        4. calculate-price 权威核价
        5. 生成个性化麦门极客工牌诊断单
        """
        # 1. 门店定位
        stores = self.client.query_nearby_stores(store_keyword)
        target_store = stores[0] if stores else {
            "storeId": "MCD-ONLINE-01",
            "name": "麦当劳（数字云端旗舰店）",
            "address": "全国联网就近配送"
        }
        store_id = target_store.get("storeId", "MCD-001")
        store_name = target_store.get("name", "麦当劳餐厅")

        # 2. 诊断匹配
        diag_info = DIAGNOSES.get(case_key, DIAGNOSES["FATAL_CRASH"])
        target_tags = diag_info["recommended_tags"]

        # 3. 菜单与营养拉取
        meals = self.client.query_meals(store_id)
        nutrition_list = self.client.list_nutrition_foods()
        nutr_map = {n.get("name"): n for n in nutrition_list}

        # 根据处方画像挑选餐品
        prescribed_items = []
        for tag in target_tags:
            matched = next((m for m in meals if m.get("tag") == tag), None)
            if matched:
                prescribed_items.append(matched)

        # 兜底确保至少包含主食与饮品
        if not prescribed_items:
            prescribed_items = meals[:2]

        # 4. 精准核价 (调用 calculate-price)
        calc_payload = [{"name": it["name"], "count": 1} for it in prescribed_items]
        price_result = self.client.calculate_price(store_id, calc_payload)

        # 5. 营养与战力计算
        total_kcal = 0
        total_protein = 0.0
        total_carbs = 0.0
        total_caffeine = 0

        for it in prescribed_items:
            name = it["name"]
            nutr = nutr_map.get(name) or it
            total_kcal += nutr.get("kcal", 0)
            total_protein += nutr.get("protein", 0.0)
            total_carbs += nutr.get("carbs", 0.0)
            total_caffeine += nutr.get("caffeine", 0)

        # 衍生极客指标
        debug_boost = min(99, int(total_protein * 1.5 + total_caffeine * 0.2 + 40))
        ram_freed = min(98, int(total_kcal / 12.0 + 35))
        mental_armor = 999 if total_caffeine > 100 else 666

        final_price = price_result.get("finalPriceYuan", sum(it.get("price", 0) for it in prescribed_items))
        saved_money = price_result.get("savedYuan", 0.0)

        return {
            "doctor": "麦当劳 MCP 代码急救站 AI 首席营养架构师",
            "developer": user_name,
            "case_key": case_key,
            "title": diag_info["title"],
            "symptom": custom_bug_msg if custom_bug_msg else diag_info["symptom"],
            "burnout": diag_info["burnout"],
            "need": diag_info["need"],
            "store": {
                "id": store_id,
                "name": store_name,
                "address": target_store.get("address", "")
            },
            "items": prescribed_items,
            "pricing": {
                "finalPrice": final_price,
                "originalPrice": price_result.get("originalPriceYuan", final_price + saved_money),
                "savedMoney": saved_money,
                "currency": "CNY"
            },
            "nutrition": {
                "caloriesKcal": round(total_kcal, 1),
                "proteinG": round(total_protein, 1),
                "carbsG": round(total_carbs, 1),
                "caffeineMg": total_caffeine
            },
            "geek_metrics": {
                "debugPowerBoost": f"+{debug_boost}%",
                "brainRamFreed": f"{ram_freed}%",
                "mentalArmor": f"+{mental_armor} 点防御",
                "hpRecovery": "满血复活 (100%)"
            },
            "motto": diag_info["motto"],
            "timestamp": "2026-10-24 10:24:00 (1024 程序员节专供)"
        }
