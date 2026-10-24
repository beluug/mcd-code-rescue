# 🍟 McRescue · 麦门代码急救站

> **献给 1024 程序员节**：代码死锁？需求突变？服务宕机？麦当劳官方 MCP 权威开方，一键拯救宕机打工人！

[![1024 Hackathon](https://img.shields.io/badge/1024_Hackathon-McDonald's_China-DA291C?style=for-the-badge&logo=mcdonalds)](https://github.com/M-China/mcd-developer-innovation-challenge)
[![MCP Protocol](https://img.shields.io/badge/MCP-Streamable_HTTP-FFBC0D?style=for-the-badge&logo=json)](https://open.mcd.cn/mcp)
[![WorkBuddy Partner](https://img.shields.io/badge/WorkBuddy-Partner_Skill-0052D9?style=for-the-badge)](https://www.workbuddy.cn)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

---

## 💡 项目背景 (Why McRescue?)

在日常研发工作中，每个程序员都会面临身心耗竭的临界点：
- 🚨 **周五晚 21:00 生产环境突发 P0 宕机**，老板站在身后，心率飙升到 160；
- 🌀 **Git Rebase 产生 500 行恶性冲突**，手抖心慌，不敢看 Commit Log；
- ⚡ **需求发版前夕遭遇第 7 次大改**，键盘火星四溅，脑力完全透支；
- 🪙 **月底深夜加班钱包见底**，饥寒交迫，急需极致性价比的能量救赎。

**McRescue（麦门代码急救站）** 基于 **麦当劳中国官方 Model Context Protocol (MCP)** 开放中枢，将程序员的“代码病情诊断”与麦当劳官方在售餐品、宏量营养指标（卡路里、蛋白质、咖啡因）以及精准价格试算深度结合。提供**即开即用的 Web 诊断台**、**Canvas 麦门极客工牌海报生成器**、**Python CLI 终端**及 **WorkBuddy 专家技能**。

---

## ✨ 核心特性 (Key Features)

### 1. 🩺 1024 程序员高危病症诊断引擎
支持 5 大经典程序员并发症挂号问诊，亦可直接输入真实 StackTrace 报错日志：
- **🚨 生产环境 P0 级宕机 (Panic Level 5)**：极度虚脱，处方暴击多巴胺与纯牛双层肉饼；
- **🌀 Git 冲突 500 行 (Conflict Shock)**：精神过载，处方温润香芋派与厚乳拿铁安抚神经；
- **⚡ 需求发版前突变 (Scope Creep)**：算力见底，处方麦辣鸡腿堡 + 150mg 纯阿拉比卡咖啡因强行超频；
- **🪙 深夜穷鬼加班 (Budget Underflow)**：钱包见底，处方 1+1 随心配极致抗熵解（仅需 ¥13.9）；
- **💪 极客久坐抗衰减脂 (Clean Eating)**：防脂肪肝，处方板烧去酱 + 大美式高蛋白控卡方案。

### 2. 🍔 深度集成麦当劳官方 MCP 全量只读工具链
- `query-nearby-stores`：秒级近场定位程序员所在办公园区（中关村、张江、科兴等）；
- `query-meals`：直连门店获取最新在售餐品与牌价；
- `list-nutrition-foods`：权威核算热量 (kcal)、蛋白质 (g)、碳水 (g) 与咖啡因 (mg)；
- `query-store-coupons`：实时匹配 1+1 随心配与超值套餐优惠券；
- `calculate-price`：官方购物车精准算价（精确到分），输出真实立省金额。

### 3. 🎨 麦门极客工牌与救赎处方笺生成器 (Viral Poster)
前端采用 Canvas 实时动态合成极具极客美学与麦当劳经典金黄/正红配色的工牌海报：
- 印有极客工号、诊断病症、官方开方餐品、宏量营养条与 **麦门圣训金句**；
- 支持 **一键下载高清 PNG 海报** 或 **一键复制 Markdown 处方**，轻松分享朋友圈、掘金、V2EX 与技术交流群！

### 4. ⚡ 零依赖双驱动架构 (Live 直连 + 离线试车)
- **Live 模式**：输入从 `open.mcd.cn/mcp` 获取的 Bearer Token，实时与麦当劳官方生产服务交互；
- **离线 Mock 模式**：内置完整的高保真脱敏数据镜像，评审专家或用户无需任何 Token 即可 100% 体验全部流程。

---

## 🚀 极速上手 (Quick Start)

### 方式一：直接在浏览器中打开 (零门槛体验)
项目根目录下的 `index.html` 为完全自包含的 Web 应用，无需安装 Node.js、无需构建编译：
1. 双击打开 `index.html`（或使用 VS Code Live Server / 开启本地静态服务器）；
2. 选择病症或输入工号，点击 **【🍟 麦当劳 MCP 权威开方】**；
3. 点击 **【💾 下载工牌海报】** 即可保存专属的 1024 麦门极客工牌！

### 方式二：Python 命令行极客交互
无需安装第三方外部依赖（使用 Python 3.8+ 标准库）：

```bash
# 1. 默认体验生产 P0 宕机急救
python -m mcrescue.cli --case FATAL_CRASH --name "麦门架构师"

# 2. 体验发版前突变超频咖啡因处方
python -m mcrescue.cli --case REQUIREMENT_CHANGED --keyword "张江高科"

# 3. 直连官方 MCP（设置环境变量）
export MCD_MCP_TOKEN="你的官方Token"
python -m mcrescue.cli --case POOR_GUY_OVERTIME
```

### 方式三：接入腾讯 WorkBuddy 智能体
1. 打开 WorkBuddy，进入 **【专家 · 技能 · 连接器】** -> **【自定义连接器】** -> **【配置 MCP】**；
2. 导入本仓库的 `mcp-config.example.json` 并填入您的 Token；
3. 详细对话调优上下文见 [workbuddy.md](./workbuddy.md)。

---

## 📂 项目仓库结构 (符合大赛规范)

```text
├── README.md                 # 项目介绍、使用指南、目标用户（必须）
├── CONTEST_DECLARATION.md    # 参赛承诺与合规原创性声明（必须，官方原文未改）
├── MCP_INTEGRATION.md        # 麦当劳官方 MCP Server/Tool 详细调用规范（必须）
├── mcp-config.example.json   # 脱敏后的 MCP 配置文件示例（必须）
├── workbuddy.md              # WorkBuddy 智能体对话上下文（必须，参加专项奖）
├── requirements.txt          # 项目依赖说明（零硬依赖，极速运行）
├── index.html                # 麦门代码急救站 Web 交互应用 & 工牌生成器
└── mcrescue/                 # 核心模块代码
    ├── __init__.py           # 包定义
    ├── client.py             # 麦当劳官方 Streamable HTTP MCP 客户端 (JSON-RPC 2.0)
    ├── prescription.py       # 程序员病情诊断与营养对冲引擎
    ├── cli.py                # 终端命令行交互界面
    └── mock_data.py          # 高保真离线 Mock 镜像数据集
```

---

## 🎯 目标用户群体

1. **一线软件工程师 / SRE / 运维人员**：高压排障、突发 Oncall 期间急需高效率、高能量、低决策成本的补给方案；
2. **注重健康管理的极客**：需要科学掌控久坐卡路里与宏量营养素（高蛋白、低升糖）；
3. **预算敏感型开发者**：追求 1+1 随心配等极致省钱策略的实用主义者；
4. **技术社群与麦门文化爱好者**：渴望在 1024 程序员节表达极客文化、分享趣味工牌的广大开发者。

---

## ⚖️ 声明与协议

- 本项目遵循 **[MIT 许可证](LICENSE)** 开源。
- 本项目系麦当劳程序员节创意开发大赛参赛独立作品，详细合规声明详见 **[CONTEST_DECLARATION.md](./CONTEST_DECLARATION.md)**。
