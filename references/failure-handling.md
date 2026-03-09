# Failure Handling: Access-Restricted Literature

## Trigger Conditions
满足任一即判定为受限：
- HTTP 401/403
- 返回页面包含 `login`, `subscribe`, `access denied`, `institutional access`
- 内容异常短且非摘要页面

## User Prompt (standard)

> 检测到该文献需要认证访问。请你手动下载 PDF 后放入：`./inputs/papers/`。
> 建议命名：`PMID_<id>.pdf` 或 `DOI_<doi>.pdf`。
> 提供文件后可继续生成完整讲义。

## Fallback Modes

1. **Full Mode**（有全文）
   - 正常生成完整讲义

2. **Partial Mode**（仅摘要/元数据）
   - 生成讲义骨架
   - Figure/Results 标注“待补全文证据”

3. **Resume Mode**（用户补交PDF后）
   - 自动补全Figure深度解读和方法学细节

## Must-not
- 不允许伪造 Results 原文引用
- 不允许把受限内容当作已验证事实输出
