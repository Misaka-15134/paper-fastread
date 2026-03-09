# 论文讲义制作最佳实践

> ⚠️ 规范优先级说明
>
> 本文档包含历史版本实践（含 `purpose-box` 写法）。当前执行请以 `SKILL.md` 与 `single-paper-lecture-template-zh.md` 为最高优先级：
> `logic-box → image → caption-box → quote-box → steps-box → results-box`。
>
> 使用旧片段时，请将 `purpose-box` 迁移为 `logic-box`，并补齐 `quote-box`（Results 连续原文）。

本文档总结了从实际教学讲义制作中积累的经验教训和最佳实践。

---

## 1. 中文图注翻译最佳实践

### 问题背景

在讲义2-4的初版中，发现28个caption-box中有13个存在不完整翻译问题，主要表现为：
- 缺少样本量（n值）
- 缺少统计显著性标记（*P<0.05等）
- 缺少比例尺信息（bar = X μm）
- 缺少详细方法学描述

### 解决方案

#### 完整翻译模板

```
中文翻译：Figure X. [总体描述]。
(a) [面板A描述]（n = X供体/样本，bar = X μm）。
(b) [面板B描述]。[方法学细节]（n = X，***P < .001，对照组 vs 实验组）。
(c) [面板C描述]（n = X，*P < .05和***P < .001，bar = X μm）。
...
```

#### 必须包含的技术参数

| 参数类型 | 示例 | 说明 |
|---------|------|------|
| 样本量 | n = 4 donors, n = 5 samples | 每个实验的样本数 |
| 统计显著性 | *P < .05, **P < .01, ***P < .001 | 与原文星号对应 |
| 比例尺 | bar = 50 μm, Bars = 200 μm | 显微镜图片必需 |
| 浓度 | 5 μM, 10 μM | 药物/试剂浓度 |
| 剂量 | 10^7 CFU, 20 μL | 细菌量、体积 |
| 能量密度 | 5/10/20 J/cm² | 光疗参数 |
| 时间点 | 24h, 7d, POD 21 | 实验时间节点 |
| 方法学 | Western blot, IHC, qPCR | 技术名称 |
| 数据表示 | mean ± SD, mean ± SEM | 统计表示方式 |

#### 翻译对比示例

**❌ 错误（简化版，约100字）：**
> Figure 1显示Piezo1在瘢痕来源成纤维细胞（KFbs）中上调并促进胶原纤维化。a为组织IHC；b为Piezo1蛋白检测；c为siPIEZO干预后免疫荧光；d-e显示敲低PIEZO1抑制迁移与增殖；f显示COL1A1/COL3A1等胶原相关蛋白变化及I/III比值分析。

**✅ 正确（完整版，约350字）：**
> Figure 1. Piezo1在KFbs中表达上调并促进胶原纤维化。(a) 瘢痕疙瘩和正常皮肤样本的Piezo1免疫组化成像（n=4供体，bar=100 μm）。(b) 从瘢痕疙瘩和配对正常皮肤真皮样本中获得的KFbs和Fbs的Piezo1 Western blot分析。标示预测的287 kDa条带。使用抗NaK ATPase抗体作为膜蛋白上样对照（n=4供体，***P<.001 Fbs vs KFbs）。(c) siPIEZO#1和siPIEZO#3转染后Fbs和KFbs中Piezo1的免疫荧光显微镜图像（n=5供体，*P<.05和***P<.001，bar=50 μm）。(d, e) 划痕愈合实验和CCK-8显示PIEZO1敲低抑制Fbs和KFbs的细胞迁移（n=5供体，***P<.001，bar=200 μm）和细胞增殖（n=6供体，***P<.001）。(f) siPIEZO#1和siPIEZO#3转染后Fbs和KFbs中胶原相关蛋白（包括COL1A1和COL3A1）的Western blot分析。显示COL1A1/GAPDH、COL3A1/GAPDH和COL1A1/COL3A1的相对灰度值（n=5供体，*P<.05，**P<.01，***P<.001）。

**改进倍数**: 3.5倍

---

## 2. 图片URL规范最佳实践

### 问题背景

讲义3使用了错误的图片URL格式（fx而非gr），可能导致显示补充材料而非正文主图。

### Elsevier CDN图片格式

