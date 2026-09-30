# -*- coding: utf-8 -*-
"""
生成静态站点：Changsha Street Food Guide
运行：python build_site.py
产出：index.html / articles/*.html / assets/style.css / sitemap.xml / robots.txt

改内容只改 ARTICLES 列表和 SITE 配置，重新运行即可。
"""
import os
import html

BASE = os.path.dirname(os.path.abspath(__file__))

# ============ 站点配置：改成你自己的 ============
SITE = {
    "name": "Changsha Street Food",
    "tagline": "A Practical Guide to Eating on the Streets of Changsha",
    "desc": "Practical, honest guides to Changsha street food — what to eat, what it costs, and where locals actually go.",
    # Vercel 真实域名（已部署）
    "url": "https://changsha-street-food-1fo1lopw8-zap-ab56.vercel.app",
    "author": "Shao Diefei",
}

# ============ 文章数据 ============
# slug: 文件名 / title: <title> / kw: 目标关键词 / desc: meta description
# body: 正文 HTML 段落数组
ARTICLES = [
    {
        "slug": "stinky-tofu",
        "title": "Stinky Tofu in Changsha: A First-Timer's Guide",
        "kw": "changsha stinky tofu",
        "desc": "What Changsha stinky tofu actually tastes like, how much it costs, and how to order your first plate without regret.",
        "body": [
            "Changsha stinky tofu is not the pale, mild version you may have tried elsewhere in China. It is black. Deep, charcoal black, crispy on the outside and soft inside, served with a ladle of garlicky chili sauce and a spoonful of pickled vegetables.",
            "The smell hits you before the stall does. That is normal, and it is not a sign that anything has gone wrong. The odor comes from the fermented brine the tofu sits in — the same process that gives the food its name in Chinese, 臭豆腐 (chòu dòu fǔ).",
            "<h2>What It Actually Tastes Like</h2>",
            "Most first-timers expect the flavor to match the smell. It does not. The taste is much milder — savory, slightly nutty, with a crisp shell that gives way to a custardy center. The sauce does most of the work: minced garlic, chili oil, a splash of broth, and chopped scallions.",
            "<h2>How Much It Costs</h2>",
            "A standard portion runs around ¥10–15 depending on the stall and the location. Tourist-heavy streets charge more. You order by portion size (小份 small / 大份 large), pay first, and wait two to three minutes while it fries.",
            "<h2>Where to Try It</h2>",
            "You do not need a specific famous shop. The best plates usually come from small stalls with a steady line of locals — if people are waiting, the oil is fresh and the turnover is high. Look for stalls near night markets and pedestrian streets across the city.",
            "<h2>First-Timer Tips</h2>",
            "<ul><li>Eat it immediately. The crisp shell softens within minutes.</li><li>Ask for 微辣 (wēi là, mild spice) if you are not used to Hunan heat.</li><li>Do not plan a first date around it.</li><li>One portion is a snack, not a meal. Order two if you are actually hungry.</li></ul>",
        ],
    },
    {
        "slug": "10-street-foods",
        "title": "10 Street Foods You Must Try in Changsha",
        "kw": "changsha street food",
        "desc": "A shortlist of the ten street foods worth your time in Changsha, with rough prices and what to expect from each.",
        "body": [
            "Changsha eats late, eats spicy, and eats outside. This is a practical shortlist — ten things you can actually find on the street, with rough prices so you know what is fair.",
            "<h2>1. Stinky Tofu (臭豆腐)</h2>",
            "Black, crisp, and far milder than it smells. Around ¥10–15. The city's most famous snack for a reason.",
            "<h2>2. Sugar Oil Baba (糖油粑粑)</h2>",
            "Glutinous rice balls fried in sugar and oil until the outside caramelizes. Soft, chewy, very sweet. Around ¥5–10. Best eaten hot.",
            "<h2>3. Rice Noodles (米粉)</h2>",
            "The local breakfast. Thin rice noodles in broth, topped with braised beef, pickled vegetables, or chili oil. Around ¥8–15. See our <a href='/articles/rice-noodles.html'>full guide to Changsha rice noodles</a>.",
            "<h2>4. Spicy Crayfish (口味虾)</h2>",
            "A summer obsession. Crayfish in a heavy, numbing chili sauce, eaten with your hands. Priced by portion and by season — expect ¥80 and up. See <a href='/articles/crayfish.html'>when and where to eat crayfish</a>.",
            "<h2>5. Scallion Pancake (葱油粑粑)</h2>",
            "Not the flat northern-style pancake — this one is a fried ring, crisp outside, chewy inside. A few yuan. A solid breakfast.",
            "<h2>6. Sucked Snails (嗍螺)</h2>",
            "Small river snails in spicy broth. You suck the meat out of the shell — hence the name. Messy, cheap, and very local.",
            "<h2>7. Skewers (烧烤)</h2>",
            "Night-time skewers: meat, vegetables, tofu skin, all dusted with cumin and chili. Priced per skewer, usually ¥2–8. Order by pointing.",
            "<h2>8. Sister Dumplings (姊妹团子)</h2>",
            "Glutinous rice dumplings, one sweet and one savory, traditionally sold as a pair. Soft, sticky, filling.",
            "<h2>9. Milk Tea (奶茶)</h2>",
            "Changsha takes milk tea seriously, and the local chains are genuinely good. ¥12–20. A useful way to cool down after everything above.",
            "<h2>10. Fried Rice Cake (炒年糕)</h2>",
            "Chewy rice cakes stir-fried with chili, vegetables, and sometimes meat. Filling enough to be a meal.",
            "<h2>Before You Go</h2>",
            "Prices here are rough local ranges, not fixed rates. Tourist streets charge more. If a stall has a line of locals, that is usually the best signal you will get.",
        ],
    },
    {
        "slug": "spicy-level",
        "title": "How Spicy Is Hunan Food, Really?",
        "kw": "hunan food spicy level",
        "desc": "An honest breakdown of Hunan spice levels, what 微辣 actually means, and how to order if you can't handle the heat.",
        "body": [
            "Hunan food has a reputation, and the reputation is earned. But the gap between 'spicy' and 'inedible' is smaller than most travel writing suggests — if you know how to order.",
            "<h2>Hunan Heat vs Sichuan Heat</h2>",
            "Sichuan food numbs you with Sichuan pepper (花椒, huā jiāo). Hunan food does not numb — it burns directly, using fresh chilies, pickled chilies, and chili oil. There is less relief, but also less of the strange tingling sensation that some travelers dislike.",
            "<h2>What the Spice Words Mean</h2>",
            "<ul><li><b>不辣 (bù là)</b> — not spicy. Actually available, and actually mild.</li><li><b>微辣 (wēi là)</b> — 'slightly spicy.' In Hunan this is still noticeably spicy to most foreigners.</li><li><b>中辣 (zhōng là)</b> — medium. This is the local default.</li><li><b>特辣 (tè là)</b> — extra hot. Not a joke.</li></ul>",
            "<h2>How to Order If You Can't Handle Spice</h2>",
            "Say 微辣 and mean it. If that is still too much, order 不辣 for one dish and share something spicy on the side. Vendors are used to this and will not take offense. Our guide to <a href='/articles/non-spicy.html'>what to eat in Changsha if you can't handle spice</a> covers this in detail.",
            "<h2>What Actually Helps</h2>",
            "Water makes it worse — capsaicin is oil-soluble, not water-soluble. Milk, yogurt, or anything fatty works far better. Rice helps by dilution. Sweet drinks help a little. Beer does not help, though you will see people trying.",
            "<h2>The Honest Answer</h2>",
            "Yes, it is genuinely spicy. No, you will not be unable to eat. Roughly 80% of street food in Changsha is mild-to-medium, and the truly punishing dishes are the ones you deliberately seek out.",
        ],
    },
    {
        "slug": "night-markets",
        "title": "Changsha Night Markets: Where Locals Actually Eat",
        "kw": "changsha night market",
        "desc": "How Changsha night markets work, when to go, what things cost, and how to tell a good stall from a tourist trap.",
        "body": [
            "Changsha is a night city. Dinner starts late, the streets fill up after 8pm, and the best eating happens when most other Chinese cities are winding down.",
            "<h2>When to Go</h2>",
            "Stalls start setting up around 6pm and hit peak between 8pm and 10pm. Many run past midnight. Going before 7pm means fewer options and lower turnover — which means oil that has been sitting.",
            "<h2>How Ordering Works</h2>",
            "Most stalls follow the same pattern: order at the counter, pay first (Alipay or WeChat Pay; cash is increasingly rare), take a numbered token or just wait nearby, then collect when called. Some places bring food to your table. Nobody will bring you a menu in English — pointing works fine, and photos on the stall sign help.",
            "<h2>How to Spot a Good Stall</h2>",
            "<ul><li><b>A line of locals.</b> The single best signal. High turnover means fresh oil and fresh ingredients.</li><li><b>One or two specialties.</b> Stalls doing three things well beat stalls doing thirty things adequately.</li><li><b>Visible cooking.</b> You should be able to see your food being made.</li><li><b>No English menu with photos of everything.</b> Usually a sign of tourist pricing.</li></ul>",
            "<h2>What to Expect to Pay</h2>",
            "A snack portion runs ¥5–20. A proper meal of several dishes plus a drink runs ¥50–100 per person. Night markets are cheap in absolute terms; the risk is not price, it is ordering twelve things and finishing none of them.",
            "<h2>Practical Notes</h2>",
            "Bring a phone with a payment app set up — cash is awkward. Bring tissues; many stalls do not provide them. Go with at least two people so you can split portions and try more things.",
        ],
    },
    {
        "slug": "rice-noodles",
        "title": "Rice Noodles (米粉): The Breakfast of Changsha",
        "kw": "changsha rice noodles",
        "desc": "How Changsha rice noodles work, what toppings to order, what they cost, and why locals eat them for breakfast.",
        "body": [
            "In Changsha, breakfast is a bowl of rice noodles. Not sometimes — most days. The city runs on 米粉 (mǐ fěn), thin rice noodles in broth, and there is a shop on almost every block.",
            "<h2>How It Works</h2>",
            "You order at the counter, choose your noodle (round or flat), choose your broth (clear or red/spicy), and choose a topping. The bowl arrives in about two minutes. You eat it there, standing or perched on a small stool, usually before 9am.",
            "<h2>Common Toppings</h2>",
            "<ul><li><b>牛肉 (beef)</b> — braised beef slices, the most common choice.</li><li><b>酸豆角 (pickled long beans)</b> — sour, salty, crunchy. A classic add-on.</li><li><b>肉丝 (pork strips)</b> — milder than beef.</li><li><b>榨菜 (preserved vegetable)</b> — cheap and sharp.</li><li><b>辣椒炒肉 (chili fried pork)</b> — the local favorite, and spicy.</li></ul>",
            "<h2>What It Costs</h2>",
            "A basic bowl runs around ¥8–15 depending on the topping. Extra toppings add a few yuan. It is one of the best value meals you will find in the city.",
            "<h2>Useful Things to Know</h2>",
            "Breakfast shops often close by late morning or sell out. If you want noodles at noon, look for shops that stay open all day — they exist, but they are less common. You can also ask for 不要辣 (bù yào là, no chili) and add chili oil yourself from the table condiments.",
            "<h2>Why Locals Eat This for Breakfast</h2>",
            "It is fast, it is hot, it is cheap, and it is filling without being heavy. A bowl takes five minutes to eat. For a city that works early and eats late, that is exactly what breakfast needs to be.",
        ],
    },
    {
        "slug": "non-spicy",
        "title": "What to Eat in Changsha If You Can't Handle Spice",
        "kw": "changsha non spicy food",
        "desc": "A practical list of Changsha foods that are genuinely mild, plus exactly what to say when ordering.",
        "body": [
            "You can eat well in Changsha without eating spicy food. It takes slightly more care, but the city has plenty of mild options — and locals eat them too.",
            "<h2>What to Say</h2>",
            "<ul><li><b>不要辣 (bú yào là)</b> — no chili, please. The most useful phrase you will learn.</li><li><b>微辣 (wēi là)</b> — a little spicy. Still noticeable.</li><li><b>一点辣 (yī diǎn là)</b> — just a tiny bit.</li></ul>",
            "Say it when you order, not after the food arrives. Most stalls cook to order and will happily leave the chili out.",
            "<h2>Reliably Mild Dishes</h2>",
            "<ul><li><b>Sugar Oil Baba (糖油粑粑)</b> — sweet, fried, no chili at all.</li><li><b>Rice noodles in clear broth (清汤米粉)</b> — ask for the clear soup, not the red one.</li><li><b>Steamed buns and dumplings</b> — widely available, mild, cheap.</li><li><b>Milk tea</b> — Changsha's local chains are excellent and completely safe.</li><li><b>Grilled skewers without chili powder</b> — ask for 不辣; cumin-only is common and delicious.</li><li><b>Fried rice cake without chili</b> — chewy, savory, mild.</li></ul>",
            "<h2>What to Watch Out For</h2>",
            "Some dishes are spicy by construction — the sauce is made in advance and cannot be adjusted. If you point at something in a big pot of red chili oil, it will be spicy no matter what you say. When unsure, point at ingredients rather than finished dishes.",
            "<h2>The Honest Bottom Line</h2>",
            "You will eat slightly less variety than a chili-tolerant traveler. You will not go hungry. See also our guide to <a href='/articles/spicy-level.html'>how spicy Hunan food actually is</a>.",
        ],
    },
    {
        "slug": "sugar-oil-baba",
        "title": "Sugar Oil Baba (糖油粑粑): Changsha's Sweetest Snack",
        "kw": "sugar oil baba",
        "desc": "What sugar oil baba is, how it's made, what it costs, and why it's the one Changsha snack with no chili in it.",
        "body": [
            "糖油粑粑 (táng yóu bā bā) is the outlier in a city of chili. It contains no spice at all, costs almost nothing, and is one of the few local snacks you can hand to a child without hesitation.",
            "<h2>What It Is</h2>",
            "Glutinous rice dough, rolled into balls, flattened slightly, and fried in a mixture of oil and sugar until the outside caramelizes into a thin, glossy shell. The inside stays soft and chewy. It is served on a stick or in a small paper cup, usually three to five pieces per portion.",
            "<h2>How It Tastes</h2>",
            "Sweet, but not frosting-sweet — the sugar is caramelized rather than raw, so there is a slight bitterness balancing it. The texture is the point: crisp shell, then a dense, sticky, mochi-like center. It is heavy for its size.",
            "<h2>What It Costs</h2>",
            "Usually ¥5–10 per portion, making it one of the cheapest things on the street. Street stalls and small shops across the city sell it, often in the afternoon rather than late at night.",
            "<h2>When to Eat It</h2>",
            "Eat it hot and fresh. As it cools, the shell loses its crispness and the center turns firmer. It does not reheat well. Buy it, eat it within five minutes, move on.",
            "<h2>Why It Matters</h2>",
            "If you are traveling with someone who does not eat spicy food, this is the snack you will end up buying repeatedly. It is also the least intimidating entry point to Changsha street food generally — see our list of <a href='/articles/non-spicy.html'>mild foods in Changsha</a> for more.",
        ],
    },
    {
        "slug": "street-food-prices",
        "title": "A Foreigner's Price Guide to Changsha Street Food",
        "kw": "changsha street food prices",
        "desc": "Realistic price ranges for Changsha street food, what counts as tourist pricing, and how to pay without cash.",
        "body": [
            "Changsha is a cheap city to eat in. The problem is rarely the price — it is not knowing whether a price is fair. Here are the ranges.",
            "<h2>Snack Prices</h2>",
            "<ul><li>Stinky tofu: ¥10–15 per portion</li><li>Sugar oil baba: ¥5–10</li><li>Scallion pancake: ¥3–8</li><li>Skewers: ¥2–8 each</li><li>Milk tea: ¥12–20</li></ul>",
            "<h2>Meal Prices</h2>",
            "<ul><li>Rice noodles (breakfast bowl): ¥8–15</li><li>Casual restaurant dish: ¥20–50</li><li>Crayfish (seasonal, by portion): ¥80 and up</li><li>Full night market meal for one: ¥40–80</li></ul>",
            "<h2>How to Tell Tourist Pricing</h2>",
            "The clearest signal is location. Stalls on the main pedestrian shopping streets charge noticeably more — often 30–50% above what the same item costs three blocks away. The food is usually identical. Walk a little.",
            "The second signal is presentation: laminated English menus with photos of every dish tend to indicate a place that prices for visitors rather than locals.",
            "<h2>How to Pay</h2>",
            "Alipay and WeChat Pay are the default. Both now accept foreign cards, but set them up before you go — registration takes time and may need passport verification. Cash still works but is increasingly awkward at small stalls. Carry ¥100–200 in small bills as backup.",
            "<h2>Is Bargaining Expected?</h2>",
            "No. Street food has fixed prices. Bargaining is for markets selling goods, not food stalls. Asking 多少钱 (duō shǎo qián, how much) is fine; haggling is not.",
            "<p><i>Note: prices are approximate local ranges and shift with location and season. Treat them as a sanity check, not a quote.</i></p>",
        ],
    },
    {
        "slug": "crayfish",
        "title": "Crayfish Season in Changsha: When and Where",
        "kw": "changsha crayfish",
        "desc": "When crayfish season runs in Changsha, how 口味虾 is served, what it costs, and how to eat it without a mess.",
        "body": [
            "口味虾 (kǒu wèi xiā) — 'flavor shrimp,' though it is crayfish, not shrimp — is the dish Changsha waits for all year. When the season starts, the city eats crayfish outdoors, late, and in enormous quantities.",
            "<h2>When Is the Season</h2>",
            "Roughly late spring through early autumn, with peak quality and peak crowds in summer. Outside these months you can still find it, but the price rises and the quality drops. Summer evenings are the real thing.",
            "<h2>How It's Served</h2>",
            "A large bowl of crayfish in a heavy red sauce of chili, garlic, and spices, often with a numbing element and sometimes with noodles or vegetables at the bottom to soak up the sauce. You peel them by hand. It is, unavoidably, messy.",
            "<h2>What It Costs</h2>",
            "Priced by portion and by market price, so it varies more than other street food. Expect ¥80 and up for a serving, more at established restaurants. For current local ranges, see our <a href='/articles/street-food-prices.html'>Changsha street food price guide</a>.",
            "<h2>How to Eat It</h2>",
            "<ul><li>Twist the tail and pull — the meat comes out in one piece.</li><li>The head contains fat and flavor; locals suck it. Optional, and messy.</li><li>Ask for gloves. Most places provide them.</li><li>Order something mild alongside. Eating an entire bowl of this is a commitment.</li></ul>",
            "<h2>Practical Notes</h2>",
            "This is a group dish. Go with three or four people, order one portion of crayfish plus several other things, and share. It is also one of the spicier things you will encounter — see <a href='/articles/spicy-level.html'>our honest guide to Hunan spice levels</a> before committing.",
        ],
    },
    {
        "slug": "street-food-safety",
        "title": "Street Food Safety Tips for Travelers in China",
        "kw": "china street food safety",
        "desc": "Practical, non-alarmist advice on eating street food safely in China — what actually matters and what doesn't.",
        "body": [
            "Street food in China is broadly safe. Millions of people eat it daily. The advice below is about reducing an already-small risk, not about avoiding anything.",
            "<h2>The Rule That Matters Most</h2>",
            "<b>Eat where the turnover is high.</b> A stall with a steady line of customers is cooking fresh food and using oil that gets replaced regularly. A stall with no customers at 8pm is the one to skip. This single heuristic covers most of the real risk.",
            "<h2>Other Things That Actually Help</h2>",
            "<ul><li><b>Watch it being cooked.</b> Food served hot and freshly made is safer than food sitting in a tray.</li><li><b>Avoid raw or undercooked items</b> if you have a sensitive stomach — this is the one category worth being cautious about.</li><li><b>Peel fruit yourself.</b> Standard travel advice, still true.</li><li><b>Be careful with ice</b> if you are cautious, though most commercial ice in cities is fine.</li><li><b>Carry hand sanitizer.</b> Many stalls have no running water for customers.</li></ul>",
            "<h2>Things That Are Overrated as Risks</h2>",
            "Spice does not make food unsafe. Unfamiliar ingredients do not make food unsafe. 'Mystery meat' is almost always exactly what the sign says — the barrier is language, not dishonesty.",
            "<h2>If Something Goes Wrong</h2>",
            "Pharmacies (药房, yào fáng) are everywhere and staff can usually help with basic stomach issues. For anything serious, go to a hospital — in a city like Changsha, this is straightforward. Travel insurance that covers medical care is worth having.",
            "<h2>The Honest Summary</h2>",
            "You are more likely to be uncomfortable from eating too much spicy food than from anything unsafe. Pace yourself, pick busy stalls, and eat the stinky tofu.",
        ],
    },
]

