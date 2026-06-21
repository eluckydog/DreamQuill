"""
DreamQuill 衍梦文枢 — 全自动小说创作引擎试验作品发布网站  v2
每部小说含: 封面 + 梗概 + 创作理念 + 目录 + 全章节
"""
import re, os, shutil

SRC = "C:/Users/13918/AppData/Local/Temp/dq-v2/小说"
OUT = "C:/Users/13918/WorkBuddy/2026-06-18-21-18-46/dreamquill-web"

shutil.rmtree(f"{OUT}/novels", ignore_errors=True)
os.makedirs(f"{OUT}/novels", exist_ok=True)

# ── 作品定义（含梗概和创作理念） ──
NOVELS = [
    {
        "id": "shuangmian", "title": "双面", "file": "双面.md",
        "genre": "都市 · 情感 · 律政",
        "cover": "linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)",
        "synopsis": "陆正言是君恒律所最年轻的合伙人。林初微是他的实习生——聪明、安静、总是坐在他对面的工位上。六个月里他帮她浇了一盆绿植，却从没说过多余的话。六年后，当他在一份竞争对手的客户资料上看到「林初微」三个字时，窗外的天已经暗了。一个关于错过与重逢、爱与背叛的都市故事。他们以对立身份再次相遇时，那些没有说出口的话，已经变成了一道无法逾越的鸿沟。",
        "philosophy": "这是一个关于「没说出口的话」的故事。创作中刻意使用了双POV叙事来制造信息差——读者知道的比任何一个角色都多，从而产生强烈的情感张力。测试重点是：纯提示词系统能否在不同视角切换时保持人物性格的一致性，以及在长时间跨度的叙事中能否维持伏笔的回收质量。",
        "type": "chaptered"
    },
    {
        "id": "jianxin", "title": "剑心", "file": "剑心.md",
        "genre": "同人 · 热血 · 海贼王",
        "cover": "linear-gradient(135deg, #2d1b00 0%, #5c3a00 50%, #8b5e00 100%)",
        "synopsis": "海贼王同人作品。在这个故事里，剑士的「心」比剑更重要。当世界政府的阴影再次笼罩大海，一个年轻剑士踏上了寻找「剑心」的旅途——不是为了变强，而是为了理解自己手中的剑为何而挥。与草帽一伙的命运交织，与七武海的宿命对决，一个关于信念与传承的热血物语。",
        "philosophy": "同人创作的核心挑战是在尊重原著的框架内讲述新故事。本作品测试：纯提示词系统能否准确把握海贼王已有人物的性格特征（路飞的莽撞、索隆的傲气），同时创造有说服力的新角色。节奏上采用红果网剧的快节奏模式——每千字一个小高潮。",
        "type": "oneshot"
    },
    {
        "id": "duji", "title": "渡己", "file": "渡己.md",
        "genre": "喜剧 · 修罗场 · 都市",
        "cover": "linear-gradient(135deg, #1a3a2a 0%, #2d6a4f 50%, #40916c 100%)",
        "synopsis": "一个男人在三任前女友的婚礼上担任司仪的故事。他以为自己已经放下了，直到他在第一场婚礼上念誓词时，看到新娘眼里有泪——而他手心的汗浸湿了卡片。三场婚礼，三段过往，一场荒诞的自我救赎。当最后一杯喜酒下肚，他终于明白：渡人易，渡己难。",
        "philosophy": "喜剧+修罗场是情感密度最高的题材之一。本作品测试：纯提示词系统能否处理好「笑中带泪」的复合情感基调——既要让读者笑出来，又要在笑完之后感到酸楚。同时测试多时间线穿插叙事的连贯性。",
        "type": "oneshot"
    },
    {
        "id": "nidie", "title": "溺蝶", "file": "溺蝶.md",
        "genre": "虐恋 · 都市 · 情感",
        "cover": "linear-gradient(135deg, #2d1a2e 0%, #5c2d5c 50%, #8b408b 100%)",
        "synopsis": "她像一只蝴蝶，美丽而易碎。他以为自己可以保护她，直到发现伤她最深的人就是自己。一段从误解开始、以伤害为养分的爱情。当真相一层层剥开，两个人都已遍体鳞伤。爱是深渊，沉溺其中，无法自拔。",
        "philosophy": "虐恋题材对情感描写的细腻度要求极高。本作品测试：纯提示词系统能否写出让读者「心疼」的段落——不是靠激烈的冲突，而是靠细节的累积。测试重点是情感弧光的自然演进，而非情节驱动的情绪转折。",
        "type": "oneshot"
    },
    {
        "id": "qijian", "title": "第七件寿衣", "file": "第七件寿衣.md",
        "genre": "悬疑 · 灵异 · 短篇",
        "cover": "linear-gradient(135deg, #1a1a1a 0%, #3a1a1a 50%, #5c2d2d 100%)",
        "synopsis": "每一个人都有自己的寿衣，穿上了就没有回头路。一个老裁缝接到七件寿衣的订单——但他不知道，这些寿衣的主人即将以他不理解的方式「领取」它们。当第六件寿衣被取走，老裁缝发现自己陷入了无法逃脱的漩涡。第七件寿衣，是为谁准备的？",
        "philosophy": "悬疑灵异短篇测试：纯提示词系统能否在有限的篇幅内建立完整的悬念结构——从铺垫到发酵到反转。核心挑战是「信息释放的节奏」：读者需要足够的信息来保持好奇，但又不能太多以至于提前猜到结局。",
        "type": "chaptered"
    },
    {
        "id": "shiwai", "title": "诗外", "file": "诗外.md",
        "genre": "穿越 · 古风 · 爽文",
        "cover": "linear-gradient(135deg, #1a2d3a 0%, #2d5c6a 50%, #408b8b 100%)",
        "synopsis": "穿越千年，以诗为剑。现代人顾言意外穿越到一个诗词决定地位的大唐平行世界。在这里，一首好诗可以让一个寒门子弟一夜成名，也可以让一个权倾朝野的宰相跌落谷底。顾言带着满腹唐诗穿越而来——但他很快发现，这个世界的规则远比他想象的要复杂。诗词是敲门砖，但真正决定命运的，是诗词背后的权谋与人心。",
        "philosophy": "穿越古风爽文是中文网络文学最成熟的类型之一，有固定的读者期待模式。本74K字作品测试：纯提示词系统能否批量生产符合类型预期的内容——装逼打脸、踩人升级、美女环绕——同时保持情节的逻辑自洽而非机械重复。",
        "type": "chaptered"
    },
    {
        "id": "shiwai-xu", "title": "诗外·续卷", "file": "诗外-续卷.md",
        "genre": "穿越 · 古风 · 爽文",
        "cover": "linear-gradient(135deg, #1a2d3a 0%, #2d5c6a 50%, #408b8b 100%)",
        "synopsis": "诗外的故事还在继续。顾言在朝堂上站稳脚跟后，面临的挑战从「生存」升级为「掌权」。更深层的权力博弈、更复杂的多角关系、更危险的敌人——以及一个关于穿越本身的惊天秘密。",
        "philosophy": "续卷测试：纯提示词系统能否在延续前作风格的同时，推动情节向前发展而非原地打转。关键的衡量指标是「每一章是否比前一章有新的信息或情感增量」。",
        "type": "supplement"
    },
]

