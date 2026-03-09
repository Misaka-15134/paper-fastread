# GitHub 发布清单（paper-fastread）

## 1) 结构与规范

- [ ] 保留技能核心结构：`SKILL.md`, `references/`, `templates/`, `tools/`, `assets/`
- [ ] `SKILL.md` frontmatter 仅含 `name` 与 `description`
- [ ] `SKILL.md` 包含会话起始提示（文献源配置检查）
- [ ] `references/` 中包含：
  - [ ] `single-paper-lecture-template-zh.md`
  - [ ] `literature-source-setup.md`
  - [ ] `paper-distill-mcp-workflow.md`
  - [ ] `checklists/release-checklist.md`

## 2) MCP 与来源策略

- [ ] 默认来源策略明确：OpenAlex 优先，PubMed 医学交叉验证
- [ ] `paper-distill-mcp` 安装与连接步骤在 README 可见
- [ ] 示例命令可直接复制执行（`uv tool install`, `opencode mcp list`）

## 3) 展示与文档

- [ ] `README.md` 包含用途、快速开始、仓库结构
- [ ] README 截图链接有效：
  - [ ] `assets/screenshots/demo-overview.png`
  - [ ] `assets/screenshots/demo-figure-module.png`
- [ ] 示例 HTML 存在于 `examples/`

## 4) 仓库卫生

- [ ] 不提交敏感信息（API Key、PAT、私有 token）
- [ ] 不提交临时文件/系统伪文件（如 `nul`）
- [ ] 可选：`dist/*.skill` 仅在发布产物需要时提交

## 5) 发布动作

- [ ] 本地 `git status` 检查通过
- [ ] 首次发布：初始化仓库并关联远程
- [ ] 提交信息清晰反映“why”
- [ ] 推送到 `Misaka-15134/paper-fastread`
