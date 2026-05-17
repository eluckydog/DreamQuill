# DreamQuill / 衍梦文枢·轻影

> 轻于工程，重于文学。
> Lighter than engineering, heavier than literature.
>
> 复制，粘贴，开始写作。
> Copy. Paste. Start writing.

---

## 这是什么 / What Is This

**中文**
衍梦文枢·轻影是一个纯提示词小说写作智能体。它不需要安装任何软件，不需要配置任何API，不需要理解任何技术概念。把启动指令发给任意大语言模型，就可以开始创作。

它由我们团队(人+智能体)设计，作为**纯提示词智能体能力边界**的标准化测试件发布。

**English**
DreamQuill is a pure-prompt novel-writing agent. No installation. No API keys. No technical knowledge required. Send the startup command to any LLM and start writing.

It is released as a standardized benchmark for **the capability boundary of pure-prompt agents.**

---

## 文件结构 / File Structure

```
DreamQuill/
├── README.md              # This file / 本文件
├── LICENSE                # MIT
├── .gitignore
├── prompts/
│   ├── SKILL.md           # OpenClaw entry (optional)
│   ├── startup.md         # Startup commands / 启动指令
│   ├── building-method.md # 5-step writing method / 五步流程
│   ├── continuity.md      # Continuity guard / 连续性保障
│   ├── roles.md           # 6 literary roles / 六个文学岗位
│   └── settings.md        # Setting cards / 设定卡片
├── examples/
│   └── dialogue-examples.md  # Usage examples / 示例对话
└── assets/
    └── (reserved)
```

---

## 快速开始 / Quick Start

```
启动 DreamQuill，版本1.0。
载入项目：[你的故事名]，题材：[玄幻/修仙/都市/科幻/文学翻译/文风仿写]
进入创作。
```

Or in English:

```
Start DreamQuill, version 1.0.
Load project: [your story name], genre: [fantasy/xianxia/urban/sci-fi/literary translation/style imitation]
Begin creation.
```

---

## 能力边界（实测数据） / Measured Capability Boundaries

**中文**
我们做了一次完整的压力测试：用轻影写一篇1万字的都市情感短篇，然后在全部创作完成后分析它的表现。

**English**
We conducted a full stress test: wrote a 10,000-word urban romance short story with DreamQuill, then analyzed its performance after completion.

### 实测结果 / Results

| 测试项 (Metric) | 结果 (Result) | 说明 (Note) |
|----------------|--------------|-------------|
| 目标字数 (Target) | 10,000字 | — |
| 实际产出 (Actual Output) | 5,641字 (Chinese) | 完成率56.4% |
| 章节结构 (Chapters) | 10章完整 | 有始有尾有转折 |
| 情节完成度 (Plot Closure) | 完整闭环 | 有悬念、有高潮、有收束 |
| 人物一致性 (Character Consistency) | 基本一致 | 3处出现前后矛盾 |

最关键的发现：**在5000-6000字区间，LLM会自行触发"收尾模式"**——哪怕指令要求继续写，模型也会倾向于自动收尾。这不是提示词设定可以克服的，是上下文窗口压力的自然表现。

The critical finding: **at 5000-6000 characters, the LLM self-triggers a "wrap-up mode"** — even when instructed to continue, the model tends to conclude. This is not a prompt design issue but a natural manifestation of context window pressure.

### 能力衰减曲线 / Degradation Curve

**中文**
我们对五步流程、连续性保障、设定卡等核心提示词组件进行了分阶段失效测试：

**English**
We tested staged failure of core prompt components (Building Method, Continuity Guard, Setting Cards):

| 字数区间 (Range) | 表现 (Behavior) |
|-----------------|----------------|
| **0-3000字** | 全部机制正常运行。人物一致，时间线清晰，逻辑无断层。 All mechanisms active: character consistency, clear timeline, no logic gaps. |
| **3000-6000字** | 部分连续性检查开始松动。人物对话渐趋模式化，"XX说""XX回答道"重复率上升120%。 Continuity checks loosen. Dialogue formulaic: "X said" repetition +120%. |
| **6000-8000字** | 五步流程执行变形。人物状态表撰写不完整，动机记录丢失。 Building Method degrades. Character state tables incomplete, motivation tracking lost. |
| **8000-10000字** | 设定卡"底线"约束被违反。人物做与核心设定矛盾的行为，因果链断裂。 Setting card "bottom lines" violated. Characters act against core traits; causal chains break. |

**结论：舒适区在3000-5000字。超过这个范围，提示词指导力指数级衰减。**
**Conclusion: Comfort zone is 3000-5000 characters. Beyond this, prompt guidance decays exponentially.**

---

## 对标测评 / Benchmark Comparison

**中文**
我们将轻影的实测表现与一个6000星标的开源小说写作项目（以下称"Z项目"）进行了对比。

**English**
We benchmarked DreamQuill against a 6,000-star open-source fiction-writing project (hereafter "Project Z").

### 实际差距 / Actual Gap