SERIES = [
    {
        "id": "shenyuan-liming", "title": "深渊黎明", "dir": "深渊黎明",
        "genre": "末日 · 生存 · 消防", "volumes": 6,
        "cover": "linear-gradient(135deg, #0a0a0a 0%, #2d0a0a 50%, #5c1a1a 100%)",
        "synopsis": "一种通过空气传播的病毒在72小时内席卷全球。感染者失去理智，只剩捕食本能。城市沦陷，秩序崩塌。在末日降临的那一刻，一群消防员做出了与职业训练完全一致的选择——往最危险的地方走。这不是一个超级英雄拯救世界的故事。这是一个关于普通人在极端环境下如何守住人性底线的故事。",
        "philosophy": "本作品测试纯提示词系统在长篇末日题材中的叙事耐力。6卷49章的内容量，在不依赖持久化存储的前提下，纯靠提示词维持世界观一致性、人物弧光和情节因果链。核心挑战是「末日疲劳」——如何在漫长的求生叙事中每一章都提供新的情感冲击，而不是重复「找到物资→遭遇危险→逃脱」的循环。",
        "files": sorted(os.listdir(f"{SRC}/深渊黎明"))
    },
    {
        "id": "fadun", "title": "法盾系列", "dir": "法盾系列",
        "genre": "AI商战 · 律政 · 国际", "volumes": 4,
        "cover": "linear-gradient(135deg, #0a1628 0%, #1a2d5c 50%, #2d408b 100%)",
        "synopsis": "当AI成为律师，法律成为武器。LexMind——一个由AI驱动的法律科技公司——正在以不可阻挡的速度颠覆全球法律行业。从新加坡到纽约，从莫斯科到伦敦，它的创始人面临着来自传统律所、监管机构和黑客的全面围剿。这是一场关于技术、权力与正义的全球博弈。",
        "philosophy": "法盾系列是衍梦文枢的「技术验证旗舰」。每部使用UB-SUMO世界法则推演引擎设计核心冲突——将不同国家法律体系视作相互作用的「规则场」，推演AI律师进入后产生的连锁反应。四部作品分别测试不同文化背景下的人机博弈叙事（新加坡的华裔商业文化、美国的对抗制诉讼、俄罗斯的灰色地带、英国的传统等级制）。",
        "files": sorted(os.listdir(f"{SRC}/法盾系列"))
    },
    {
        "id": "feitu-jingdian", "title": "废土镜典", "dir": "../examples",
        "genre": "废土 · 科幻 · 镜源", "volumes": 2,
        "cover": "linear-gradient(135deg, #1a0a0a 0%, #3d1a1a 50%, #6b2d2d 100%)",
        "synopsis": "大熄灭之后，世界沦为废土。镜源——一种能改写物质规律的晶体——成为废土上最珍贵的资源，也是最危险的诅咒。沈镜，一个在废墟中长大的拾荒者，意外卷入了一场关于镜器、记忆与代价的千年博弈。使用镜器需要付出代价：创世镜吞噬记忆，律法镜吞噬情感。过度使用会导致「镜衰病」，最终变成一具没有记忆、没有情感、只会呼吸的「镜壳」。",
        "philosophy": "废土镜典是衍梦文枢的「文学性测试件」。与法盾系列的技术验证定位不同，本作侧重测试纯提示词系统在严肃文学风格下的表现——叙事节奏的控制、氛围的营造、人物的深度。蓝晶《魔法学徒》式的详细方法论贯穿全篇，每一章的伏笔都需要在后续章节中回收，这对纯提示词系统的长程记忆和一致性是严峻考验。",
        "files": ["wasteland-mirror-chronicles.txt.txt", "old-zhong-prequel.md.md"]
    },
]

