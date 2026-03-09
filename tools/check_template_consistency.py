#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path

LECTURE_TITLES = [
    "1. 论文概览卡片",
    "2. 研究逻辑与故事主线",
    "3. 引言导读",
    "4. 摘要精读",
    "5. Figure逐图精读与逻辑串联",
    "6. 核心方法学精读",
    "7. 方法学批判",
    "8. 讨论导读",
    "9. 课堂讨论题",
]

LECTURE_TITLES_EN = [
    "1. Paper Overview Card",
    "2. Research Logic & Storyline",
    "3. Introduction Guide",
    "4. Abstract Deep Dive",
    "5. Figure-by-Figure Analysis & Logic Chain",
    "6. Core Methods Deep Dive",
    "7. Methods Critique",
    "8. Discussion Guide",
    "9. Discussion Questions",
]

LECTURE_BLOCKS = [
    'class="figure-section"',
    'class="logic-box"',
    'class="caption-box"',
    'class="quote-box"',
    'class="steps-box"',
    'class="results-box"',
    'class="panel-details"',
]

BIBLIO_IDS = [
    'id="net"',
    'id="sankey"',
    'id="methodHeat"',
    'id="domainHeat"',
    'id="domainTrend"',
    'id="thematicMap"',
    'id="treeMap"',
    'id="yearSlider"',
    'id="yearBadge"',
]

BIBLIO_MARKERS = [
    "function renderByYear",
    "Plotly.newPlot('sankey'",
    "Plotly.newPlot('methodHeat'",
    "Plotly.newPlot('domainHeat'",
    "Plotly.newPlot('domainTrend'",
    "Plotly.newPlot('thematicMap'",
    "Plotly.newPlot('treeMap'",
]


def find_missing(content: str, required: list[str]) -> list[str]:
    return [item for item in required if item not in content]


def check_lecture(content: str) -> tuple[bool, list[str]]:
    issues = []

    missing_titles = find_missing(content, LECTURE_TITLES)
    if missing_titles:
        issues.append(f"缺少章节标题: {', '.join(missing_titles)}")

    card_count = len(re.findall(r'<section\s+class="card"', content))
    if card_count < 9:
        issues.append(f"section.card 数量不足: {card_count} < 9")

    missing_blocks = find_missing(content, LECTURE_BLOCKS)
    if missing_blocks:
        issues.append(f"缺少Figure区块: {', '.join(missing_blocks)}")

    fig_count = len(re.findall(r'class="figure-section"', content))
    if fig_count < 3:
        issues.append(f"figure-section 数量异常偏少: {fig_count}")

    for block in ["logic-box", "caption-box", "quote-box", "steps-box", "results-box"]:
        cnt = len(re.findall(rf'class="{block}"', content))
        if cnt < fig_count:
            issues.append(f"{block} 数量不足: {cnt} < figure-section({fig_count})")

    quote_count = len(re.findall(r'class="quote-box"', content))
    if quote_count < fig_count:
        issues.append(
            f"quote-box 数量不足: {quote_count} < figure-section({fig_count})"
        )

    if "相关原文提取" not in content:
        issues.append("缺少 Results 原文提取标签：相关原文提取")

    for token in ["n=", "P<", "scale", "bar"]:
        if token not in content:
            issues.append(f"疑似缺少关键定量信息标记: {token}")
            break

    img_tags = re.findall(r"<img\b[^>]*>", content, flags=re.IGNORECASE)
    if len(img_tags) < fig_count:
        issues.append(
            f"图片标签不足: img({len(img_tags)}) < figure-section({fig_count})"
        )
    for tag in img_tags:
        src_match = re.search(
            r"\bsrc\s*=\s*['\"]([^'\"]*)['\"]", tag, flags=re.IGNORECASE
        )
        if not src_match:
            issues.append("检测到缺少src属性的<img>标签")
            continue
        src = src_match.group(1).strip().lower()
        if src in ["", "#", "javascript:void(0)"]:
            issues.append(f"检测到无效图片src: {src or '<empty>'}")

    sections = re.findall(
        r'<section\s+class="card"[^>]*>(.*?)</section>',
        content,
        flags=re.IGNORECASE | re.DOTALL,
    )
    for idx, sec in enumerate(sections, 1):
        text = re.sub(r"<[^>]+>", "", sec)
        text = re.sub(r"\s+", "", text)
        if len(text) < 12:
            issues.append(f"第{idx}个section内容疑似为空")

    return (len(issues) == 0, issues)