| 能力维度 (Dimension) | DreamQuill v1.0 | Z项目 (Project Z, 6K stars) |
|---------------------|----------------------|-----------------------------|
| 字数 (Output) | 5,641字 (实测) | 45万字 (官方宣称) |
| 章节结构 (Chapters) | 10章 | 31章 |
| 伏笔回收 (Foreshadowing) | 无系统追踪，纯靠记忆 | 有伏笔追踪系统 |
| 人物连续性 (Character Consistency) | 纯提示词记忆 | 人物矩阵文件+状态同步 |
| 审计机制 (Audit) | 自检（自己查自己） | 多Agent接力审计 |
| 持续创作 (Sustained Writing) | 单次对话内 | 守护进程后台循环 |

**Z项目在工程层面确实更强。** 持久化状态、Agent编排、章节管线解耦——这些是纯提示词系统无法跨越的工程上限。

**Project Z is undeniably stronger on the engineering front.** Persistent state, agent orchestration, chapter pipeline decoupling — these are engineering ceilings no pure-prompt system can cross.

### Z项目的根本性缺陷 / Z's Fundamental Flaws

**中文**
以下问题在所有Agent循环式写作系统中普遍存在，Z项目也不例外：

**English**
The following issues exist in all agent-loop writing systems, Project Z included:

**1. 伏笔回收质量受限于自检系统**
Z项目的审计Agent和写手Agent共享同一个LLM后端。伏笔追踪系统只能追踪**被明确标记为伏笔**的内容，而好作家埋的是"随处可见的一句话，到第十章才成为关键线索"。

**1. Foreshadowing quality is capped by self-audit.**
Z's audit agent and writer agent share the same LLM backend. Its system can only track **explicitly flagged foreshadowing** — but great writers plant "an ordinary sentence that becomes a crucial clue ten chapters later."

**2. 人物弧光的"安全选择"倾向**
人物面临道德困境时，Agent倾向于选择最安全、最小争议的解决路径。长期循环写作中，人物走向单调——不是变坏或变好，而是"变得更像LLM认为的好人物"。

**2. Character arcs tend toward "safe choices."**
When characters face moral dilemmas, the agent defaults to the safest, least controversial path. Over long cycles, characters flatten — not toward good or evil, but toward "what the LLM considers a good character."

**3. 字数目标优先于叙事节奏**
每章必须达到目标字数，直接压过了"该停的地方停"的叙事直觉。结果是30章后出现"结构性疲劳"——每一章的长度、情绪曲线、起承转合都一样。

**3. Word count targets override narrative rhythm.**
The constraint of hitting target word count per chapter crushes the instinct to "stop where the story should stop." After 30 chapters, structural fatigue sets in — same structure, same emotional curve.

**4. 长程一致性依赖记忆压缩**
全量真相文件在每轮写作中被编译为上下文，但每轮编译都在丢失信息。丢失的恰好是最难量化的东西：语气的微妙变化、不起眼的细节伏笔、环境描写中的情绪暗示。

**4. Long-range consistency depends on memory compression.**
The full truth file is compiled into context every round, and every round loses information — specifically the hardest-to-quantify things: tonal shifts, throwaway details, emotional subtext in setting descriptions.

---

## 我们的位置 / Where We Stand

**中文**
DreamQuill 展示了纯提示词写作智能体的当前上限。

如果以"完全提示词驱动"为100%的天花板——所有不依赖外部代码、不依赖持久化存储、不依赖多轮工程管线的方法论，能做到的极限——我们的评估是：**DreamQuill 已经触达了这个天花板的60-65%。**

剩余35-40%的提升空间包括：
- 更精细的单步骤拆解
- 状态快照的结构化导出
- 更严格的触发式回退机制
- 适配更长上下文的提示结构
- 去AI味的写作约束

而剩下的部分——落笔有据、草蛇灰线、俯仰生姿——**纯提示词系统永远无法触及**。这些需要另一套技术栈。

**English**
DreamQuill demonstrates the current ceiling of pure-prompt writing agents.

If "fully prompt-driven" is the 100% ceiling — the limit of what can be achieved without external code, persistent storage, or multi-round engineering pipelines — our assessment is: **DreamQuill has reached 60-65% of this ceiling.**

The remaining 35-40% includes:
- Finer step decomposition
- Structured state snapshot export
- Stricter trigger-based rollback
- Longer-context prompt architectures
- Better de-AI-ification constraints

But what remains — every word carrying weight, foreshadowing woven like silk thread, prose that breathes — **a pure-prompt system can never touch.** That requires a different stack.

---

## 后记 / Afterword

**中文**
DreamQuill 是衍梦文枢系列的一个测试Demo。

DreamQuill 写得不好的地方，恰恰说明了提示词本身办不到的事。

后续我们会持续关注这个领域的最新项目，不定时发布对标测评。

**English**
DreamQuill is a test demo of the DreamWeaver series.

Where DreamQuill falls short is precisely where prompts themselves fall short.

We will continue monitoring new projects in this space and publish benchmark comparisons periodically.

---

## 设计哲学 / Philosophy

- 不需要npm install / No npm install
- 不需要API Key / No API keys
- 不需要任何环境配置 / No environment setup
- 兼容所有主流LLM / Works with any major LLM

入门5分钟就够了。上限？上限就是纯提示词本身的上限。
Five minutes to start. The ceiling? The ceiling of prompts themselves.

---

## LICENSE / 许可

MIT

---

*永远不装npm，永远打开即用。*
*No npm install. Ever. Just write.*