PRODUCTION_SYSTEMS = [
    {
        "id": "lingxu-jiyuan", "title": "灵墟纪元", "dir": "灵墟纪元",
        "cover": "linear-gradient(135deg, #1a2d1a 0%, #2d5c2d 50%, #408b40 100%)",
        "synopsis": "修仙与科学共存的世界，丧尸病毒突然爆发。灵气成为病毒的催化剂——灵气浓度越高，丧尸越强大。人类在修仙文明崩塌的废墟上艰难求生。这是一个关于「当一个时代结束时，夹在中间的人如何找到自己的路」的故事。",
        "philosophy": "灵墟纪元是衍梦文枢的「世界观推演模板」。它不是一部小说，而是一套完整的创作生产系统——包含UB-SUMO世界观推演、因果链图谱、人物总谱、分卷蓝图、伏笔管理表和质量门。任何写手拿到这套文档都可以开始创作百万字级别的长篇连载。测试核心：纯提示词系统能否输出结构完整、逻辑自洽、可直接交付人类写手的创作文档。",
    },
    {
        "id": "wanqi-qiyue", "title": "万界契约", "dir": "万界契约",
        "cover": "linear-gradient(135deg, #2d1a2d 0%, #5c2d5c 50%, #8b408b 100%)",
        "synopsis": "意识穿越+灵兽+规则怪谈。主角意外穿越到一个由「契约」统治的世界——万物之间的互动都由看不见的规则契约约束。违反契约，就会触发无法预料的后果。在这里，语言本身就是一种力量——说出口的话会成为契约的一部分。",
        "philosophy": "万界契约测试纯提示词系统在「规则密集叙事」中的表现——故事的核心驱动力是角色对契约规则的发现和利用，而非传统的战斗升级。这要求AI不仅要生成情节，还要设计自洽的规则系统，并确保所有情节转折都符合已设定的规则。",
    },
]


