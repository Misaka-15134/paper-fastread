# 讲义质量对比指南

## 目的

本文档通过对比`讲义2`（高质量范例）与常见不足案例，帮助理解skill的输出标准。

---

## 对比维度

### 1. 实验目的（purpose-box）

#### ✅ 高质量示例（讲义2 Figure 1）

```html
<div class="purpose-box">
  <h4>实验目的：</h4>
  <p>Figure 1先定义模型是否成立，并给出后续多组学的必要前提：如果仅看HE形态，
  无法判断保护来自<span class="highlight">蛋白执行层（proteomics）</span>还是
  <span class="highlight">脂质终末层（lipidomics）</span>。因此这一步先确认8周UV暴露后
  损伤存在、n-3 PUFA干预后损伤减轻，再进入组学机制分解。</p>
</div>
```

**特点**：
- 长度：120字
- 说明了实验在整体机制中的位置
- 解释了为什么需要这个实验
- 与后续Figure的逻辑关系清晰

#### ❌ 不合格示例

```html
<div class="purpose-box">
  <h4>实验目的：</h4>
  <p>验证模型是否成功建立。</p>
</div>
```

**问题**：
- 长度：仅12字
- 未说明实验在机制中的位置
- 未解释为什么需要这个实验
- 缺少与其他Figure的关系

---

### 2. 实验步骤（steps-box）

#### ✅ 高质量示例（讲义2 Figure 1）

```html
<div class="steps-box">
  <h4>实验步骤：</h4>
  <ol>
    <li>建立四组模型：UF、UC、NF、NC，并进行持续8周UV暴露流程（UV组）。</li>
    <li>在UV背景下比较是否补充n-3 PUFA（UF vs UC），在非UV背景下比较基础差异（NF vs NC）。</li>
    <li>采集皮肤组织做HE染色（200x），按A-D面板展示四组形态。</li>
    <li>将组织学终点与后续LC-MS/MS蛋白质组和脂质组结果联动解释。</li>
  </ol>
</div>
```

**特点**：
- 步骤数：4步
- 每步包含具体操作和参数
- 包含分组信息、技术细节、分辨率
- 说明了数据如何与后续分析联动

#### ❌ 不合格示例

```html
<div class="steps-box">
  <h4>实验步骤：</h4>
  <ol>
    <li>建立模型</li>
    <li>HE染色</li>
  </ol>
</div>
```

**问题**：
- 步骤数：仅2步
- 缺少具体参数（分组、n值、分辨率）
- 未说明对照设置
- 未说明数据如何使用

---

### 3. 结果描述（results-box）

#### ✅ 高质量示例（讲义2 Figure 1）

```html
<div class="results-box">
  <h4>结果描述：</h4>
  <p><strong>核心发现：</strong>8周UV后，UC出现典型光老化组织损伤；UF损伤程度减轻，
  提示n-3 PUFA具有结构保护效应，但仅靠形态学还不能解释其分子机制。</p>
  
  <div class="panel-details">
    <p>Panel A-B（UV背景）</p>
    <ul>
      <li>A为UF，B为UC；二者直接回答n-3 PUFA在UV下是否有效。</li>
      <li>UF较UC表皮增生和结构紊乱更轻，提示干预方向正确。</li>
    </ul>
    <p>Panel C-D（非UV背景）</p>
    <ul>
      <li>C为NF，D为NC；用于区分"营养补充本底效应"与"抗UV效应"。</li>
      <li>该对照框架保证后续UF vs UC、UC vs NC等组学比较具有生物学解释力。</li>
    </ul>
  </div>
</div>
```

**特点**：
- 核心发现：简洁明确（1-2句）
- Panel解读：每个Panel 2条bullet points
- 逻辑清晰：说明了Panel间的对照关系
- 机制意义：与后续Figure的联系

#### ❌ 不合格示例

```html
<div class="results-box">
  <h4>结果描述：</h4>
  <p><strong>核心发现：</strong>UV导致损伤，n-3 PUFA有保护作用。</p>
  
  <div class="panel-details">
    <p>Panel A-D</p>
    <ul>
      <li>显示四组的HE染色结果。</li>
    </ul>
  </div>
</div>
```

**问题**：
- 核心发现：过于简化，缺少具体观察
- Panel解读：未逐面板拆解
- 每个Panel只有1条或合并描述
- 缺少对照逻辑说明
- 缺少机制意义

---

### 4. 中文翻译完整性

#### ✅ 高质量示例（讲义3 Figure 1）

```html
<div class="caption-box">
  <p><strong>原文图注：</strong>Figure 1. Piezo1 expression was upregulated in KFbs and 
  contributed to collagen fibrosis. (a) Piezo1 immunohistochemical imaging of keloid and 
  normal skin samples (n = 4 donors, bar = 100 um). (b) Western blotting analysis of Piezo1 
  obtained from KFbs and Fbs from keloids and matched normal skin dermis samples. The predicted 
  mass of 287 kDa is indicated. It is probed with an anti-NaK ATPase antibody as a membrane 
  protein-loading control (n = 4 donors, ***P &lt; .001 Fbs vs KFbs). ...</p>
  
  <p><strong>中文翻译：</strong>Figure 1. Piezo1在KFbs中表达上调并促进胶原纤维化。
  (a) 瘢痕疙瘩和正常皮肤样本的Piezo1免疫组化成像（n = 4供体，bar = 100 um）。
  (b) 对来自瘢痕疙瘩及匹配正常皮肤真皮样本的KFbs和Fbs进行Piezo1的Western blot分析。
  图中标示预测分子量287 kDa。采用抗NaK ATPase抗体作为膜蛋白上样对照
  （n = 4供体，***P &lt; .001，Fbs vs KFbs）。...</p>
</div>
```

