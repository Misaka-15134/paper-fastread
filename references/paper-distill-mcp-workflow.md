# paper-distill-mcp Workflow for paper-fastread

## Goal

使用 paper-distill MCP 完成两件事：

1. 文献搜索与候选筛选（默认 OpenAlex）
2. 获取可用于讲义的主图链接（优先正文主图）

## Step 1: search papers (default OpenAlex-first)

- 用论文题目、关键词或作者调用 MCP 检索。
- 先锁定 DOI，再补充 PMID/PMCID（若有）。
- 医学论文追加 PubMed 交叉验证，确认题目、年份、作者一致。

推荐保留字段：

- title
- journal
- year
- doi
- pmid / pmcid
- abstract

## Step 2: choose canonical source

优先顺序：

1. DOI 官方页面
2. PMC（若开放获取）
3. 出版社正文页面

避免仅依赖聚合站二手信息。

## Step 3: get figure URLs for lecture

### If paper has PMCID

- 优先使用 PMC 的 `gr` 主图资源。

示例（PMCID=PMC12766209）：

- `https://cdn.ncbi.nlm.nih.gov/pmc/blobs/.../gr1.jpg`
- `https://cdn.ncbi.nlm.nih.gov/pmc/blobs/.../gr2.jpg`

### If Elsevier paper

- 使用主图格式：

`https://ars.els-cdn.com/content/image/1-s2.0-{PII}-gr1.jpg`

- 避免 `fx`（通常是补图）除非明确需要补充材料。

## Step 4: map figures to lecture blocks

每个 Figure 至少填充：

- `logic-box`：承上启下逻辑
- `caption-box`：完整英文图注 + 中文翻译（保留 n/P/fold/scale）
- `quote-box`：Results 连续 3-5 句原文
- `steps-box`：样本、处理、检测
- `results-box`：panel 级结果 + 小结

## Step 5: quality gate

交付前检查：

- DOI/PMID/PMCID 一致
- 主图 URL 可访问且与图号一致
- 图注翻译包含关键参数
- Results 引文不是摘要替代