# ── 解析与渲染 ──
def parse_chapters(filepath):
    """智能章节解析: 先试#，再试##，最后整篇"""
    with open(filepath, encoding="utf-8-sig") as f:
        text = f.read()
    
    # Strategy 1: 按 # 分割 (双面/诗外模式)
    parts = re.split(r'^# ', text, flags=re.MULTILINE)
    chapters = []
    for p in parts:
        if not p.strip():
            continue
        lines = p.split('\n')
        title = lines[0].strip()
        body = '\n'.join(lines[1:]).strip()
        if title and len(body) > 100:  # 有效章节
            chapters.append({"title": title, "body": body})
    
    if len(chapters) >= 2:
        # 检查是否是聚合标题（# 第1-6章 或 # Chapters 1–6 这种）
        # 同时检查标题和正文内是否有聚合标记
        has_aggregator = any(
            re.search(r'第[\d〇一二三四五六七八九十百千]+[-~至到][\d〇一二三四五六七八九十百千]+章', ch['title']) or
            re.search(r'Chapters?\s+\d+[-–]\d+', ch['title'], re.IGNORECASE) or
            re.search(r'^##\s*Chapters?\s+\d+[-–]\d+', ch['body'], re.MULTILINE | re.IGNORECASE)
            for ch in chapters
        )
        if has_aggregator:
            # 递归拆分: 在每章body内按 ## 第x章 或 ## Chapter N 拆分
            final_chapters = []
            sub_pat = re.compile(
                r'^## (第[\d〇一二三四五六七八九十百千]+章[^].\n]*|Chapter\s+\d+\s*[-–—]\s*[^].\n]+)',
                re.MULTILINE | re.IGNORECASE
            )
            for ch in chapters:
                body = ch['body']
                sub_matches = list(sub_pat.finditer(body))
                if len(sub_matches) >= 2:
                    for si, sm in enumerate(sub_matches):
                        s_start = sm.start()
                        s_end = sub_matches[si+1].start() if si+1 < len(sub_matches) else len(body)
                        s_title = sm.group(1).strip()
                        s_body = body[s_start:s_end].strip()
                        s_lines = s_body.split('\n')
                        s_body = '\n'.join(s_lines[1:]).strip()
                        final_chapters.append({"title": s_title, "body": s_body})
                else:
                    final_chapters.append(ch)
            if final_chapters:
                return final_chapters
        return chapters
    
    # Strategy 2: 按 ## 章节名分割 (剑心/渡己/溺蝶模式)
    # 匹配: ## 第1章, ## 第一章, ## Chapter 1, 十、, 尾声等
    lines = text.split('\n')
    chapter_indices = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('## '):
            content = stripped[3:].strip()
            if (re.match(r'^第[\d〇一二三四五六七八九十百千]+章', content) or
                re.match(r'^[\d一二三四五六七八九十]+[、.．]', content) or
                re.match(r'^(尾声|后记|终章)', content) or
                re.match(r'^Chapter\s+\d+', content, re.IGNORECASE)):
                # 过滤子章节: "聚落N"、"节点N"、"一" 等不是真章节
                if re.match(r'^(聚落|节点|一$|二$|三$|四$|五$|六$|七$|八$|九$|十$)', content):
                    continue
                chapter_indices.append(i)
    
    if len(chapter_indices) >= 2:
        chapters = []
        for idx, start_line in enumerate(chapter_indices):
            end_line = chapter_indices[idx+1] if idx+1 < len(chapter_indices) else len(lines)
            title = lines[start_line].strip().replace('## ', '')
            body_lines = lines[start_line+1:end_line]
            # 跳过空行
            while body_lines and not body_lines[0].strip():
                body_lines = body_lines[1:]
            body = '\n'.join(body_lines).strip()
            chapters.append({"title": title, "body": body})
        return chapters
    
    # Strategy 3: 按 ## 分割 (第七件寿衣模式)
    parts2 = re.split(r'^## ', text, flags=re.MULTILINE)
    if len(parts2) >= 3:
        chapters = []
        for p in parts2:
            if not p.strip():
                continue
            ln = p.split('\n')
            title = ln[0].strip()
            body = '\n'.join(ln[1:]).strip()
            # 过滤: 非章节标题/内容太少/子章节标记
            if not title or len(body) < 2000:
                continue
            if re.match(r'^(聚落|节点|章节字数|章节统计)', title):
                continue
            if re.match(r'^\d+$', title):  # 纯数字标题(如"一""二")
                continue
            chapters.append({"title": title, "body": body})
        if len(chapters) >= 2:
            return chapters
    
    # Fallback: 整篇作为一章，提取第一个#标题
    title_match = re.search(r'^#\s+(.+)', text, re.MULTILINE)
    fallback_title = title_match.group(1).strip() if title_match else os.path.basename(filepath).replace('.md','').replace('.txt','')
    return [{"title": fallback_title, "body": text}]
    return [{"title": os.path.basename(filepath).replace('.md',''), "body": text}]

def md2html(text):
    text = re.sub(r'\*\*POV：(.+?)\*\*', r'<div class="pov-tag">POV：\1</div>', text)
    text = re.sub(r'^---+\s*$', r'<hr>', text, flags=re.MULTILINE)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    paras = []
    for p in text.split('\n\n'):
        p = p.strip()
        if not p: continue
        if p.startswith('<d') or p.startswith('<h') or p.startswith('<p'):
            paras.append(p)
        elif p.startswith('## '):
            paras.append(f'<h3>{p[3:]}</h3>')
        else:
            paras.append(f'<p>{p}</p>')
    return '\n'.join(paras)