# ============ 模板 ============
CSS = """
:root{--maxw:720px;--fg:#1a1a1a;--muted:#666;--accent:#c0392b;--bg:#fff;--line:#e6e6e6}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,"PingFang SC","Microsoft YaHei",sans-serif;
color:var(--fg);background:var(--bg);line-height:1.75;font-size:17px}
header.site{border-bottom:1px solid var(--line);padding:20px 0;margin-bottom:32px}
header.site .wrap,main,footer.site .wrap{max-width:var(--maxw);margin:0 auto;padding:0 20px}
header.site a.brand{font-weight:700;font-size:19px;color:var(--fg);text-decoration:none}
header.site .tag{color:var(--muted);font-size:14px;margin-top:2px}
h1{font-size:29px;line-height:1.3;margin:0 0 12px}
h2{font-size:21px;margin:32px 0 10px}
p{margin:0 0 16px}
ul{padding-left:22px;margin:0 0 16px}
li{margin-bottom:7px}
.meta{color:var(--muted);font-size:14px;margin-bottom:26px;padding-bottom:14px;border-bottom:1px solid var(--line)}
.kw{display:inline-block;background:#f4f4f4;border-radius:4px;padding:2px 8px;font-size:12px;color:var(--muted);margin-left:6px}
a{color:var(--accent)}
.card{border-bottom:1px solid var(--line);padding:18px 0}
.card h2{margin:0 0 6px;font-size:20px;line-height:1.35}
.card h2 a{color:var(--fg);text-decoration:none}
.card h2 a:hover{color:var(--accent)}
.card p{margin:0;color:var(--muted);font-size:15px}
.hero{padding:8px 0 26px}
.hero p{font-size:18px;color:#444}
footer.site{border-top:1px solid var(--line);margin-top:50px;padding:24px 0;color:var(--muted);font-size:14px}
.back{display:inline-block;margin-top:34px;font-size:15px}
"""

