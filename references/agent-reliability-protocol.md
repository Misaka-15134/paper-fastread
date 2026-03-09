# Agent Reliability Protocol（防缺图/缺章节）

适用场景：当本 skill 被其它 agent 调用时，确保输出稳定完整。

## 目标

1. 不丢章节（固定9章节）
2. 不丢Figure结构（logic/caption/quote/steps/results）
3. 不出现空图片位（至少给出有效图片或可追踪占位）

## 强制执行流程

### Step 1：先复制模板再填充（禁止从空白自由发挥）

- 中文：`templates/lecture-template.html`
- 英文：`templates/lecture-template-en.html`

### Step 2：图片解析与保底

每个 `figure-section` 必须包含 `<img ...>`，并按以下顺序尝试：

1. PMC 主图（`gr`）
2. Elsevier 主图（`gr`）
3. 出版社正文图链接

若均失败，不允许删掉 `<img>`，必须使用可追踪占位：

```html
<img src="https://placehold.co/1200x700?text=Figure+Unavailable" class="fig-img" alt="Figure unavailable" />
```

并在 `caption-box` 备注失败原因与已尝试来源。

### Step 3：结构校验（必跑）

```bash
bash tools/check_template_consistency.sh <output.html> lecture
```

英文输出：

```bash
bash tools/check_template_consistency.sh <output.html> lecture-en
```

### Step 4：自修复循环（最多3轮）

- 若校验失败：只修缺失块和空内容，不重写整文。
- 每次修复后必须重新校验。
- 3轮后仍失败：输出“部分完成 + 缺失清单 + 下一步动作”。

## 禁止项

- 禁止删除失败 Figure 区块
- 禁止把 Results 原文替换成摘要改写
- 禁止跳过校验直接交付
