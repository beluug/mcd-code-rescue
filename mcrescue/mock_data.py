"""
mcrescue.mock_data - 麦当劳官方 MCP 数据的高保真离线镜像与兜底数据
包含北京、上海、深圳代表性门店、真实餐品、价格、卡路里、营养与优惠券结构
"""

MOCK_STORES = [
    {
        "storeId": "MCD-BJ-001",
        "name": "麦当劳（北京中关村软件园餐厅）",
        "address": "北京市海淀区东北旺西路8号中关村软件园二期",
        "distance": "120m",
        "isOpen": True
    },
    {
        "storeId": "MCD-SH-002",
        "name": "麦当劳（上海张江高科传奇广场餐厅）",
        "address": "上海市浦东新区碧波路635号传奇广场1楼",
        "distance": "250m",
        "isOpen": True
    },
    {
        "storeId": "MCD-SZ-003",
        "name": "麦当劳（深圳科技园科兴科学园餐厅）",
        "address": "深圳市南山区科技中三路科兴科学园G层",
        "distance": "80m",
        "isOpen": True
    }
]

# 真实餐品库（含卡路里、蛋白质、咖啡因等营养指标）
MOCK_MEALS = [
    {
        "id": "item-01",
        "name": "巨无霸汉堡 (Big Mac)",
        "category": "burger",
        "price": 25.0,
        "kcal": 525,
        "protein": 26.0,
        "carbs": 44.0,
        "caffeine": 0,
        "tag": "经典图腾·万物起源",
        "desc": "双层牛肉搭配特调巨无霸酱，100%纯牛肉煎烤，程序员终极多巴胺补给。"
    },
    {
        "id": "item-02",
        "name": "原味板烧鸡腿堡 (Grilled Chicken Burger)",
        "category": "burger",
        "price": 24.5,
        "kcal": 402,
        "protein": 24.5,
        "carbs": 38.0,
        "caffeine": 0,
        "tag": "极客高蛋白·低脂首选",
        "desc": "整块鲜嫩去骨鸡腿肉铁板煎制，无裹粉油炸，健身与久坐码农的抗熵福音。"
    },
    {
        "id": "item-03",
        "name": "麦辣鸡腿汉堡 (Spicy McChicken)",
        "category": "burger",
        "price": 22.0,
        "kcal": 518,
        "protein": 21.0,
        "carbs": 48.0,
        "caffeine": 0,
        "tag": "提神爆辣·代码除虫",
        "desc": "辣椒腌制酥脆鸡腿排，一口咬下去辣意直冲天灵盖，瞬间轰散熬夜睡意。"
    },
    {
        "id": "item-04",
        "name": "双层吉士汉堡 (Double Cheeseburger)",
        "category": "burger",
        "price": 21.5,
        "kcal": 450,
        "protein": 25.0,
        "carbs": 34.0,
        "caffeine": 0,
        "tag": "1+1穷鬼顶梁柱",
        "desc": "香浓车达芝士融化在双层纯牛肉上，极致性价比的麦门教义实体。"
    },
    {
        "id": "item-05",
        "name": "大号金黄薯条 (Large French Fries)",
        "category": "side",
        "price": 16.0,
        "kcal": 434,
        "protein": 5.0,
        "carbs": 58.0,
        "caffeine": 0,
        "tag": "碳水炸弹·多巴胺狂欢",
        "desc": "外脆内绵金黄马铃薯条，抓一把蘸番茄酱，快速恢复思考消耗的血糖。"
    },
    {
        "id": "item-06",
        "name": "麦乐鸡 (5块装 McNugets)",
        "category": "side",
        "price": 13.5,
        "kcal": 269,
        "protein": 14.0,
        "carbs": 16.0,
        "caffeine": 0,
        "tag": "甜酸酱信仰·一口一个",
        "desc": "外酥里嫩鸡肉块，配经典甜酸酱，单手敲代码也能吃的随行零食。"
    },
    {
        "id": "item-07",
        "name": "麦辣鸡翅 (4块装 McWings)",
        "category": "side",
        "price": 20.0,
        "kcal": 405,
        "protein": 23.0,
        "carbs": 18.0,
        "caffeine": 0,
        "tag": "咔哧酥脆·解压利器",
        "desc": "酥脆金黄裹粉包裹多汁翅中，撕咬感带来极致的压力释放。"
    },
    {
        "id": "item-08",
        "name": "鲜萃美式咖啡 (大杯 McCafé Americano)",
        "category": "drink",
        "price": 18.0,
        "kcal": 15,
        "protein": 1.0,
        "carbs": 2.0,
        "caffeine": 150,
        "tag": "超频核心·CPU超载防御",
        "desc": "100%雨林联盟认证阿拉比卡咖啡豆，零糖低卡，150mg咖啡因强行拉满认知算力。"
    },
    {
        "id": "item-09",
        "name": "鲜萃厚乳拿铁 (大杯 McCafé Latte)",
        "category": "drink",
        "price": 22.0,
        "kcal": 195,
        "protein": 8.5,
        "carbs": 16.0,
        "caffeine": 120,
        "tag": "温润醇香·抚慰神经",
        "desc": "浓郁精萃浓缩咖啡融于丝滑厚牛乳，抚平因需求变更受创的心灵。"
    },
    {
        "id": "item-10",
        "name": "零度可口可乐 (中杯 Coca-Cola Zero)",
        "category": "drink",
        "price": 10.5,
        "kcal": 1,
        "protein": 0,
        "carbs": 0,
        "caffeine": 35,
        "tag": "无糖气泡·爽口回血",
        "desc": "冰爽劲爽无负担，气泡充斥口腔带来激爽振奋。"
    },
    {
        "id": "item-11",
        "name": "奥利奥麦旋风 (Oreo McFlurry)",
        "category": "dessert",
        "price": 14.5,
        "kcal": 340,
        "protein": 6.5,
        "carbs": 52.0,
        "caffeine": 0,
        "tag": "快乐源泉·多巴胺巅峰",
        "desc": "浓郁冰淇淋混合酥脆奥利奥饼干碎，代码通过 CI/CD 时的庆功甜品。"
    },
    {
        "id": "item-12",
        "name": "香芋派 (Taro Pie)",
        "category": "dessert",
        "price": 9.0,
        "kcal": 230,
        "protein": 2.5,
        "carbs": 33.0,
        "caffeine": 0,
        "tag": "温暖酥脆·治愈胃袋",
        "desc": "经典千层酥皮夹着滚烫细腻香芋粒，入口满满童年幸福感。"
    }
]

# 优惠券与随心配组合
MOCK_COUPONS = [
    {
        "couponId": "CPN-1024-01",
        "title": "1024程序员专属：随心配 1+1 仅需 ¥13.9",
        "discountType": "fixed_price",
        "targetCategory": ["burger", "drink"],
        "price": 13.9,
        "desc": "红区选双吉/麦乐鸡/板烧，白区选零度/咖啡/派，立省高达 40%"
    },
    {
        "couponId": "CPN-1024-02",
        "title": "巨无霸超值三件套专享券：¥29.9 (原价 ¥48)",
        "discountType": "combo",
        "price": 29.9,
        "desc": "巨无霸 + 中薯 + 中可乐，程序员节专属折扣"
    },
    {
        "couponId": "CPN-1024-03",
        "title": "麦咖啡第2杯半价提神券",
        "discountType": "discount",
        "desc": "购买任意麦咖啡现磨系列，第二杯立享 5 折"
    }
]
