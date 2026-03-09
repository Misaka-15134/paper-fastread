# Workflow: Single-Paper Lecture HTML

## Goal
从单篇论文生成可投屏、可教学复用的完整讲义 HTML（9章节）。

## Step-by-step

1. **输入解析**
   - 接收：`PMID` / `DOI` / `URL` / 本地 `PDF`
   - 标准化为 paper metadata（标题、期刊、年份、作者、DOI/PMID）

2. **可访问性检测**
   - 若全文可访问：进入 Full Mode
   - 若受限：走 `failure-handling.md` 回退流程

3. **内容抽取**
   - 抽取：Abstract / Intro / Results / Methods / Discussion / Figure captions
   - Figure caption必须保留原文完整句子

4. **讲义骨架生成（9章节）**
   - 按 `template.md` 生成完整章节骨架

5. **Figure深度填充（强制）**
    - caption-box：英文原文+完整中文翻译
    - logic-box：承上启下逻辑链（为什么接着做这张图）
    - quote-box：Results连续原文（3-5句）
    - steps-box：实验步骤
    - results-box：核心发现+panel-details+阶段小结

6. **质量检查（硬门槛）**
   - 图注中文是否完整覆盖 `n/P/bar/剂量/时间点`
   - Elsevier 图是否优先使用 `grX`
   - 术语和统计口径统一

7. **输出**
   - `讲义_<主题>_<PMID>.html`

## Definition of Done

- 9章节齐全
- 每个 Figure 含完整结构
- 所有图注翻译参数完整
- HTML 可直接在浏览器打开并放大图片