| 格式 | 用途 | 示例 | 使用建议 |
|------|------|------|---------|
| **gr** | 正文主图 | `-gr1.jpg`, `-gr2.jpg` | ✅ **优先使用** |
| **fx** | 扩展图/补充图 | `-fx1.jpg`, `-fx2.jpg` | ❌ 避免使用 |
| **ga** | 图形摘要 | `-ga1_lrg.jpg`, `-ga1.jpg` | ✅ 用于Graphical Abstract |

### URL构建规则

```
https://ars.els-cdn.com/content/image/1-s2.0-{PII}-{figureid}.jpg
```

**PII获取方法**：
1. 从DOI提取：`10.1016/j.jid.2025.03.039`
2. 从PubMed "Full text links" → Elsevier页面URL中获取
3. 格式：期刊ISSN（去掉连字符）+ 文章编号
   - 例：Journal ISSN `0022-202X` + 文章号 `25004154` = `S0022202X25004154`

### 验证方法

```bash
# 验证URL是否可访问
curl -I https://ars.els-cdn.com/content/image/1-s2.0-S0022202X25004154-gr1.jpg

# 应返回
HTTP/1.1 200 OK
Content-Type: image/jpeg
```

### 常见错误

| 错误 | 原因 | 修复 |
|------|------|------|
| 使用fx格式 | 误用补充材料URL | 改为gr格式 |
| PII错误 | 从错误来源复制 | 从官方DOI/PubMed验证 |
| 缺少ga1_lrg | 图形摘要用错格式 | 使用ga1_lrg或ga1 |

---

## 3. 详细结果解读最佳实践

### 问题背景

初版讲义的Figure描述只有1-2句话（40-70字），缺少：
- 实验步骤说明（做了什么）
- 方法学选择理由（为什么这么做）
- 具体数值和统计显著性
- 多面板间的逻辑关系

### 增强结构

每个Figure应包含以下完整结构：

#### 1. 实验目的（purpose-box）

```html
<div class="purpose-box">
  <h4>🎯 实验目的：</h4>
  <p>为什么要做这个实验？在整体机制中的位置？要回答什么科学问题？</p>
</div>
```

**示例**：
> 前面Figure 3已通过RNA-seq和多层验证确认ALA-PDT上调NR4A1。但**相关性不等于因果性**——NR4A1上调可能只是伴随现象，而非抑脂的功能中介。本实验通过功能获得/丧失（gain/loss-of-function）双向验证，明确NR4A1是否为ALA-PDT抑制脂质合成的**必要且充分**条件。

#### 2. 实验步骤（steps-box）

```html
<div class="steps-box">
  <h4>🔬 实验步骤：</h4>
  <ol>
    <li><strong>样本准备：</strong>[材料、细胞、组织，n=?]</li>
    <li><strong>处理条件：</strong>[如何分组，对照是什么]</li>
    <li><strong>检测方法：</strong>[用了什么技术，为什么选这个方法]</li>
    <li><strong>数据分析：</strong>[统计方法，阈值设定]</li>
  </ol>
</div>
```

**示例**：
> 1. **细胞模型构建**：使用永生化人皮脂腺细胞系XL-i-20，分别构建：
>    - Sh-NR4A1组：慢病毒介导的NR4A1敲低（loss-of-function）
>    - OE-NR4A1组：慢病毒介导的NR4A1过表达（gain-of-function）
>    - NC组：阴性对照（空载体）
> 2. **干预处理**：各组细胞分为"未处理"和"ALA-PDT处理"（5-ALA + 10 J/cm² 红光照射）两个亚组，处理后24小时收样。
> 3. **检测指标**：
>    - NR4A1验证：RT-qPCR（mRNA水平）+ Western blot（蛋白水平）
>    - 脂质负荷：BODIPY 493/503荧光染色定量细胞内中性脂质
>    - 脂质合成蛋白：Western blot检测SREBP1和FASN
> 4. **统计分析**：多组间比较使用单因素方差分析（ANOVA）+ Tukey事后检验，n≥3次独立重复。

#### 3. 详细结果解读（results-box增强版）

```html
<div class="results-box">
  <h4>📊 结果解读：</h4>
  
  <p><strong>核心发现：</strong>[保留原1-2句简洁版]</p>
  
  <div class="panel-details">
    <p>Panel A - [子图标题]：</p>
    <ul>
      <li><strong>观察到什么：</strong>[具体数值、p值、倍数变化]</li>
      <li><strong>对照组表现：</strong>[基线是什么]</li>
      <li><strong>统计显著性：</strong>[p<0.001等]</li>
    </ul>
    <!-- 其他Panel... -->
  </div>
  
  <p><strong>🔗 逻辑链条：</strong>[Panel A→B→C如何构建完整证据链]</p>
  <p><strong>💡 机制意义：</strong>[在整体机制中的位置、临床转化意义]</p>
</div>
```

