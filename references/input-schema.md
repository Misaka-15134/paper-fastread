# Input Schema

## A. Single-paper lecture

支持输入：
- `pmid` (string)
- `doi` (string)
- `url` (string)
- `pdf_path` (string, 本地绝对路径)

至少一个必填：`pmid|doi|url|pdf_path`

建议同时提供：
- `title`（可选）
- `author_focus`（可选）
- `language`（默认 zh-CN）

## B. Bibliometric dashboard

CSV 必填列：
- `year`
- `pmid`
- `doi`
- `journal`
- `title`

推荐列：
- `pubmed_url`
- `authors`
- `keywords`

## Validation Rules
- `year` 为 4 位数字
- `pmid` 或 `doi` 至少其一非空
- 同一篇文献去重键优先：`pmid` > `doi` > `title+year`