**特点**：
- 逐面板翻译：(a), (b), (c)...
- 包含所有n值：n = 4 donors
- 包含所有P值：***P < .001
- 包含所有比例尺：bar = 100 um
- 包含技术细节：287 kDa, NaK ATPase抗体

#### ❌ 不合格示例

```html
<div class="caption-box">
  <p><strong>原文图注：</strong>Figure 1. Piezo1 expression was upregulated in KFbs...</p>
  
  <p><strong>中文翻译：</strong>Figure 1显示Piezo1在KFbs中上调并促进纤维化。
  a为IHC；b为Western blot；c为免疫荧光；d-e为迁移和增殖实验；f为胶原蛋白检测。</p>
</div>
```

**问题**：
- 未逐面板翻译
- 缺少所有n值
- 缺少所有P值
- 缺少所有比例尺
- 缺少技术细节（分子量、抗体、统计方法）

---

## 质量检查清单

生成讲义后，使用以下清单逐项检查：

### Figure解读完整性

- [ ] 每个Figure包含4个box：caption-box, purpose-box, steps-box, results-box
- [ ] purpose-box长度至少80-120字
- [ ] steps-box至少4-6步
- [ ] results-box包含panel-details
- [ ] 每个Panel至少2-3条bullet points

### 定量信息完整性

- [ ] 所有图注包含n值
- [ ] 所有图注包含P值标记（*P<.05, **P<.01, ***P<.001）
- [ ] 所有图注包含比例尺（bar = X um）
- [ ] 所有图注包含技术参数（浓度、时间、分子量等）

### 内容深度

- [ ] 实验目的说明了实验在机制中的位置
- [ ] 实验步骤包含具体操作和参数
- [ ] Panel解读包含观察、对照、统计、技术细节
- [ ] 机制意义段落100-150字

### 格式规范

- [ ] 图片URL使用gr格式（Elsevier期刊）
- [ ] CSS样式完整（purpose-box橙色、steps-box紫色、results-box绿色）
- [ ] HTML结构与模板一致

---

## 修复流程

如果生成的讲义不符合标准，按以下流程修复：

### 1. 对比模板

将生成的讲义与`讲义2_多组学光老化_PMID34241612.html`对比：
- 打开两个文件
- 找到同一类型的Figure（如Figure 1）
- 逐box对比内容长度和深度

### 2. 识别不足

使用本文档的"对比维度"部分，识别具体不足：
- 实验目的是否过于简化？
- 实验步骤是否缺少参数？
- Panel解读是否不够详细？
- 中文翻译是否缺少技术参数？

### 3. 补充内容

根据识别的不足，补充内容：
- 回到原文Results部分，提取更多细节
- 回到原文图注，逐字翻译所有技术参数
- 展开实验步骤，补充n值、对照、统计方法
- 逐Panel拆解，每个Panel至少2-3条

### 4. 验证修复

修复后，再次使用质量检查清单验证：
- 所有检查项是否通过？
- 与讲义2的格式和丰富度是否对齐？

---

## 常见问题

### Q1: 为什么讲义2的Figure解读这么详细？

**A**: 讲义2是教学用途，需要：
1. 帮助学生理解实验设计逻辑
2. 训练学生阅读图注的能力
3. 展示如何从图中提取定量信息
4. 说明实验在整体机制中的位置

简化的描述无法达到这些教学目标。

### Q2: 如何判断"实验目的"是否足够详细？

**A**: 检查是否回答了以下问题：
1. 为什么要做这个实验？
2. 这个实验在整体机制中的位置？
3. 与前后Figure的逻辑关系？
4. 要回答什么科学问题？

如果只回答了第1个问题，说明不够详细。

### Q3: 如何判断"Panel解读"是否足够详细？

**A**: 检查每个Panel是否包含：
1. 观察到什么（具体数值、倍数变化）
2. 对照组表现（基线、差异）
3. 统计显著性（P值、n值）
4. 技术细节（比例尺、方法）

如果只有1条bullet point，说明不够详细。

### Q4: 中文翻译必须逐字翻译吗？

**A**: 是的。图注中的所有技术参数都有教学价值：
- n值：样本量，影响统计功效
- P值：显著性，判断结果可靠性
- 比例尺：空间分辨率，理解图像尺度
- 浓度/剂量：实验条件，可重复性关键

省略任何一个都会降低讲义的教学价值。

---

## 总结

高质量讲义的核心是**内容丰富度**，而非仅仅是HTML结构正确。

**记住**：
- 实验目的：80-120字，说明机制位置
- 实验步骤：4-6步，包含所有参数
- Panel解读：每个Panel 2-3条，包含定量信息
- 中文翻译：逐字翻译，不遗漏任何技术参数

**参考标准**：`讲义2_多组学光老化_PMID34241612.html`

**验证方法**：使用本文档的质量检查清单
