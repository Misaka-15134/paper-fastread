#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <html_file> [lecture|lecture-en|biblio|auto]"
  exit 2
fi

FILE="$1"
MODE="${2:-auto}"

if [ ! -f "$FILE" ]; then
  echo "[FAIL] file not found: $FILE"
  exit 2
fi

if [ "$MODE" = "auto" ]; then
  base="$(basename "$FILE")"
  if echo "$base" | grep -qiE "lecture-en"; then
    MODE="lecture-en"
  elif echo "$base" | grep -qiE "讲义|lecture"; then
    MODE="lecture"
  else
    MODE="biblio"
  fi
fi

issues=0

check_contains() {
  local token="$1"
  if ! grep -Fq "$token" "$FILE"; then
    echo "  - missing: $token"
    issues=$((issues+1))
  fi
}

echo "[MODE] $MODE"
echo "[FILE] $FILE"

if [ "$MODE" = "lecture" ]; then
  for t in "1. 论文概览卡片" "2. 研究逻辑与故事主线" "3. 引言导读" "4. 摘要精读" "5. Figure逐图精读与逻辑串联" "6. 核心方法学精读" "7. 方法学批判" "8. 讨论导读" "9. 课堂讨论题"; do
    check_contains "$t"
  done
  for t in 'class="figure-section"' 'class="logic-box"' 'class="caption-box"' 'class="quote-box"' 'class="steps-box"' 'class="results-box"' 'class="panel-details"'; do
    check_contains "$t"
  done
  check_contains "相关原文提取"
elif [ "$MODE" = "lecture-en" ]; then
  for t in "1. Paper Overview Card" "2. Research Logic & Storyline" "3. Introduction Guide" "4. Abstract Deep Dive" "5. Figure-by-Figure Analysis & Logic Chain" "6. Core Methods Deep Dive" "7. Methods Critique" "8. Discussion Guide" "9. Discussion Questions"; do
    check_contains "$t"
  done
  for t in 'class="figure-section"' 'class="logic-box"' 'class="caption-box"' 'class="quote-box"' 'class="steps-box"' 'class="results-box"' 'class="panel-details"'; do
    check_contains "$t"
  done
else
  for t in 'id="net"' 'id="sankey"' 'id="methodHeat"' 'id="domainHeat"' 'id="domainTrend"' 'id="thematicMap"' 'id="treeMap"' 'id="yearSlider"' 'id="yearBadge"' 'function renderByYear' "Plotly.newPlot('sankey'" "Plotly.newPlot('methodHeat'" "Plotly.newPlot('domainHeat'" "Plotly.newPlot('domainTrend'" "Plotly.newPlot('thematicMap'" "Plotly.newPlot('treeMap'"; do
    check_contains "$t"
  done
  if grep -Fq "year <= y" "$FILE"; then
    echo "  - warning: detected cumulative logic (year <= y), recommended year === y"
  fi
fi

if [ "$issues" -eq 0 ]; then
  echo "[PASS] template consistency check passed"
  exit 0
else
  echo "[FAIL] template consistency check failed, issues=$issues"
  exit 1
fi
