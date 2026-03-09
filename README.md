# paper-fastread

`paper-fastread` 是一个面向**文献推送后深度解读**场景的技能仓库。它的目标不是重复“给链接”，而是把每日推送论文进一步转化为：

- 可讲授的 9 章节中文讲义（HTML）
- 结构化 Figure 逐图精读（逻辑链条 + Results 原文 + 参数保真）
- 方法学深挖与批判性讨论
- 可分享的 PDF 导出

它集成了 `paper-distill-mcp` 工作流：在 OpenAlex/PubMed 等来源完成检索后，继续做中文翻译、图像提取与总结，帮助使用者快速抓住研究逻辑并开展批判性思考。

---

## ✨ 核心价值（相对于“只推文献链接”）

1. **从“发现论文”到“理解论文”**：把检索结果直接转成课堂级讲义。
2. **从“摘要概览”到“结果证据”**：强制提取 Results 连续原文并推导结论。
3. **从“看图”到“讲图”**：Figure 强制模块化，明确承上启下逻辑。
4. **从“个人阅读”到“团队传播”**：一键 HTML → PDF，便于群组分发与归档。

---

## 🔧 主要能力

- 固定 9 章节输出结构（教学模板化）
- Figure 强制结构：`logic-box → caption-box → quote-box → steps-box → results-box`
- 默认来源策略：**OpenAlex 优先**，医学论文追加 PubMed 交叉验证
- 集成 `paper-distill-mcp`（检索、元数据、图像链接定位）
- HTML 转 PDF：`tools/html_to_pdf.sh`

---

## 🚀 快速开始（通用版）

> 下面分为“通用基础步骤”+“不同客户端接入方式”。

### A. 通用基础步骤

1) 安装 MCP 工具：

```bash
uv tool install paper-distill-mcp
```

2) 配置文献源环境变量（推荐）：

```bash
OPENALEX_EMAIL=your-email@example.com
NCBI_EMAIL=your-email@example.com
NCBI_API_KEY=your-ncbi-api-key
```

3) 准备本仓库（技能内容）：

```bash
git clone https://github.com/Misaka-15134/paper-fastread.git
cd paper-fastread
```

### B. 客户端接入

#### OpenCode

在 `opencode.json` 增加 MCP：

```json
{
  "mcp": {
    "paper-distill": {
      "type": "local",
      "command": ["uvx", "paper-distill-mcp"],
      "environment": {
        "PAPER_DISTILL_DATA_DIR": "C:/Users/Lenovo/.paper-distill"
      }
    }
  }
}
```

检查：

```bash
opencode mcp list
```

#### Claude Code

```bash
claude mcp add paper-distill -- uvx paper-distill-mcp
```

或在项目 `.mcp.json`：

```json
{
  "mcpServers": {
    "paper-distill": {
      "command": "uvx",
      "args": ["paper-distill-mcp"]
    }
  }
}
```

#### OpenClaw

```bash
mcporter config add paper-distill --command uvx --scope home -- paper-distill-mcp
mcporter list
```

#### Qoder（及其他支持 MCP 的客户端）

使用与 Claude Code 类似的 MCP 配置模板：

```json
{
  "mcpServers": {
    "paper-distill": {
      "command": "uvx",
      "args": ["paper-distill-mcp"]
    }
  }
}
```

> 如果客户端配置路径不同，只需将同一段 `mcpServers.paper-distill` 写入其 MCP 配置文件即可。

---

## 🤖 给其他 Agent 的“自安装引导 Prompt”（可直接复制）

```text
请把 paper-fastread 安装到当前客户端的技能目录，并接入 paper-distill-mcp。

要求：
1) 安装 MCP：uv tool install paper-distill-mcp
2) 在当前客户端 MCP 配置中注册：command=uvx, args=[paper-distill-mcp]
3) 检查连接状态（如 opencode mcp list / mcporter list / 客户端自带 MCP 状态页）
4) 读取仓库中的 SKILL.md 与 references/literature-source-setup.md
5) 开始任务前先提示我确认 OPENALEX_EMAIL、NCBI_EMAIL、NCBI_API_KEY
6) 以 paper-fastread 的 9章节模板生成讲义 HTML，并导出 PDF
```

---

## 🧪 使用示例（Prompt + 结果）

### 示例 Prompt

```text
请用 paper-fastread 处理这篇论文：
Blood metabolites mediate causal inference studies on the effect of gut microbiota on the risk of vascular calcification

要求：
1) 先检查文献源配置（OpenAlex 默认 + PubMed 交叉）
2) 输出9章节中文讲义HTML
3) Figure必须使用 logic/caption/quote/steps/results 五大模块
4) 导出同名PDF
5) 生成2张截图：讲义总览 + Figure精读模块
```

### 示例输出结果（仓库内）

- HTML：`examples/Blood_metabolites_VC_PMID40139524_lecture_demo.html`
- PDF：`examples/Blood_metabolites_VC_PMID40139524_lecture_demo.pdf`
- 截图：
  - `assets/screenshots/demo-overview.png`
  - `assets/screenshots/demo-figure-module.png`

---

## 🖼️ 展示截图

### 讲义总览

![Lecture overview](assets/screenshots/demo-overview.png)

### Figure 精读模块（logic/caption/quote/steps/results）

![Figure module](assets/screenshots/2026-03-09_114856.png)

---

## 📤 HTML → PDF 导出

```bash
bash tools/html_to_pdf.sh examples/Blood_metabolites_VC_PMID40139524_lecture_demo.html
```

指定输出路径：

```bash
bash tools/html_to_pdf.sh examples/Blood_metabolites_VC_PMID40139524_lecture_demo.html outputs/demo.pdf
```

详见：`references/html-to-pdf.md`

---

## 📁 仓库结构

```text
paper-fastread/
├── SKILL.md
├── README.md
├── references/
├── templates/
├── tools/
├── examples/
└── assets/screenshots/
```

---

## 📚 关键文档

- 技能入口：`SKILL.md`
- 文献源配置：`references/literature-source-setup.md`
- MCP 搜索与取图流程：`references/paper-distill-mcp-workflow.md`
- 单篇讲义规范：`references/single-paper-lecture-template-zh.md`
- 快速 prompts：`references/quick-prompts.md`
- PDF 导出：`references/html-to-pdf.md`
- 发布清单：`GITHUB_RELEASE_CHECKLIST.md`
