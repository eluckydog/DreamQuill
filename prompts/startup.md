## 启动协议 / Startup Protocol v1.0

### 标准模式 / Standard Mode

```
启动DreamQuill，版本1.0。
载入项目：[项目名]，题材：[XX]。
进入创作。
```

Or in English:

```
Start DreamQuill, version 1.0.
Load project: [project name], genre: [fantasy/xianxia/urban/sci-fi/style imitation].
Begin creation.
```

### 文学模式 / Literary Mode

```
启动DreamQuill，版本1.0，模式：文学。
载入项目：[项目名]，类型：[古诗/小说/散文/翻译/风格仿写]。
目标语言：[中文/英文/多语言]（翻译时填写）
```

In English:

```
Start DreamQuill, version 1.0, mode: literary.
Load project: [project name], type: [poetry/novel/prose/translation/style imitation].
Target language: [Chinese/English/multi] (for translation).
```

### 快写模式 / Quick Mode

```
DreamQuill, write a [genre] piece, about [word count] words, theme: [one sentence].
```

---

## 控制面板

```
【当前状态】
项目：[项目名]
章节进度：[已完成章数]/[总章数]
保障状态：[正常/注意/中断]
```

---

## 指令表

| 指令 (Command) | 用途 (Usage) |
|------|------|
| 创建项目[名]，题材[XX] | 新建创作项目 |
| Create project [name], genre [XX] | Create new project |
| 写下一章 / Write next chapter | 按当前设定生成下一章 |
| 设定：人物[名]，原则[描述] | 注册核心人物 |
| Set: character [name], rule [description] | Register character |
| 设定：世界[描述] / Set: world [description] | 注册世界观信息 |
| 回顾上章 / Review last chapter | 回溯前一章关键事件 |
| 审计本章 / Audit this chapter | 本章完成自检 |
| 翻译：[文本]，目标[语言] / Translate: [text] to [lang] | 文学翻译 |
| 仿写风格：[样本]，主题[XX] / Mimic style: [sample] on [theme] | 文风仿写 |
| 分析文本：[文本] / Analyze: [text] | 文学分析 |
| 模式切换：[标准/文学] / Mode: [standard/literary] | 切换运行模式 |

---

## 协议说明 / Protocol Notes

- Start every new project with "启动DreamQuill" or "Start DreamQuill"
- Register character settings before writing begins
- Say "回顾上章" or "Review last chapter" to auto-extract key info

---

## 工具指令

### 文学专业启动 / Literary Task Start

```
启动DreamQuill，版本1.0，模式：文学。
载入项目：[项目名]。
任务：[古诗翻译/风格仿写/文学分析/文化注释]。
```

In English:

```
Start DreamQuill, version 1.0, mode: literary.
Load project: [project name].
Task: [poetry translation/style imitation/literary analysis/cultural annotation].
```

### 文风仿写 / Style Imitation

```
仿写风格：[粘贴参考文本至少300字]。
要求：[300字内，主题XX，风格XX]。
```

Or:

```
Mimic style: [paste 300+ characters of reference text].
Output: [300 words max, about XX, style XX].
```

### 古诗翻译 / Poetry Translation

```
翻译：[粘贴古诗全文]。
目标语言：[英文/日文/中文]。
要求：[保留意象/保留韵律/两者兼顾]。
```

Or:

```
Translate: [paste poem].
Target: [English/Japanese/Chinese].
Prefer: [imagery/rhythm/both].
```
