# Literature Source Setup (OpenAlex default)

## Required at session start

在开始任何论文讲义生成前，先提示并检查：

1. OpenAlex 是否可用（默认主数据源）
2. PubMed 是否可用（医学文献推荐启用）
3. paper-distill MCP 是否已连接

## Environment variables

最小配置（推荐）：

```bash
OPENALEX_EMAIL=your-email@example.com
```

医学场景增强（可选）：

```bash
NCBI_EMAIL=your-email@example.com
NCBI_API_KEY=your-ncbi-api-key
```

MCP 运行目录（已在 OpenCode MCP 配置中设置）：

```bash
PAPER_DISTILL_DATA_DIR=C:/Users/Lenovo/.paper-distill
```

## OpenCode MCP quick check

```bash
opencode mcp list
```

期望看到 `paper-distill` 为 `connected`。

## Source priority policy

默认检索顺序：

1. OpenAlex（主源）
2. PubMed（医学交叉验证）
3. 其他源（仅补充）

讲义中元数据以 DOI/PMID/PMCID 可核验记录为准，避免标题近似匹配误选。