# ── CSS ──
CSS = '''
*{margin:0;padding:0;box-sizing:border-box}
html{font-size:16px;scroll-behavior:smooth}
body{
  font-family:"Noto Serif SC","Source Han Serif SC",STSong,"宋体",Georgia,serif;
  color:#2c2c2c;background:#f5f0eb;line-height:1.9
}
.site-wrapper{max-width:1000px;margin:0 auto;padding:0 20px}

/* Header */
.site-header{
  background:linear-gradient(135deg,#1a1a2e,#0f3460);color:#e8e8e8;
  padding:0 20px;position:sticky;top:0;z-index:100
}
.header-inner{max-width:1000px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;height:56px}
.site-title{color:#e8e8e8;text-decoration:none;font-size:1.1rem;font-weight:700;letter-spacing:.15em}
.site-title span{color:#64b5f6}
.site-nav a{color:#a0aec0;text-decoration:none;font-size:.85rem;margin-left:20px;transition:.2s}
.site-nav a:hover{color:#e8e8e8}

/* Hero */
.hero{text-align:center;padding:60px 20px;background:linear-gradient(180deg,#f5f0eb 0%,#ede5db 100%)}
.hero h1{font-size:2.2rem;color:#1a1a2e;letter-spacing:.15em;margin-bottom:8px}
.hero .tagline{color:#666;font-size:1rem;max-width:600px;margin:0 auto}
.hero .badge{display:inline-block;margin-top:16px;padding:4px 16px;background:#0f3460;color:#fff;border-radius:20px;font-size:.8rem}

/* Section */
.section-title{font-size:1.15rem;color:#1a1a2e;margin:40px 0 20px;padding-bottom:8px;border-bottom:2px solid #1a1a2e;display:flex;align-items:center;gap:10px}
.section-title .count{font-size:.8rem;color:#999;font-weight:400}

/* Grid */
.novel-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px;margin-bottom:40px}

/* Card */
.novel-card{
  border-radius:10px;padding:28px;color:#e8e8e8;text-decoration:none;
  position:relative;overflow:hidden;transition:transform .2s,box-shadow .2s;
  box-shadow:0 4px 12px rgba(0,0,0,.15);min-height:150px;display:flex;flex-direction:column;justify-content:space-between
}
.novel-card:hover{transform:translateY(-3px);box-shadow:0 8px 24px rgba(0,0,0,.25)}
.novel-card .card-badge{
  display:inline-block;padding:2px 10px;background:rgba(255,255,255,.15);
  border-radius:12px;font-size:.75rem;margin-bottom:10px;width:fit-content
}
.novel-card .card-title{font-size:1.4rem;font-weight:700;letter-spacing:.1em;margin-bottom:6px}
.novel-card .card-desc{font-size:.82rem;color:rgba(255,255,255,.65);line-height:1.5;flex:1}
.novel-card .card-footer{margin-top:12px;font-size:.75rem;color:rgba(255,255,255,.4)}
.novel-card.series{border:2px solid rgba(255,255,255,.2)}

/* Novel Page */
.novel-header{padding:30px 0 0}
.back-link{color:#0f3460;text-decoration:none;font-size:.8rem;padding:6px 14px;border:1px solid #0f3460;border-radius:4px;display:inline-block;margin-bottom:16px;transition:.2s}
.back-link:hover{background:#0f3460;color:#fff}
.cover-large{
  border-radius:12px;padding:50px 40px;text-align:center;color:#e8e8e8;
  box-shadow:0 8px 32px rgba(0,0,0,.3);margin-bottom:30px
}
.cover-large h1{font-size:2.6rem;letter-spacing:.3em;margin-bottom:10px}
.cover-large .sub{color:rgba(255,255,255,.65);font-size:.9rem;margin-bottom:16px}
.cover-large .tags{display:flex;justify-content:center;gap:8px;flex-wrap:wrap}
.cover-large .tags span{padding:4px 14px;background:rgba(255,255,255,.1);border-radius:20px;font-size:.78rem}

/* Synopsis & Philosophy */
.section-block{padding:24px 0 16px}
.section-block h2{font-size:1.1rem;color:#1a1a2e;margin-bottom:12px;padding-bottom:6px;border-bottom:1px solid #e2d8d0}
.section-block p{font-size:.95rem;color:#444;line-height:1.8;text-indent:2em}

/* Chapter List */
.chapter-list{list-style:none;padding:10px 0 30px}
.chapter-list li{border-bottom:1px solid #e2d8d0}
.chapter-list a{
  display:flex;padding:13px 16px;text-decoration:none;color:#2c2c2c;transition:.2s;gap:12px
}
.chapter-list a:hover{background:rgba(15,52,96,.05);padding-left:24px;color:#0f3460}
.ch-num{color:#0f3460;font-weight:600;min-width:5em;font-size:.9rem}

/* Series Chapter List */
.series-chapter-list{list-style:none;padding:10px 0 30px}
.series-chapter-list .volume-header{
  display:flex;justify-content:space-between;align-items:center;
  padding:14px 16px 8px;margin-top:16px;border-bottom:2px solid #1a1a2e;
  font-weight:700;color:#1a1a2e;font-size:1rem;background:rgba(26,26,46,.03);border-radius:6px 6px 0 0
}
.series-chapter-list .volume-header .vol-count{
  font-size:.8rem;color:#999;font-weight:400
}
.series-chapter-list .chapter-item{border-bottom:1px solid #e2d8d0;padding-left:20px}
.series-chapter-list .chapter-item a{
  display:flex;padding:11px 16px;text-decoration:none;color:#2c2c2c;transition:.2s;gap:12px
}
.series-chapter-list .chapter-item a:hover{
  background:rgba(15,52,96,.05);padding-left:24px;color:#0f3460
}

/* Reader */
.reader-top{
  padding:16px 0;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px
}
.reader-top .back{color:#0f3460;text-decoration:none;font-size:.85rem}
.reader-title{font-size:1.2rem;font-weight:600;color:#1a1a2e;text-align:center}
.chapter-body{padding:20px 0;font-size:1.05rem;text-align:justify;max-width:750px;margin:0 auto}
.chapter-body p{text-indent:2em;margin-bottom:1.1em}
.chapter-body hr{border:none;border-top:1px solid #d4cbc3;margin:2em auto;width:30%}
.chapter-body h2,.chapter-body h3{text-align:center;margin:1.8em 0 1em;color:#1a1a2e}
.chapter-body strong{color:#1a1a2e}
.pov-tag{text-align:center;color:#0f3460;font-size:.82rem;letter-spacing:.15em;margin:1.5em 0;font-weight:600}
.reader-nav{
  display:flex;justify-content:space-between;align-items:center;
  padding:24px 0;border-top:1px solid #e2d8d0;max-width:750px;margin:0 auto
}
.reader-nav a{
  text-decoration:none;padding:8px 18px;border:1px solid #cbd5e0;
  border-radius:6px;color:#2c2c2c;font-size:.85rem;transition:.2s
}
.reader-nav a:hover{background:#0f3460;color:#fff;border-color:#0f3460}

/* Footer */
.site-footer{text-align:center;padding:30px 0;color:#a0aec0;font-size:.78rem;border-top:1px solid #e2d8d0;margin-top:30px}

@media(max-width:600px){
  .hero h1{font-size:1.6rem}
  .novel-grid{grid-template-columns:1fr}
  .cover-large{padding:30px 20px}.cover-large h1{font-size:1.8rem}
  .chapter-list a{flex-direction:column;gap:4px}
}
'''