### 字数对比

| 版本 | 平均字数 | 包含内容 |
|------|---------|---------|
| 原版 | 40-70字 | 仅结论概括 |
| 增强版 | 1000-1500字 | 目的+步骤+逐面板解读+逻辑+意义 |
| 增长率 | +150% ~ +300% | 教学价值显著提升 |

---

## 4. CSS样式规范

### 必需样式类

```css
/* 原文图注（蓝色边框） */
.caption-box {
  border-left: 4px solid #2563eb;
  background: #eff6ff;
  padding: 12px 16px;
  border-radius: 8px;
  margin: 10px 0;
}

/* 实验目的（橙色边框） */
.purpose-box {
  border-left: 4px solid #ea580c;
  background: #fff7ed;
  padding: 12px 16px;
  border-radius: 8px;
  margin: 10px 0;
}
.purpose-box h4 {
  margin: 0 0 8px 0;
  color: #ea580c;
  font-size: 16px;
}

/* 实验步骤（紫色边框） */
.steps-box {
  border-left: 4px solid #7c3aed;
  background: #f5f3ff;
  padding: 12px 16px;
  border-radius: 8px;
  margin: 10px 0;
}
.steps-box h4 {
  margin: 0 0 8px 0;
  color: #7c3aed;
  font-size: 16px;
}
.steps-box ol {
  margin: 8px 0;
  padding-left: 24px;
}
.steps-box li {
  margin: 6px 0;
  line-height: 1.6;
}

/* 结果解读（绿色边框） */
.results-box {
  border-left: 4px solid #059669;
  background: #ecfdf5;
  padding: 12px 16px;
  border-radius: 8px;
  margin: 10px 0;
}
.results-box h4 {
  margin: 0 0 8px 0;
  color: #059669;
  font-size: 16px;
}

/* 面板详解 */
.panel-details {
  margin: 12px 0;
  padding-left: 12px;
}
.panel-details > p {
  font-weight: 600;
  color: #334155;
  margin: 10px 0 4px 0;
}
.panel-details ul {
  margin: 4px 0 12px 0;
  padding-left: 24px;
}
.panel-details li {
  margin: 4px 0;
  line-height: 1.5;
}

/* 高亮标记 */
.highlight {
  background: #fef3c7;
  padding: 2px 4px;
  border-radius: 3px;
}
```

### 颜色语义

| 颜色 | 用途 | 边框色 | 背景色 |
|------|------|--------|--------|
| 蓝色 | 原文/方法 | #2563eb | #eff6ff |
| 橙色 | 目的/目标 | #ea580c | #fff7ed |
| 紫色 | 步骤/流程 | #7c3aed | #f5f3ff |
| 绿色 | 结果/发现 | #059669 | #ecfdf5 |
| 黄色 | 高亮/重点 | - | #fef3c7 |

---

## 5. 质量检查清单

### 交付前必查项目

#### 基础检查

- [ ] 所有9个章节完整
- [ ] Introduction/Methods/Discussion有原文引用
- [ ] 每个Figure有完整结构
- [ ] 方法学有具体参数

#### 图注翻译检查

- [ ] 所有面板标签（a/b/c）完整翻译
- [ ] 所有n值已标注
- [ ] 所有P值标记已标注（*/**/***)
- [ ] 所有比例尺已标注（bar = X μm）
- [ ] 所有浓度/剂量已标注
- [ ] 所有方法学细节已翻译

#### 图片URL检查

- [ ] Elsevier期刊使用gr格式（非fx）
- [ ] Graphical Abstract使用ga1_lrg或ga1
- [ ] PII正确（从DOI/PubMed验证）
- [ ] 所有URL可访问（curl -I验证）

#### 结果解读检查

- [ ] 每个Figure有实验目的（purpose-box）
- [ ] 每个Figure有实验步骤（steps-box）
- [ ] 每个Figure有详细结果解读（panel-details）
- [ ] 每个Figure有逻辑链条说明
- [ ] 每个Figure有机制意义说明

#### CSS样式检查