def page(title, desc, body_html, is_home=False):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="stylesheet" href="{'assets/style.css' if is_home else '../assets/style.css'}">
</head>
<body>
<header class="site"><div class="wrap">
<a class="brand" href="{'index.html' if is_home else '../index.html'}">{html.escape(SITE['name'])}</a>
<div class="tag">{html.escape(SITE['tagline'])}</div>
</div></header>
<main>
{body_html}
</main>
<footer class="site"><div class="wrap">
{html.escape(SITE['name'])} · Built as a content-operations portfolio project · Contact: {html.escape(SITE['author'])}
</div></footer>
</body>
</html>
"""


def build():
    # CSS
    os.makedirs(os.path.join(BASE, "assets"), exist_ok=True)
    os.makedirs(os.path.join(BASE, "articles"), exist_ok=True)
    with open(os.path.join(BASE, "assets", "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS)

    # 首页
    cards = []
    for a in ARTICLES:
        cards.append(
            f'<div class="card"><h2><a href="articles/{a["slug"]}.html">{html.escape(a["title"])}</a></h2>'
            f'<p>{html.escape(a["desc"])}</p></div>'
        )
    home_body = (
        '<div class="hero"><h1>Changsha Street Food Guide</h1>'
        f'<p>{html.escape(SITE["desc"])}</p></div>'
        + "\n".join(cards)
    )
    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(page(f'{SITE["name"]} — {SITE["tagline"]}', SITE["desc"], home_body, is_home=True))

    # 文章页
    for a in ARTICLES:
        body = (
            f'<article><h1>{html.escape(a["title"])}</h1>'
            f'<div class="meta">By {html.escape(SITE["author"])}<span class="kw">{html.escape(a["kw"])}</span></div>'
            + "\n".join(f"<p>{p}</p>" if not p.startswith("<") else p for p in a["body"])
            + f'<a class="back" href="../index.html">&larr; Back to all guides</a></article>'
        )
        with open(os.path.join(BASE, "articles", f'{a["slug"]}.html'), "w", encoding="utf-8") as f:
            f.write(page(a["title"], a["desc"], body))

    # sitemap.xml
    urls = [SITE["url"] + "/"] + [f'{SITE["url"]}/articles/{a["slug"]}.html' for a in ARTICLES]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{html.escape(u)}</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>")
    sm.append("</urlset>")
    with open(os.path.join(BASE, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(sm) + "\n")

    # robots.txt
    with open(os.path.join(BASE, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE['url']}/sitemap.xml\n")

    print(f"OK: 生成 {len(ARTICLES)} 篇文章 + index.html + sitemap.xml + robots.txt")
    for a in ARTICLES:
        print("  -", a["slug"])


if __name__ == "__main__":
    build()