# ═══════════════════════════════════════════════════════════
#  页面渲染
# ═══════════════════════════════════════════════════════════

def page(html, title="衍梦文枢"):
    return f'''<!DOCTYPE html><html lang="zh-CN">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title><link rel="stylesheet" href="style.css">
<body><div class="site-wrapper">
<header class="site-header"><div class="header-inner">
<a href="index.html" class="site-title">衍梦<span>文枢</span></a>
<nav class="site-nav">
<a href="index.html">作品</a>
<a href="https://github.com/eluckydog/DreamQuill">GitHub</a>
</nav></div></header>
{html}
<footer class="site-footer"><p>衍梦文枢 · DreamQuill · 全自动小说创作引擎试验作品</p></footer>
</div></body></html>'''


def gen_index():
    cards = ""
    for n in NOVELS:
        c = n['cover']
        cards += f'''<a href="novels/{n['id']}.html" class="novel-card" style="background:{c}">
  <div><div class="card-badge">{n['genre']}</div>
  <div class="card-title">{n['title']}</div>
  <div class="card-desc">{n['synopsis'][:80]}…</div></div>
  <div class="card-footer">阅读 →</div></a>\n'''

    for s in SERIES:
        cards += f'''<a href="novels/{s['id']}.html" class="novel-card series" style="background:{s['cover']}">
  <div><div class="card-badge">{s['genre']}</div>
  <div class="card-title">{s['title']}</div>
  <div class="card-desc">{s['synopsis'][:80]}…</div></div>
  <div class="card-footer">{s['volumes']}卷 · 阅读 →</div></a>\n'''

    for p in PRODUCTION_SYSTEMS:
        cards += f'''<a href="novels/{p['id']}.html" class="novel-card" style="background:{p['cover']}">
  <div><div class="card-badge">创作档案</div>
  <div class="card-title">{p['title']}</div>
  <div class="card-desc">{p['synopsis'][:80]}…</div></div>
  <div class="card-footer">查看 →</div></a>\n'''

    body = f'''
<div class="hero">
  <h1>衍梦文枢</h1>
  <p class="tagline">全自动小说创作引擎 · 试验作品发布站</p>
  <div class="badge">DreamQuill v1.0 — 纯提示词智能体能力边界测试</div>
</div>
<div class="site-wrapper">
  <h2 class="section-title">小说 <span class="count">{len(NOVELS)+len(SERIES)}部</span></h2>
  <div class="novel-grid">{cards}</div>
  <h2 class="section-title">创作档案 <span class="count">{len(PRODUCTION_SYSTEMS)}套</span></h2>
  <div class="novel-grid" style="margin-bottom:0">
    {''.join(f'<a href="novels/{p["id"]}.html" class="novel-card" style="background:{p["cover"]}"><div><div class="card-badge">创作档案</div><div class="card-title">{p["title"]}</div><div class="card-desc">{p["synopsis"][:80]}…</div></div><div class="card-footer">查看 →</div></a>' for p in PRODUCTION_SYSTEMS)}
  </div>
</div>'''
    return page(body)


