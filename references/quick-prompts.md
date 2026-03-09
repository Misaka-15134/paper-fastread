# 快速调用提示词

## Prompt 0：先做文献源配置检查（必须）

```text
开始前先检查文献来源配置：
- 默认主源：OpenAlex（确认 OPENALEX_EMAIL）
- 医学交叉验证：PubMed（确认 NCBI_EMAIL / NCBI_API_KEY，如可用）
- MCP：确认 paper-distill 已连接（opencode mcp list）

若未配置，先给出配置步骤，再开始论文处理。
```

## Prompt 1：单篇快速讲义（模板锚定）

```text
请基于 templates/lecture-template.html 生成这篇论文的完整讲义HTML：
- 必须保留模板主结构（9章节 + Figure完整结构）
- Figure必须包含：logic-box + caption-box + quote-box + steps-box + results-box(panel-details)
- 图注中文翻译必须完整包含 n值、P值、比例尺、剂量、时间点
- 默认先用 OpenAlex 获取元数据，再用 PubMed（医学场景）交叉核验

论文来源：{PDF/HTML/URL/PMID/DOI}
输出文件名：讲义_<主题>_<PMID>.html
```

## Prompt 2：已有讲义深度补齐（不改风格）

```text
请在现有讲义HTML上按模板规范补齐内容：
- 不改页面风格
- 只增强 Figure 结果解读深度
- 补齐图注翻译技术参数（n/P/bar/剂量/时间点）
- 保持模板区块完整
```

## Prompt 3：图注完整性专项修复

```text
逐图检查中文翻译是否完整覆盖英文图注，修复所有缺失项：
- 面板标签(a)(b)(c)...
- n值 / P值 / 比例尺 / 剂量 / 时间点
不改英文图注，不改图片链接。
```

## Prompt 4：研究者文献计量仪表盘（模板锚定）

```text
请基于 templates/bibliometric-network-template.html 生成文献计量HTML：
- 输入CSV：{path_to_csv}
- 保留模板布局与图表组合
- 默认年度演化按年显示（非累计）
- 输出：{name}_network.html + nodes/edges/centrality.csv

数据策略：PubMed CSV + Google Scholar补充（如可用）
```

## Prompt 5：认证失败回退流程

```text
先检测文献可访问性：
- 可访问：继续完整生成
- 不可访问：提示用户手动下载PDF到 ./inputs/papers/
  命名建议：PMID_<id>.pdf 或 DOI_<doi>.pdf
- 未提供全文时：仅输出讲义骨架并标注待补证据
```

## Prompt 6：批量讲义生产（多篇）

```text
按模板批量生成讲义HTML：
- 统一基于 templates/lecture-template.html
- 每篇输出一个HTML
- 生成总索引页
- 标记每篇状态（full/partial）

输入清单：{pmid_or_doi_list}
```