- [ ] 包含caption-box样式
- [ ] 包含purpose-box样式
- [ ] 包含steps-box样式
- [ ] 包含results-box样式
- [ ] 包含panel-details样式
- [ ] 包含highlight样式

---

## 6. 常见错误及修复

### 错误1：图注翻译过于简化

**症状**：中文翻译只有50-100字，而英文原文有150-200字

**诊断**：
```bash
# 检查中文翻译长度
grep -A 1 "中文翻译：" 讲义.html | wc -c
```

**修复**：参考"中文图注翻译最佳实践"，补充所有技术参数

### 错误2：图片URL使用fx格式

**症状**：图片URL包含`-fx1.jpg`, `-fx2.jpg`

**诊断**：
```bash
grep -n "fx[0-9]\.jpg" 讲义.html
```

**修复**：
```bash
# 替换fx为gr
sed -i 's/-fx\([0-9]\)\.jpg/-gr\1.jpg/g' 讲义.html
```

### 错误3：结果描述过于简洁

**症状**：results-box只有1-2句话，无逐面板解读

**诊断**：检查是否包含`<div class="panel-details">`

**修复**：参考"详细结果解读最佳实践"，添加完整结构

### 错误4：缺少CSS样式

**症状**：purpose-box、steps-box等样式不显示

**诊断**：检查`<style>`标签中是否包含所有必需样式

**修复**：复制"CSS样式规范"中的完整样式代码

---

## 7. 成功案例参考

### 案例1：讲义3（瘢痕Piezo1）

**修复内容**：
- 修复了6个Figure的图片URL（fx → gr）
- 补充了完整的中文图注翻译（增加约200个技术参数）
- 添加了详细的结果解读（从100字扩展到350字/Figure）

**文件位置**：
- `讲义3_瘢痕Piezo1_PMID40254148.html`
- `讲义3图片URL修复报告.md`

### 案例2：讲义4（痤疮PDT）

**特点**：
- 完整的实验目的说明（150-200字/Figure）
- 详细的实验步骤（300-400字/Figure）
- 逐面板结果解读（800-1000字/Figure）

**文件位置**：
- `讲义4_痤疮PDT_PMID39922453.html`

### 案例3：图注翻译修复

**修复范围**：28个caption-box，13个不完整翻译
**新增内容**：约200+个技术参数，约3000字
**平均增长率**：+150%（讲义3最高达+317%）

**文件位置**：
- `图注中文翻译修复报告.md`

---

## 8. 工具与脚本

### 验证图片URL

```bash
#!/bin/bash
# verify_image_urls.sh
# 验证HTML中所有图片URL是否可访问

html_file="$1"
grep -oP 'https://ars\.els-cdn\.com[^"]+\.jpg' "$html_file" | while read url; do
  status=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  if [ "$status" = "200" ]; then
    echo "✅ $url"
  else
    echo "❌ $url (HTTP $status)"
  fi
done
```

### 检查中文翻译完整性

```bash
#!/bin/bash
# check_translation_completeness.sh
# 检查中文翻译是否包含必需的技术参数

html_file="$1"
echo "检查 n 值..."
grep -c "n\s*=\s*[0-9]" "$html_file"

echo "检查 P 值..."
grep -c "\*\*\*P\s*<\|P\s*<\s*\." "$html_file"

echo "检查比例尺..."
grep -c "bar\s*=\s*[0-9]" "$html_file"
```

### 统计Figure描述字数

```bash
#!/bin/bash
# count_figure_description_length.sh
# 统计每个Figure的results-box字数

html_file="$1"
awk '/<div class="results-box">/,/<\/div>/' "$html_file" | \
  sed 's/<[^>]*>//g' | \
  wc -c
```

---

## 9. 未来改进方向

### 短期改进（已规划）

1. **自动化验证脚本**：集成到skill中，自动检查图注完整性和URL正确性
2. **模板生成器**：根据论文类型自动生成对应的Figure结构
3. **批量修复工具**：一键修复所有常见错误

### 长期改进（待评估）

1. **AI辅助翻译**：自动提取技术参数并生成完整中文翻译
2. **图片内容验证**：自动验证图片内容与图注描述是否匹配
3. **交互式质量检查**：生成HTML报告，高亮所有需要修复的问题

---

**本文档持续更新，记录最新的经验教训和最佳实践。**

**最后更新**: 2026-03-03  
**版本**: v2.0