def _fmt_chapter_title(title, idx):
    """格式化章节标题: 去掉"第x章"/"Chapter N"前缀避免重复"""
    # 去掉中文 "第x章" 前缀
    title = re.sub(r'^第[\d〇一二三四五六七八九十百千]+章\s*[·.．]?\s*', '', title).strip()
    # 去掉英文 "Chapter N" 前缀
    title = re.sub(r'^Chapter\s+\d+\s*[-–—]\s*', '', title, flags=re.IGNORECASE).strip()
    # 如果去掉后为空，保留原标题的部分内容
    if not title:
        title = re.sub(r'^(第[\d〇一二三四五六七八九十百千]+章|Chapter\s+\d+)\s*', '', title).strip()
    return title

def gen_novel_page(novel):
    fp = f"{SRC}/{novel['file']}"
    chs = parse_chapters(fp) if os.path.exists(fp) else [{"title": novel['title'], "body": ""}]
    toc = "".join(f'<li><a href="{novel["id"]}-{i}.html"><span class="ch-num">第{i+1}章</span>{_fmt_chapter_title(ch["title"], i)}</a></li>' for i,ch in enumerate(chs))
    
    body = f'''
<div class="novel-header">
  <a href="../index.html" class="back-link">← 返回作品列表</a>
  <div class="cover-large" style="background:{novel['cover']}">
    <h1>{novel['title']}</h1>
    <p class="sub">{novel.get('synopsis','')[:120]}</p>
    <div class="tags"><span>{novel['genre']}</span><span>{len(chs)}章</span></div>
  </div>
  <div class="section-block">
    <h2>故事梗概</h2>
    <p>{novel['synopsis']}</p>
  </div>
  <div class="section-block">
    <h2>创作理念</h2>
    <p>{novel['philosophy']}</p>
  </div>
  <h2 class="section-title" style="margin-top:10px">目录 · {len(chs)}章</h2>
  <ol class="chapter-list">{toc}</ol>
</div>'''
    return page(body, f"{novel['title']} — 衍梦文枢")


def gen_series_page(series):
    toc, vol_idx = "", 0
    for fname in series['files']:
        fp = f"{SRC}/{series['dir']}/{fname}"
        with open(fp, encoding='utf-8-sig') as fh:
            text = fh.read()
        vol_title = re.search(r'^# (.+)', text)
        vol_title = vol_title.group(1) if vol_title else fname.replace('.md','').replace('.txt','')
        # 去掉文件名中多余的扩展名
        vol_display = vol_title.replace('.md','').replace('.txt','')
        chs = parse_chapters(fp)
        safe = fname.replace('.md','').replace(' ','-')
        
        # 卷标题(不可点击, 仅标记)
        toc += f'<li class="volume-header"><span class="vol-name">📖 {vol_display}</span> <span class="vol-count">{len(chs)}章</span></li>\n'
        
        # 卷内各章节(可点击)
        for i, ch in enumerate(chs):
            ch_title = ch['title']
            display_title = _fmt_chapter_title(ch_title, i)
            toc += f'<li class="chapter-item"><a href="{series["id"]}-{safe}-{i}.html">'
            toc += f'<span class="ch-num">第{i+1}章</span>{display_title}</a></li>\n'
        
        vol_idx += 1
    
    body = f'''
<div class="novel-header">
  <a href="../index.html" class="back-link">← 返回作品列表</a>
  <div class="cover-large" style="background:{series['cover']}">
    <h1>{series['title']}</h1>
    <p class="sub">{series['synopsis'][:120]}</p>
    <div class="tags"><span>{series['genre']}</span><span>{series['volumes']}卷 · {vol_idx}章</span></div>
  </div>
  <div class="section-block">
    <h2>故事梗概</h2>
    <p>{series['synopsis']}</p>
  </div>
  <div class="section-block">
    <h2>创作理念</h2>
    <p>{series['philosophy']}</p>
  </div>
  <h2 class="section-title" style="margin-top:10px">全书目录 · {vol_idx}章</h2>
  <ul class="series-chapter-list">{toc}</ul>
</div>'''
    return page(body, f"{series['title']} — 衍梦文枢")


def _list_files_recursive(dirpath, prefix=""):
    """递归列出目录下所有文件，返回 (type, rel_path, display_name)"""
    entries = sorted(os.listdir(dirpath))
    items = []
    for e in entries:
        full = os.path.join(dirpath, e)
        rel = os.path.join(prefix, e) if prefix else e
        if os.path.isfile(full):
            if e == "00-总索引.md" or e.endswith('.xlsx'):
                continue
            name = e.replace('.md','')
            items.append(('file', rel, name))
        elif os.path.isdir(full):
            items.append(('dir', rel, e))
            items.extend(_list_files_recursive(full, rel))
    return items

