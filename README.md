# PPT Design

一个 agent 技能，用来设计**并真正做出来**能讲清楚事的 PPT / 演示文稿。

<div align="center">

中文 | [English](./README_en.md)

</div>

大多数 PPT 失败的原因都一样：它们其实是伪装成幻灯片的文档。幻灯片是**视觉辅助**，不是逐字稿。观众是来听你讲的，不是来读你的页面的。这个技能里的每一页都围绕一个问题展开：这一页只说一件事，那件事是什么？

技能分两半，共用同一套标准：

- **方法论**：怎么想、怎么排。逻辑、视觉、结构三套框架，让它们真正落地的硬数字，以及在上台之前就能挑出坏 deck 的检查项。
- **执行引擎**：怎么真的把文件做出来。两条路径，都输出可编辑的原生 `.pptx`：从主题、文章、脚本或大纲直接生成；或者拿一张参考图美化已有 deck，一个字都不改。

方法论部分可以单独用来做评审、列大纲、写规格，也可以整条链路跑到出文件。

## 它给你什么

三套理论框架，回答三个不同的问题，外加让它们真正落地的硬数字：

| 层 | 框架 | 它回答的问题 |
| --- | --- | --- |
| **逻辑** | 金字塔原理、MECE、SCQA | 论证怎么组织？一个主张站不站得住？ |
| **视觉** | 格式塔、三分法、希克定律、CRAP | 页面怎么排？视线怎么走？ |
| **结构** | 5W2H、SWOT、漏斗、时间线 | 这一页该用哪个容器装？ |

按这个顺序用：先用逻辑层想清楚，再用结构层选容器，最后用视觉层排版。

引擎负责那些算术活和体力活：

- **14 套风格预设**（瑞士网格、墨刊、钴蓝字体、暗黑科技、暖橙等），每套都有版式必须遵守的硬规则
- **一个版式库**，带每种版式的容量，内容装不下会在渲染之前就被发现
- **图标库**、**五维自检**（统一性、层级、细节、沟通、节奏），以及一道 QA 检查：文字缺失、溢出、重叠、过度强调
- **配图是可选的**：可以接 OpenAI、Gemini、火山方舟或自定义端点，也可以退回程序化插图

## 安装

每个 agent 只选**一种**方式。装两种等于装了两份。

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add zxf3023/ppt-design-skill
claude plugin install ppt-design-skills@zxf3023
```

</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
codex plugin marketplace add zxf3023/ppt-design-skill
codex plugin add ppt-design-skills@zxf3023
```

</details>

<details>
<summary><strong>其他 agent（手动）</strong></summary>

把技能目录拷进你的 agent 的 skills 目录：

```bash
cp -r skills/productivity/ppt-design ~/.your-agent/skills/
```

技能是自包含的。首次使用前先跑一次环境检查：它会验证 Python、`python-pptx`、Pillow、numpy 和 lxml，缺什么可以顺手装上：

```bash
python3 scripts/setup_check.py --quick --install
```

建议装 LibreOffice（它负责渲染预览图），但不是必需：没有它会退回 `render_lite.py`，直接按版式数据画一张近似预览。

</details>

## 技能

### 模型可调用

模型或用户都能触达（触发语写得足够丰富，模型才够得着）。

- **[ppt-design](./skills/productivity/ppt-design/SKILL.md)**：设计和产出 deck。方法论部分：逻辑（金字塔原理 / MECE / SCQA）、视觉（格式塔 / 三分法 / 希克定律 / CRAP）、结构（5W2H / SWOT / 漏斗 / 时间线）、字号层级、留白、配色、大段文字的处理、页面模板与叙事节奏。执行引擎部分：从主题、文章、脚本或大纲生成 deck，标题写成结论式，带演讲备注；或者拿一张参考图美化已有的 `.pptx`，不动正文一个字。自带 14 套风格预设、一个图标库，以及一条五维自检链。

## 目录结构

```
skills/productivity/ppt-design/
├── SKILL.md                  # 方法论：11 章
├── agents/openai.yaml        # 显示名与简短描述
├── references/               # 深入文档，按需加载
│   ├── logic-frameworks.md   # 方法论：逻辑层
│   ├── visual-theories.md    # 方法论：视觉层
│   ├── structure-models.md   # 方法论：结构层
│   ├── layout-patterns.md    # 方法论：38 种页面版式
│   ├── design-basics.md      # 方法论：CRAP、留白、对比
│   ├── checklist.md          # 方法论：交付前检查清单
│   ├── generate.md           # 引擎：生成规则
│   ├── deck_schema.md        # 引擎：deck.json 字段与页面类型
│   ├── layouts.md            # 引擎：版式库与容量
│   ├── style_extraction.md   # 引擎：从图片读出 style.json
│   ├── critique.md           # 引擎：五维打分
│   ├── icons.md              # 引擎：图标目录
│   ├── image_prompts.md      # 引擎：插图提示词
│   ├── imagegen_config.md    # 引擎：配图后端配置
│   ├── fonts.md              # 引擎：字体选择与兼容性
│   └── styles/               # 引擎：14 套风格预设（JSON）
├── themes/                   # 方法论：可插拔配色主题
│   ├── business-navy.md
│   └── deep-blue-tech.md
├── scripts/                  # 引擎：23 个 Python 脚本
├── assets/                   # 引擎：图标库、风格图册
└── config.example.json       # 引擎：配图后端模板
```

引擎通过三个中间文件驱动：`deck.json`（每页说什么）、`style.json`（配色、字体、装饰）和 `plan.json`（每页的版式、图标与配图提示词）。脚本做确定性的活，模型做判断。

## 许可

MIT，见 [LICENSE](./LICENSE)。执行引擎派生自 zhouluobo 的 [luobo-ppt](https://github.com/zhouwei713/luobo-ppt)，同为 MIT，见 [LICENSE-luobo-ppt](./LICENSE-luobo-ppt)。
