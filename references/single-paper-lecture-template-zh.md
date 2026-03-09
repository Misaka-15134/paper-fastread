# Single Paper -> Lecture Template (ZH)

目标：把一篇论文快速整理为统一9章节讲义，优先保证“细节饱满、逻辑清晰、可讲、可复用”。

## 固定输出结构（必须严格遵循）

1. 论文概览卡片（标题/期刊/PMID/DOI/作者/核心命题）
2. 研究逻辑与故事主线（问题-假设-逐步验证-结论）
3. 引言导读（2-3段原文英文 + 中文解读）
4. 摘要精读（逐句拆解）
5. Figure逐图精读与逻辑串联（逻辑承接 + Results原文 + 实验步骤 + 小结）
6. 核心方法学精读（提取Methods关键原文并深度解析）
7. 方法学批判（样本量、统计、验证深度、转化gap）
8. 讨论导读（关键原文段 + 中文解读）
9. 课堂讨论题（3-5题，需有启发性）

## Figure 完整结构（强制）

```html
<div class="figure-section">
  <h3>Figure X: [图表主旨标题]</h3>

  <div class="logic-box">
    <h4>🔗 研究逻辑链条：</h4>
    <p><strong>承上启下：</strong>[上一部分结论 -> 未解问题 -> 本图实验设计的必要性]</p>
  </div>

  <img src="[正确URL]" class="fig-img" onclick="openModal(this.src)" alt="Figure X" />

  <div class="caption-box">
    <p><strong>原文图注：</strong>[完整英文图注，逐字复制]</p>
    <p><strong>中文翻译：</strong>[完整中文翻译，必须包含 n值、P值、fold change、比例尺等定量信息]</p>
  </div>

  <div class="quote-box">
    <h4>📝 Results 原文精读：</h4>
    <p><strong>相关原文提取：</strong><em>"[Results章节连续3-5句关键英文原文]"</em></p>
    <p><strong>数据推导解读：</strong>[从原文与图表数据推导结论，写清倍数、时间、空间分布特征]</p>
  </div>

  <div class="steps-box">
    <h4>🔬 实验细节拆解：</h4>
    <ol>
      <li><strong>样本准备与分组：</strong>[材料、n值、分组]</li>
      <li><strong>处理条件：</strong>[剂量、时间点、介质]</li>
      <li><strong>检测指标：</strong>[技术与抗体/探针]</li>
    </ol>
  </div>

  <div class="results-box">
    <h4>📊 结果梳理与小结：</h4>
    <div class="panel-details">
      <p>Panel A-B（[子图功能]）：[具体结果 + 显著性]</p>
      <p>Panel C-D（[子图功能]）：[具体结果 + 倍数变化]</p>
    </div>
    <p><strong>本节阶段性结论：</strong>[1-2句总结，作为下一张图铺垫]</p>
  </div>
</div>
```

## 核心方法学精读规范（Methods Deep Dive）

第6章绝不能只罗列常规参数，必须挑选最核心/最创新的1-2个方法并完成：

1. 方法学原文摘录：提取Methods描述该技术的完整英文段落。
2. 细节与参数深挖：解释为何选择该模型/参数（例如时间窗、对照策略、阈值设置）。
3. 严谨性分析：双盲、多中心、数据清洗cut-off、复现性与偏倚控制。
4. 优势与局限：方法在该领域的优势与潜在技术盲区。

## 中文翻译与参数提取底线

- 禁止“概括式翻译”替代参数。
- 中文必须1:1保留英文中的定量信息：`n=`、`P<`、`fold`、`scale bar`、剂量、时间点。
- Results解读必须引用正文原文，不可仅靠图注或摘要推断。

## 图片URL规范（Elsevier）

- 正确格式：`https://ars.els-cdn.com/content/image/1-s2.0-{PII}-{figureid}.jpg`
- 正文主图优先：`gr1, gr2, ...`
- 避免补图ID：`fx1, fx2, ...`
- PII从DOI/原文链接提取，去掉标点后按实际文章校验。

## 必需CSS样式补充

```css
/* 逻辑承接块 */
.logic-box {
  border-left: 4px solid #0891b2;
  background: #ecfeff;
  padding: 12px 16px;
  border-radius: 8px;
  margin: 10px 0 20px 0;
}
.logic-box h4 { color: #0891b2; margin-top: 0; margin-bottom: 8px; font-size: 16px; }

/* 原文精读块 */
.quote-box {
  border-left: 4px solid #3b82f6;
  background: #eff6ff;
  padding: 16px 20px;
  border-radius: 8px;
  margin: 16px 0;
}
.quote-box h4 { color: #1d4ed8; margin-top: 0; margin-bottom: 10px; font-size: 16px; }
.quote-box p { margin: 8px 0; }
```

## 质量门槛与验收标准

- [ ] 逻辑连贯性：每个Figure都有`.logic-box`且解释“图A后为何做图B”。
- [ ] 原文还原度：每个Figure在`.quote-box`中有Results连续3句及以上英文原文。
- [ ] 参数完整度：图注翻译完整包含`n=`、`P<`、`fold change`、`scale bar`。
- [ ] 方法学深度：第6章含Methods原文段落并解释“为何这样设计实验”。
- [ ] 图文对应：Elsevier链接优先`gr`格式，避免补图或缩略图。

人格锚定：以“苛刻的顶刊审稿人 + 优秀生信讲师”标准输出，强调逻辑链条与Results原文推导。
