"""
mcrescue.cli - 麦门代码急救站命令行客户端
支持终端交互式问诊、参数化开方、ASCII 卡片渲染
"""

import sys
import argparse

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from mcrescue.client import McDonaldsMCPClient
from mcrescue.prescription import PrescriptionEngine, DIAGNOSES

BANNER = r"""
  __  __      _____                               
 |  \/  |    |  __ \                              
 | \  / | ___| |__) |___  ___  ___ _   _  ___     
 | |\/| |/ __|  _  // _ \/ __|/ __| | | |/ _ \    
 | |  | | (__| | \ \  __/\__ \ (__| |_| |  __/    
 |_|  |_|\___|_|  \_\___||___/\___|\__,_|\___|    
    [ 麦门代码急救站 · 1024 程序员能量诊断与救赎站 ]
"""

def render_prescription_card(p: dict):
    print("\n" + "=" * 65)
    print(f"       🍟 麦当劳官方 MCP · 1024 程序员代码续命处方笺 🍟")
    print("=" * 65)
    print(f"【患者极客】: {p['developer']}")
    print(f"【所属门店】: {p['store']['name']}")
    print(f"【病情诊断】: {p['title']}")
    print(f"【病理表征】: {p['symptom']}")
    print(f"【机体状态】: {p['burnout']} ──> 需要：{p['need']}")
    print("-" * 65)
    print("【麦当劳 MCP 权威开方】:")
    for idx, item in enumerate(p['items'], 1):
        print(f"  {idx}. {item['name']} (¥{item['price']}) - [{item['tag']}]")
        print(f"     -> {item['desc']}")
    print("-" * 65)
    pr = p['pricing']
    nu = p['nutrition']
    gk = p['geek_metrics']
    print(f"【价格试算】: 现价 ¥{pr['finalPrice']} (原价 ¥{pr['originalPrice']}，立省 ¥{pr['savedMoney']})")
    print(f"【营养构成】: 热量 {nu['caloriesKcal']} kcal | 蛋白质 {nu['proteinG']}g | 咖啡因 {nu['caffeineMg']}mg")
    print(f"【战力加成】: 除虫战力 {gk['debugPowerBoost']} | 大脑内存释放 {gk['brainRamFreed']} | 精神护甲 {gk['mentalArmor']}")
    print("=" * 65)
    print(f"【麦门圣训】: \"{p['motto']}\"")
    print("=" * 65 + "\n")

def main():
    parser = argparse.ArgumentParser(description="麦门代码急救站 (McRescue) 1024 命令行客户端")
    parser.add_argument("--case", choices=list(DIAGNOSES.keys()), default="FATAL_CRASH", help="故障/病情代码")
    parser.add_argument("--name", default="麦门极客", help="开发者昵称")
    parser.add_argument("--keyword", default="", help="门店搜索关键词（例如：中关村/张江/科兴）")
    parser.add_argument("--bug", default="", help="自定义报错日志或病情自述")
    parser.add_argument("--token", default="", help="麦当劳官方 MCP Token（可选，不填启用安全模拟引擎）")

    args = parser.parse_args()

    print(BANNER)
    client = McDonaldsMCPClient(token=args.token)
    engine = PrescriptionEngine(client)

    print(f"[*] 正在接入麦当劳中国 MCP 中枢（端点: {client.base_url}）...")
    if client.is_live:
        print("[+] 检测到有效 Bearer Token，已激活 Live 实时生产中枢。")
    else:
        print("[!] 未指定 MCD_MCP_TOKEN，已安全切换至高保真离线 Mock 试车模式。")

    prescription = engine.generate_prescription(
        case_key=args.case,
        user_name=args.name,
        store_keyword=args.keyword,
        custom_bug_msg=args.bug
    )

    render_prescription_card(prescription)

if __name__ == "__main__":
    main()
