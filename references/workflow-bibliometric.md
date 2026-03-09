# Workflow: Researcher Bibliometric Dashboard

## Goal
生成研究者文献计量 HTML 仪表盘，支持网络关系与年度演化可视化。

## Data Strategy (默认)
- 主数据源：**PubMed CSV**
- 补充数据源：**Google Scholar**（用于补充元数据/引用信息，若可用）

## Required Input
- CSV 最小字段：`year,pmid,doi,journal,title`
- 推荐字段：`pubmed_url,keywords,authors`

## Step-by-step

1. **读入与清洗**
   - 校验年份、去重（pmid/doi）

2. **方法学/领域标签映射**
   - 通过规则表或关键词映射到 method/domain

3. **图结构构建**
   - 节点：paper/method/domain
   - 边：paper-method / paper-domain / method-domain

4. **核心可视化生成**
   - 三部网络图（vis-network）
   - Sankey（method->domain）
   - 方法×年份热图
   - 领域×年份热图
   - 年度趋势曲线
   - Thematic map
   - Treemap

5. **年度演化模式**
   - 默认：按年显示（`year === y`）
   - 非累计，除非用户明确要求累计

6. **输出与导出**
   - `*_network.html`
   - `*_nodes.csv`, `*_edges.csv`, `*_centrality.csv`

## Validation
- 频次统计一致（图表与CSV一致）
- 年度演化逻辑正确（非累计）
- HTML可打开且交互正常
