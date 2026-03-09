# 讲义与文献计量模板锚定（HTML基准）

## A. 讲义模板（强制基准）

- 基准文件：`templates/lecture-template.html`
- 来源：`讲义2_多组学光老化_PMID34241612.html`
- 要求：后续生成讲义时，保持该模板的版式风格与信息层级（卡片、figure-section、logic/caption/quote/steps/results结构）。

### 讲义内容骨架（9章节）

1. 论文概览卡片
2. 研究逻辑与故事主线
3. 引言导读（原文引用+中文解读）
4. 摘要精读
5. Figure逐图精读与逻辑串联
6. 核心方法学精读
7. 方法学批判
8. 讨论导读
9. 课堂讨论题

### Figure区块最小结构

- 原文图注（英文）
- 中文翻译（完整参数）
- logic-box（为什么接着做）
- quote-box（Results原文提取）
- steps-box（怎么做）
- results-box（核心发现+panel-details+阶段性结论）

## B. 文献计量模板（强制基准）

- 基准文件：`templates/bibliometric-network-template.html`
- 来源：`王秀丽_文献方法领域网络.html`
- 要求：后续生成文献计量仪表盘时，以该模板的布局与图表组件为标准。

### 文献计量最小组件

1. 三部网络图（paper-method-domain）
2. Sankey（method->domain）
3. 方法×年份热图
4. 领域×年份热图
5. 年度趋势图
6. 主题图（thematic map）
7. Treemap
8. 年度演化滑条（默认按年非累计）

## C. 模板使用规则

- 优先从模板复制结构，再替换数据内容。
- 不得删减关键区块，只能在不破坏结构的前提下增强文本。
- 若样式冲突，以模板样式变量为准。
