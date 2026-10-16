#!/usr/bin/env python3
"""Look up layouts: what each is for, which deck type maps to it, and how much it holds.

Usage:
  python layout_info.py                 table of all layouts
  python layout_info.py timeline        one layout: capacity + a deck.json example
  python layout_info.py --check WORK    capacity check of every slide in WORK/deck.json
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import layouts as L  # noqa: E402
import capacity  # noqa: E402
from common import load_json  # noqa: E402

PURPOSE = {
    "cover_hero": "封面", "section": "章节分隔", "closing": "结尾、行动号召",
    "statement_number": "一个核心数字加一句话", "statement_hero": "一句主张配大插画",
    "stats_row": "两到四个数据卡片", "chart": "原生图表加结论（柱、条、折线、饼、环形、堆叠）",
    "table": "原生表格，可高亮一列", "rows_side": "几个并列概念的解释", "grid_cards": "三到六个短要点",
    "list_icons": "条目多、字多时兜底", "steps_flow": "有先后的两到五步", "side_cards": "做法建议，一重一轻",
    "compare_split": "两方对比、前后对比", "cycle": "循环往复的环节", "pyramid": "层级、基础和上层",
    "timeline": "按时间排列的里程碑", "funnel": "逐层转化、逐层筛选", "hub": "一个中心连着几个部分",
    "matrix": "两个维度的 2x2 定位", "framework": "SWOT、PEST、波特五力、商业画布",
    "quote_cards": "例句、提示词、原话", "cards_quote": "风险和坑加一句总结", "media_text": "示意图加讲解",
    "shot_notes": "一张大截图配编号说明，可在图上打编号点", "shot_stack": "两到四张截图并排，步骤或前后对照",
    "free": "手工摆放",
}

EXAMPLES = {
    "shot_notes": {"type": "screenshot", "title": "打开设置页，先改这三处", "image": "media/settings.png",
                   "items": [{"title": "选模型", "text": "左上角下拉框里选最新的那个", "at": [0.3, 0.2]},
                             {"title": "保存", "text": "改完一定要点右下角按钮", "at": [0.85, 0.9]}],
                   "caption": "截图来自 2026 年 10 月版本"},
    "shot_stack": {"type": "screenshots", "title": "三步跑通整个流程",
                   "items": [{"image": "media/a.png", "title": "上传素材", "text": "支持图片和 PDF"},
                             {"image": "media/b.png", "title": "选模板", "text": "后面还能改"},
                             {"image": "media/c.png", "title": "导出", "text": "导出成 pptx"}]},
    "cover_type": {"type": "cover", "layout": "cover_type", "kicker": "2026 年度复盘", "title": "一年涨粉 **10 万**，靠的是什么",
                   "subtitle": "AI 工具号运营复盘", "body": "萝卜哥 · 2026 年 12 月"},
    "question": {"type": "question", "kicker": "先想一个问题", "question": "为什么下载量翻倍，**日活**却没动？",
                 "body": "答案藏在注册后的第一天"},
    "big_quote": {"type": "big_quote", "quote": "下载多不算啥，日活高才说明有人天天用。", "by": "某增长负责人", "note": "2026 年访谈"},
    "toc": {"type": "toc", "title": "目录", "kicker": "CONTENTS",
            "items": [{"title": "一年做了什么", "text": "内容、渠道和节奏"}, {"title": "明年怎么做", "text": "两件事优先"}]},
    "timeline": {"type": "timeline", "title": "两年走完三个阶段", "items": [
        {"date": "2024 Q1", "title": "立项", "text": "三个人验证需求"},
        {"date": "2025 Q2", "title": "增长", "text": "月活突破 10 万", "emphasis": "primary"}]},
    "funnel": {"type": "funnel", "title": "最大的流失在注册之后", "items": [
        {"label": "访问", "value": "12,000", "text": "来自公众号和搜索"},
        {"label": "注册", "value": "3,600", "text": "注册率 30%"}]},
    "hub": {"type": "hub", "title": "一篇内容喂给五个渠道", "center": {"title": "一篇公众号"},
            "items": [{"title": "小红书", "text": "拆成 6 张图文"}, {"title": "视频号", "text": "改成口播"}]},
    "matrix": {"type": "matrix", "title": "先做高价值、低成本的事",
               "x_axis": {"label": "投入成本", "low": "低", "high": "高"},
               "y_axis": {"label": "用户价值", "low": "低", "high": "高"},
               "quadrants": [{"title": "马上做", "items": ["模板复用"], "emphasis": "primary"},
                             {"title": "排进计划", "items": ["多人协作"]}, {"title": "顺手做", "items": ["快捷键"]},
                             {"title": "先不做", "items": ["自研引擎"]}]},
    "table": {"type": "table", "title": "B 方案性价比最高", "columns": ["对比项", "方案 A", "方案 B"],
              "rows": [["月费", "199 元", "99 元"], ["可编辑", "部分", "**全部**"]], "highlight_col": 2,
              "note": "价格为官网标价"},
    "chart": {"type": "chart", "title": "日活是同期的近 3 倍",
              "chart": {"type": "column", "title": "美国移动端日活（万）", "categories": ["同期竞品", "Muse"],
                        "series": [{"name": "日活", "values": [22, 64]}], "highlight": 1, "number_format": "0"},
              "insights": ["下载多不算啥，日活高才说明有人天天用"], "source": "Sensor Tower"},
    "framework": {"type": "framework", "title": "机会大于威胁", "framework": {"kind": "swot", "blocks": {
        "s": ["懂工具，出稿快"], "w": ["一个人精力有限"], "o": ["新工具每周都在出"], "t": ["同质化内容多"]}}},
}


def types_for(layout):
    return [t for t, ls in L.TYPE_TO_LAYOUTS.items() if layout in ls]


def main():
    args = sys.argv[1:]
    if args[:1] == ["--check"]:
        deck = load_json(Path(args[1]) / "deck.json")
        capacity.set_projection(deck.get("meta", {}).get("projection"))
        bad = 0
        for s in deck["slides"]:
            lay = s.get("layout") or L.TYPE_TO_LAYOUTS.get(s.get("type"), ["list_icons"])[0]
            probs = capacity.check(s, lay)
            print(f"{s['n']:>3} {lay:<17} {'OK' if not probs else '；'.join(probs)}")
            bad += bool(probs)
        sys.exit(1 if bad else 0)
    if args:
        name = args[0]
        if name not in L.LAYOUTS:
            raise SystemExit(f"unknown layout {name}")
        print(f"{name}：{PURPOSE.get(name, '')}")
        print(f"对应页型 type：{', '.join(types_for(name)) or '（在 plan.json 里直接指定 layout）'}")
        print(f"插画位：{L.HERO_SLOT.get(name, '无')}")
        print(f"容量：{capacity.summary(name) or '不限'}")
        if name in EXAMPLES:
            print("deck.json 示例：")
            print(json.dumps(EXAMPLES[name], ensure_ascii=False, indent=1))
        return
    print(f"{'版式':<17} {'页型 type':<22} 用途")
    for name in L.LAYOUTS:
        print(f"{name:<17} {', '.join(types_for(name)):<22} {PURPOSE.get(name, '')}")
    print("\n查看单个版式的容量和示例：python layout_info.py <版式名>")


if __name__ == "__main__":
    main()