def check_lecture_en(content: str) -> tuple[bool, list[str]]:
    issues = []

    missing_titles = find_missing(content, LECTURE_TITLES_EN)
    if missing_titles:
        issues.append(f"Missing section titles: {', '.join(missing_titles)}")

    card_count = len(re.findall(r'<section\s+class="card"', content))
    if card_count < 9:
        issues.append(f"section.card count too low: {card_count} < 9")

    missing_blocks = find_missing(content, LECTURE_BLOCKS)
    if missing_blocks:
        issues.append(f"Missing figure blocks: {', '.join(missing_blocks)}")

    fig_count = len(re.findall(r'class="figure-section"', content))
    if fig_count < 1:
        issues.append("figure-section count too low")

    for block in ["logic-box", "caption-box", "quote-box", "steps-box", "results-box"]:
        cnt = len(re.findall(rf'class="{block}"', content))
        if cnt < fig_count:
            issues.append(f"{block} count too low: {cnt} < figure-section({fig_count})")

    quote_count = len(re.findall(r'class="quote-box"', content))
    if quote_count < fig_count:
        issues.append(
            f"quote-box count too low: {quote_count} < figure-section({fig_count})"
        )

    if "Quoted Results text" not in content and "Results" not in content:
        issues.append("Missing Results quote marker")

    img_tags = re.findall(r"<img\b[^>]*>", content, flags=re.IGNORECASE)
    if len(img_tags) < fig_count:
        issues.append(
            f"img count too low: {len(img_tags)} < figure-section({fig_count})"
        )
    for tag in img_tags:
        src_match = re.search(
            r"\bsrc\s*=\s*['\"]([^'\"]*)['\"]", tag, flags=re.IGNORECASE
        )
        if not src_match:
            issues.append("Detected <img> tag without src")
            continue
        src = src_match.group(1).strip().lower()
        if src in ["", "#", "javascript:void(0)"]:
            issues.append(f"Detected invalid image src: {src or '<empty>'}")

    sections = re.findall(
        r'<section\s+class="card"[^>]*>(.*?)</section>',
        content,
        flags=re.IGNORECASE | re.DOTALL,
    )
    for idx, sec in enumerate(sections, 1):
        text = re.sub(r"<[^>]+>", "", sec)
        text = re.sub(r"\s+", "", text)
        if len(text) < 12:
            issues.append(f"Section {idx} appears empty")

    return (len(issues) == 0, issues)


def check_biblio(content: str) -> tuple[bool, list[str]]:
    issues = []

    missing_ids = find_missing(content, BIBLIO_IDS)
    if missing_ids:
        issues.append(f"缺少关键容器/控件: {', '.join(missing_ids)}")

    missing_markers = find_missing(content, BIBLIO_MARKERS)
    if missing_markers:
        issues.append(f"缺少关键脚本标记: {', '.join(missing_markers)}")

    if "year <= y" in content:
        issues.append("检测到累计年度逻辑 year <= y（建议按年模式 year === y）")

    return (len(issues) == 0, issues)


def infer_mode(path: Path) -> str:
    name = path.name
    lower_name = name.lower()
    if "lecture-en" in lower_name:
        return "lecture-en"
    if "讲义" in name or "lecture" in lower_name:
        return "lecture"
    return "biblio"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check HTML consistency against skill templates"
    )
    parser.add_argument("html", type=Path, help="Path to generated HTML")
    parser.add_argument(
        "--mode", choices=["lecture", "lecture-en", "biblio", "auto"], default="auto"
    )
    args = parser.parse_args()

    if not args.html.exists():
        print(f"[FAIL] 文件不存在: {args.html}")
        return 2

    content = args.html.read_text(encoding="utf-8", errors="ignore")
    mode = infer_mode(args.html) if args.mode == "auto" else args.mode

    if mode == "lecture":
        ok, issues = check_lecture(content)
    elif mode == "lecture-en":
        ok, issues = check_lecture_en(content)
    else:
        ok, issues = check_biblio(content)

    print(f"[MODE] {mode}")
    print(f"[FILE] {args.html}")

    if ok:
        print("[PASS] 模板一致性检查通过")
        return 0

    print("[FAIL] 模板一致性检查未通过")
    for i, issue in enumerate(issues, 1):
        print(f"  {i}. {issue}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