def gen_production_page(ps):
    dirp = f"{SRC}/{ps['dir']}"
    items = _list_files_recursive(dirp)
    total_files = sum(1 for t,_,_ in items if t == 'file')
    
    def render(items, indent=0):
        h = ""
        for t, rel, name in items:
            pad = "&nbsp;&nbsp;" * indent
            if t == 'dir':
                h += f'<li style="list-style:none;margin:6px 0 2px;font-weight:600;color:#1a1a2e">{pad}📁 {name}</li>\n'
            else:
                url = f"https://github.com/eluckydog/DreamQuill/blob/main/小说/{ps['dir']}/{rel.replace(chr(92),'/')}"
                h += f'<li style="list-style:none;margin:2px 0"><a href="{url}" target="_blank" style="color:#0f3460;text-decoration:none">{pad}📄 {name}</a></li>\n'
        return h
    
    body = f'''
<div class="novel-header">
  <a href="../index.html" class="back-link">← 返回作品列表</a>
  <div class="cover-large" style="background:{ps['cover']}">
    <h1>{ps['title']}</h1>
    <p class="sub">{ps['synopsis'][:120]}</p>
    <div class="tags"><span>创作档案</span><span>{total_files}个文件</span></div>
  </div>
  <div class="section-block">
    <h2>故事梗概</h2>
    <p>{ps['synopsis']}</p>
  </div>
  <div class="section-block">
    <h2>创作理念</h2>
    <p>{ps['philosophy']}</p>
  </div>
  <div class="section-block">
    <h2>设计文档目录</h2>
    <p>本作品为百万字级生产系统，包含以下设计文档（共{total_files}个文件）：</p>
    <ul style="margin-top:12px;padding-left:10px">{render(items)}</ul>
  </div>
</div>'''
    return page(body, f"{ps['title']} — 创作档案")


def gen_chapter_page(novel, ch, idx, total):
    prev = f'<a href="{novel["id"]}-{idx-1}.html">‹ 上一章</a>' if idx > 0 else '<span></span>'
    nxt = f'<a href="{novel["id"]}-{idx+1}.html">下一章 ›</a>' if idx < total-1 else '<span></span>'
    html = md2html(ch['body'])
    body = f'''
<div class="reader-top">
  <a href="../novels/{novel['id']}.html" class="back">← 目录</a>
  <span class="reader-title">{ch['title']}</span>
  <span></span>
</div>
<article class="chapter-body">{html}</article>
<nav class="reader-nav">{prev}<a href="../novels/{novel['id']}.html">目录</a>{nxt}</nav>'''
    return page(body, f"{ch['title']} — {novel['title']}")


# ── 生成 ──
with open(f"{OUT}/style.css","w",encoding="utf-8") as f: f.write(CSS)
with open(f"{OUT}/index.html","w",encoding="utf-8") as f: f.write(gen_index())
print("[OK] index.html")

for n in NOVELS:
    fp = f"{SRC}/{n['file']}"
    chs = parse_chapters(fp)
    with open(f"{OUT}/novels/{n['id']}.html","w",encoding="utf-8") as f: f.write(gen_novel_page(n))
    for i,ch in enumerate(chs):
        with open(f"{OUT}/novels/{n['id']}-{i}.html","w",encoding="utf-8") as f: f.write(gen_chapter_page(n,ch,i,len(chs)))
    print(f"[OK] {n['id']} ({len(chs)}ch)")

for s in SERIES:
    print(f"[SERIES] {s['id']} with {len(s['files'])} files")
    with open(f"{OUT}/novels/{s['id']}.html","w",encoding="utf-8") as f: f.write(gen_series_page(s))
    for fname in s['files']:
        fp = f"{SRC}/{s['dir']}/{fname}"
        chs = parse_chapters(fp)
        safe = fname.replace('.md','').replace(' ','-')
        for i,ch in enumerate(chs):
            prev = f'<a href="{s["id"]}-{safe}-{i-1}.html">‹ 上一章</a>' if i > 0 else '<span></span>'
            nxt = f'<a href="{s["id"]}-{safe}-{i+1}.html">下一章 ›</a>' if i < len(chs)-1 else '<span></span>'
            html = md2html(ch['body'])
            body = f'''
<div class="reader-top">
  <a href="../novels/{s['id']}.html" class="back">← 目录</a>
  <span class="reader-title">{ch['title']}</span>
  <span></span>
</div>
<article class="chapter-body">{html}</article>
<nav class="reader-nav">{prev}<a href="../novels/{s['id']}.html">目录</a>{nxt}</nav>'''
            with open(f"{OUT}/novels/{s['id']}-{safe}-{i}.html","w",encoding="utf-8") as f:
                f.write(page(body, f"{ch['title']} — {s['title']}"))

for p in PRODUCTION_SYSTEMS:
    with open(f"{OUT}/novels/{p['id']}.html","w",encoding="utf-8") as f: f.write(gen_production_page(p))
    print(f"[OK] {p['id']} (创作档案)")

total = sum(1 for _,_,fs in os.walk(OUT) for f in fs if f.endswith('.html'))
print(f"\n=== 生成完成: {total} 个HTML页面 ({os.path.getsize(OUT)//1024}KB) ===")
