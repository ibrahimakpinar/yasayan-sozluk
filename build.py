#!/usr/bin/env python3
"""Builds the Yaşayan Sözlük animation site into ./public and QR codes into ./qr.

Usage: python3 build.py https://your-site.onrender.com
"""
import html, json, os, sys, shutil

BASE_URL = (sys.argv[1] if len(sys.argv) > 1 else "https://yasayan-sozluk.onrender.com").rstrip("/")
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "public")

# ---------------------------------------------------------------- entries
# Text is taken from the handwritten pages (spelling tidied only).
E = [
 dict(slug="asel", letter="A", name="Asel", origin="Arapça", color="#ffe082",
      meaning="Bal.",
      sentence="Bugün asel yedim."),
 dict(slug="bekir", letter="B", name="Bekir", origin="Arapça", color="#ffd54f",
      meaning="Sabahları erken kalkmayı alışkanlık edinen kimse.",
      sentence="Benim babam çok bekirdir."),
 dict(slug="can", letter="C", name="Can", origin="Farsça", color="#ef9a9a",
      meaning="Yaşama, hayat.",
      sentence="Kedilerin dokuz canı vardır."),
 dict(slug="colpan", letter="Ç", name="Çolpan", origin="Türkçe", color="#9fa8da",
      meaning="Çoban yıldızı, Venüs.",
      sentence="Akşam Çolpan'ı inceledim."),
 dict(slug="doga", letter="D", name="Doğa", origin="Türkçe", color="#a5d6a7",
      meaning="Kendi kuralları çerçevesinde sürekli gelişen, değişen canlı ve cansız varlıkların hepsi, tabiat.",
      sentence="Doğamızı koruyalım."),
 dict(slug="emir", letter="E", name="Emir", origin="Arapça", color="#ffcc80",
      meaning="Bir işin yapılmasını veya yapılmamasını bildiren söz, buyruk, talimat.",
      sentence="Kralın emrini yerine getirmeliyiz."),
 dict(slug="fahriye", letter="F", name="Fahriye", origin="Arapça", color="#fff59d",
      meaning="Onurla, gururla ilgili.",
      sentence="Yarışmayı kazanınca annem benden fahriyeyle bahsetti."),
 dict(slug="giray", letter="G", name="Giray", origin="Türkçe", color="#ffab91",
      meaning="Tarihte Kırım hanlarına verilen san.",
      sentence="Girayımız dört yaşına bastı."),
 dict(slug="isik", letter="I", name="Işık", origin="Türkçe", color="#fff176",
      meaning="Bir yeri aydınlatmaya yarayan araç.",
      sentence="Güneş ışığı bizi aydınlatır."),
 dict(slug="ibrahim", letter="İ", name="İbrahim", origin="İbranice", color="#ffccbc",
      meaning="İnananların babası, halkların babası.",
      sentence=""),
 dict(slug="jale", letter="J", name="Jale", origin="Farsça", color="#b2ebf2",
      meaning="Sabahları yaprakların ve çiçeklerin üzerinde biriken su damlacıkları, çiy, kırağı.",
      sentence="Sabah uyandığımda orkidemin üzerinde jale gördüm."),
 dict(slug="kivanc", letter="K", name="Kıvanç", origin="Türkçe", color="#f8bbd0",
      meaning="Övünç, övünme.",
      sentence="Piyano çalmakta kıvanç duyuyorum."),
 dict(slug="lale", letter="L", name="Lale", origin="Farsça", color="#ce93d8",
      meaning="Zambakgillerden, yaprakları uzun ve mızraksı, çiçekleri kadeh biçiminde, türlü renkte süs bitkisi.",
      sentence="Laleleri çok severim."),
 dict(slug="melek", letter="M", name="Melek", origin="Arapça", color="#90caf9",
      meaning="Tanrı ile insan arasında aracılık yaptığına inanılan, nurdan yaratılmış ruhani varlık.",
      sentence="Benim annem melek gibidir."),
 dict(slug="nihan", letter="N", name="Nihan", origin="Farsça", color="#bcaaa4",
      meaning="Gizli, saklı olan, görünmeyen, sır.",
      sentence="Benim kardeşim ile ilgili bir nihanım var."),
 dict(slug="ozan", letter="O", name="Ozan", origin="Türkçe", color="#80cbc4",
      meaning="Eski Türklerde saz çalarak şiirler, destanlar söyleyen halk şairi.",
      sentence="Ozanlar şiirlerini çok güzel söylediler."),
]

# ---------------------------------------------------------------- animations
# Each is (svg_body, css). viewBox is 0 0 300 300.
A = {}


A["asel"] = ("""
<rect width="300" height="300" fill="#fff8e1"/>
<polygon points="18.0,0.0 9.0,15.6 -9.0,15.6 -18.0,0.0 -9.0,-15.6 9.0,-15.6" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="18.0,62.0 9.0,77.6 -9.0,77.6 -18.0,62.0 -9.0,46.4 9.0,46.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="18.0,124.0 9.0,139.6 -9.0,139.6 -18.0,124.0 -9.0,108.4 9.0,108.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="18.0,186.0 9.0,201.6 -9.0,201.6 -18.0,186.0 -9.0,170.4 9.0,170.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="18.0,248.0 9.0,263.6 -9.0,263.6 -18.0,248.0 -9.0,232.4 9.0,232.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="18.0,310.0 9.0,325.6 -9.0,325.6 -18.0,310.0 -9.0,294.4 9.0,294.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="72.0,31.0 63.0,46.6 45.0,46.6 36.0,31.0 45.0,15.4 63.0,15.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="72.0,93.0 63.0,108.6 45.0,108.6 36.0,93.0 45.0,77.4 63.0,77.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="72.0,155.0 63.0,170.6 45.0,170.6 36.0,155.0 45.0,139.4 63.0,139.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="72.0,217.0 63.0,232.6 45.0,232.6 36.0,217.0 45.0,201.4 63.0,201.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="72.0,279.0 63.0,294.6 45.0,294.6 36.0,279.0 45.0,263.4 63.0,263.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="126.0,0.0 117.0,15.6 99.0,15.6 90.0,0.0 99.0,-15.6 117.0,-15.6" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="126.0,62.0 117.0,77.6 99.0,77.6 90.0,62.0 99.0,46.4 117.0,46.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="126.0,124.0 117.0,139.6 99.0,139.6 90.0,124.0 99.0,108.4 117.0,108.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="126.0,186.0 117.0,201.6 99.0,201.6 90.0,186.0 99.0,170.4 117.0,170.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="126.0,248.0 117.0,263.6 99.0,263.6 90.0,248.0 99.0,232.4 117.0,232.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="126.0,310.0 117.0,325.6 99.0,325.6 90.0,310.0 99.0,294.4 117.0,294.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="180.0,31.0 171.0,46.6 153.0,46.6 144.0,31.0 153.0,15.4 171.0,15.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="180.0,93.0 171.0,108.6 153.0,108.6 144.0,93.0 153.0,77.4 171.0,77.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="180.0,155.0 171.0,170.6 153.0,170.6 144.0,155.0 153.0,139.4 171.0,139.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="180.0,217.0 171.0,232.6 153.0,232.6 144.0,217.0 153.0,201.4 171.0,201.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="180.0,279.0 171.0,294.6 153.0,294.6 144.0,279.0 153.0,263.4 171.0,263.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="234.0,0.0 225.0,15.6 207.0,15.6 198.0,0.0 207.0,-15.6 225.0,-15.6" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="234.0,62.0 225.0,77.6 207.0,77.6 198.0,62.0 207.0,46.4 225.0,46.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="234.0,124.0 225.0,139.6 207.0,139.6 198.0,124.0 207.0,108.4 225.0,108.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="234.0,186.0 225.0,201.6 207.0,201.6 198.0,186.0 207.0,170.4 225.0,170.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="234.0,248.0 225.0,263.6 207.0,263.6 198.0,248.0 207.0,232.4 225.0,232.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="234.0,310.0 225.0,325.6 207.0,325.6 198.0,310.0 207.0,294.4 225.0,294.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="288.0,31.0 279.0,46.6 261.0,46.6 252.0,31.0 261.0,15.4 279.0,15.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="288.0,93.0 279.0,108.6 261.0,108.6 252.0,93.0 261.0,77.4 279.0,77.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="288.0,155.0 279.0,170.6 261.0,170.6 252.0,155.0 261.0,139.4 279.0,139.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="288.0,217.0 279.0,232.6 261.0,232.6 252.0,217.0 261.0,201.4 279.0,201.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="288.0,279.0 279.0,294.6 261.0,294.6 252.0,279.0 261.0,263.4 279.0,263.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="342.0,0.0 333.0,15.6 315.0,15.6 306.0,0.0 315.0,-15.6 333.0,-15.6" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="342.0,62.0 333.0,77.6 315.0,77.6 306.0,62.0 315.0,46.4 333.0,46.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="342.0,124.0 333.0,139.6 315.0,139.6 306.0,124.0 315.0,108.4 333.0,108.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="342.0,186.0 333.0,201.6 315.0,201.6 306.0,186.0 315.0,170.4 333.0,170.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="342.0,248.0 333.0,263.6 315.0,263.6 306.0,248.0 315.0,232.4 333.0,232.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/><polygon points="342.0,310.0 333.0,325.6 315.0,325.6 306.0,310.0 315.0,294.4 333.0,294.4" fill="none" stroke="#ffca28" stroke-width="3" opacity=".5"/>
<g class="jar">
 <rect x="95" y="105" width="110" height="160" rx="12" fill="#ffd54f" stroke="#333" stroke-width="4"/>
 <rect x="95" y="200" width="110" height="34" fill="#fff" stroke="#333" stroke-width="3"/>
 <text x="150" y="226" class="bal">Bal</text>
 <circle cx="132" cy="148" r="5" fill="#333"/><circle cx="168" cy="148" r="5" fill="#333"/>
 <path d="M130,166 Q150,186 170,166" stroke="#333" stroke-width="4" fill="none" stroke-linecap="round"/>
 <circle class="blush" cx="118" cy="168" r="7" fill="#ff8a65"/><circle class="blush" cx="182" cy="168" r="7" fill="#ff8a65"/>
 <path d="M100,108 Q102,124 108,124 Q114,124 114,108Z" fill="#ffb300"/>
 <path class="drip" d="M190,108 Q190,130 196,132 Q202,130 200,108Z" fill="#ffb300"/>
</g>
<g class="lid"><rect x="88" y="82" width="124" height="26" rx="6" fill="#ff7043" stroke="#333" stroke-width="4"/></g>
""" + "".join(
 f'<g class="bee" style="animation-delay:{d}s"><ellipse cx="0" cy="0" rx="13" ry="9" fill="#ffca28" stroke="#333" stroke-width="2"/>'
 f'<rect x="-3" y="-9" width="4" height="18" fill="#333"/><rect x="5" y="-8" width="3" height="16" fill="#333"/>'
 f'<ellipse class="wing" cx="-2" cy="-12" rx="7" ry="5" fill="#e3f2fd" stroke="#90a4ae"/><circle cx="10" cy="-2" r="1.8" fill="#333"/></g>'
 for d in (0, -2.3, -4.6)) + """
""", """
.jar{animation:bob 2s ease-in-out infinite}
@keyframes bob{50%{transform:translateY(-6px)}}
.lid{transform-origin:212px 95px;animation:lid 4s ease-in-out infinite}
@keyframes lid{0%,55%,100%{transform:rotate(0)}65%,85%{transform:rotate(25deg) translate(10px,-12px)}}
.drip{transform-box:fill-box;transform-origin:top;animation:drip 3s ease-in infinite}
@keyframes drip{0%{transform:scaleY(.2)}80%{transform:scaleY(1.6)}100%{transform:scaleY(.2)}}
.blush{animation:tw 1.6s ease-in-out infinite}
.bal{font:bold 24px sans-serif;text-anchor:middle;fill:#5d4037}
.bee{animation:buzz 7s linear infinite}
@keyframes buzz{0%{transform:translate(40px,60px)}24%{transform:translate(250px,50px)}26%{transform:translate(250px,50px) scaleX(-1)}50%{transform:translate(255px,250px) scaleX(-1)}74%{transform:translate(40px,250px) scaleX(-1)}76%{transform:translate(40px,250px)}100%{transform:translate(40px,60px)}}
.wing{animation:flap .12s linear infinite alternate}
@keyframes flap{to{transform:translateY(3px) scaleY(.4)}}
""")

A["bekir"] = ("""
<rect class="sky" width="300" height="300"/>
<g class="rays">""" + "".join(f'<rect x="147" y="10" width="6" height="40" rx="3" fill="#ffe082" transform="rotate({i*30} 150 150)"/>' for i in range(12)) + """</g>
<g class="clock">
 <circle cx="112" cy="78" r="18" fill="#e53935"/><circle cx="188" cy="78" r="18" fill="#e53935"/>
 <circle cx="150" cy="150" r="78" fill="#fffde7" stroke="#424242" stroke-width="8"/>
 """ + "".join(f'<rect x="148" y="80" width="4" height="12" fill="#616161" transform="rotate({i*30} 150 150)"/>' for i in range(12)) + """
 <text x="150" y="108" class="num">12</text><text x="198" y="158" class="num">3</text>
 <text x="150" y="208" class="num">6</text><text x="102" y="158" class="num">9</text>
 <rect class="hour" x="146" y="105" width="8" height="48" rx="4" fill="#212121"/>
 <rect class="min" x="148" y="88" width="4" height="64" rx="2" fill="#424242"/>
 <circle cx="150" cy="150" r="7" fill="#e53935"/>
</g>
<text x="150" y="275" class="hello">Günaydın! ☀️</text>
""", """
.sky{animation:sky 6s ease-in-out infinite}
@keyframes sky{0%{fill:#1a237e}40%{fill:#ffb74d}100%{fill:#81d4fa}}
.rays{transform-origin:150px 150px;animation:spin 12s linear infinite}
.num{font:bold 20px sans-serif;text-anchor:middle;fill:#424242}
.min{transform-origin:150px 150px;animation:spin 1.5s linear infinite}
.hour{transform-origin:150px 150px;animation:hour 6s ease-in-out infinite}
@keyframes hour{0%{transform:rotate(150deg)}60%,100%{transform:rotate(210deg)}}
.clock{transform-origin:150px 150px;animation:ring 6s infinite}
@keyframes ring{0%,62%,100%{transform:rotate(0)}64%,68%,72%,76%{transform:rotate(8deg)}66%,70%,74%,78%{transform:rotate(-8deg)}80%{transform:rotate(0)}}
.hello{font:bold 28px sans-serif;text-anchor:middle;fill:#fff;stroke:#e65100;stroke-width:1;opacity:0;animation:hello 6s infinite}
@keyframes hello{0%,60%{opacity:0}70%,95%{opacity:1}100%{opacity:0}}
""")

HEART = "M0,-8 C-10,-22 -32,-12 -24,6 C-18,18 0,28 0,34 C0,28 18,18 24,6 C32,-12 10,-22 0,-8Z"
A["can"] = ("""
<rect width="300" height="300" fill="#fce4ec"/>
""" + "".join(
  f'<g transform="translate({x} 120)"><path class="mini" style="animation-delay:{i*0.45}s" d="{HEART}" transform="scale(.45)" fill="#f06292"/></g>'
  for i, x in enumerate(range(30, 300, 30))) + f"""
<g transform="translate(150 120)"><path class="big" d="{HEART}" transform="scale(2.4)" fill="#e53935"/></g>
<g transform="translate(150 240)"><g class="cat">
 <polygon points="-38,-20 -30,-52 -10,-30" fill="#ffb74d"/><polygon points="38,-20 30,-52 10,-30" fill="#ffb74d"/>
 <ellipse cx="0" cy="0" rx="45" ry="36" fill="#ffb74d"/>
 <circle cx="-16" cy="-6" r="5" fill="#333"/><circle cx="16" cy="-6" r="5" fill="#333"/>
 <polygon points="-5,6 5,6 0,12" fill="#e91e63"/>
 <path d="M-20,10 L-55,4 M-20,15 L-55,18 M20,10 L55,4 M20,15 L55,18" stroke="#555" stroke-width="2"/>
</g></g>
<text x="150" y="40" class="nine">9 can!</text>
""", """
.big{animation:beat 1s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
@keyframes beat{0%,100%{transform:scale(2.4)}15%{transform:scale(2.8)}30%{transform:scale(2.4)}45%{transform:scale(2.7)}}
.mini{opacity:0;animation:pop 4s ease-out infinite;transform-box:fill-box;transform-origin:center}
@keyframes pop{0%{opacity:0;transform:scale(.1) translateY(60px)}15%{opacity:1;transform:scale(.45) translateY(0)}70%{opacity:1;transform:scale(.45) translateY(-60px)}100%{opacity:0;transform:scale(.45) translateY(-110px)}}
.cat{animation:nod 2s ease-in-out infinite}
@keyframes nod{0%,100%{transform:rotate(-4deg)}50%{transform:rotate(4deg)}}
.nine{font:bold 30px sans-serif;text-anchor:middle;fill:#c2185b}
""")

STAR = "M0,-50 L12,-16 L48,-16 L19,6 L30,40 L0,19 L-30,40 L-19,6 L-48,-16 L-12,-16Z"
A["colpan"] = ("""
<defs><radialGradient id="glow"><stop offset="0" stop-color="#fff9c4" stop-opacity=".9"/><stop offset="1" stop-color="#fff9c4" stop-opacity="0"/></radialGradient></defs>
<rect width="300" height="300" fill="#ff8a65"/>
<rect class="night" width="300" height="300" fill="#0d1b4c"/>
""" + "".join(f'<circle class="tiny" style="animation-delay:{(i*0.37)%3:.2f}s" cx="{(i*67)%290+5}" cy="{(i*41)%170+10}" r="{1.5+(i%3)*0.7}" fill="#fff"/>' for i in range(22)) + f"""
<circle class="halo" cx="150" cy="120" r="70" fill="url(#glow)"/>
<g transform="translate(150 120)"><path class="venus" d="{STAR}" fill="#fff176" stroke="#f9a825" stroke-width="3"/></g>
<path d="M0,250 Q75,215 150,240 T300,235 V300 H0Z" fill="#33691e"/>
<g transform="translate(60 228)"><circle cx="0" cy="-22" r="9" fill="#5d4037"/><rect x="-7" y="-14" width="14" height="24" rx="5" fill="#8d6e63"/><line x1="14" y1="-30" x2="10" y2="12" stroke="#5d4037" stroke-width="3"/></g>
<text x="150" y="215" class="lbl">Venüs</text>
""", """
.night{animation:night 8s ease-in-out infinite}
@keyframes night{0%{opacity:0}35%,90%{opacity:1}100%{opacity:0}}
.tiny{animation:tw 3s ease-in-out infinite}
@keyframes tw{0%,100%{opacity:.2}50%{opacity:1}}
.venus{transform-box:fill-box;transform-origin:center;animation:shine 2.4s ease-in-out infinite}
@keyframes shine{0%,100%{transform:scale(.9) rotate(-6deg)}50%{transform:scale(1.08) rotate(6deg)}}
.halo{animation:tw 2.4s ease-in-out infinite}
.lbl{font:bold 22px sans-serif;text-anchor:middle;fill:#fff9c4}
""")

def tree(x, y, d):
    return (f'<g class="tree" style="animation-delay:{d}s;transform-origin:{x}px {y}px">'
            f'<rect x="{x-6}" y="{y-60}" width="12" height="60" fill="#795548"/>'
            f'<circle cx="{x}" cy="{y-70}" r="26" fill="#43a047"/><circle cx="{x-18}" cy="{y-55}" r="18" fill="#66bb6a"/><circle cx="{x+18}" cy="{y-55}" r="18" fill="#66bb6a"/></g>')
def flower(x, y, c, d):
    return (f'<g class="flower" style="animation-delay:{d}s;transform-origin:{x}px {y}px">'
            f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y-22}" stroke="#388e3c" stroke-width="3"/>'
            + "".join(f'<circle cx="{x}" cy="{y-30}" r="6" fill="{c}" transform="rotate({a} {x} {y-24})"/>' for a in range(0, 360, 72))
            + f'<circle cx="{x}" cy="{y-24}" r="4" fill="#ffeb3b"/></g>')
A["doga"] = ("""
<rect width="300" height="300" fill="#b3e5fc"/>
<g class="sun"><circle cx="240" cy="60" r="26" fill="#ffeb3b"/>""" + "".join(f'<line x1="240" y1="22" x2="240" y2="10" stroke="#fdd835" stroke-width="4" stroke-linecap="round" transform="rotate({a} 240 60)"/>' for a in range(0, 360, 45)) + """</g>
<g class="cloud"><ellipse cx="60" cy="60" rx="30" ry="14" fill="#fff"/><ellipse cx="80" cy="52" rx="20" ry="14" fill="#fff"/></g>
<path class="bird" d="M0,0 q8,-8 16,0 q8,-8 16,0" stroke="#37474f" stroke-width="3" fill="none"/>
<path d="M-20,300 Q60,170 170,300Z" fill="#9ccc65"/>
<path d="M90,300 Q220,160 330,240 V300Z" fill="#7cb342"/>
""" + tree(70, 225, 0) + tree(225, 205, .6) + flower(120, 262, "#e91e63", 1.2) + flower(165, 255, "#ff7043", 1.5) + flower(260, 250, "#ab47bc", 1.8) + """
""", """
.tree{animation:grow 6s ease-out infinite}
@keyframes grow{0%{transform:scale(0)}25%,92%{transform:scale(1)}100%{transform:scale(0)}}
.flower{animation:grow 6s ease-out infinite}
.sun{transform-origin:240px 60px;animation:spin 10s linear infinite}
.cloud{animation:drift 9s linear infinite}
@keyframes drift{from{transform:translateX(-120px)}to{transform:translateX(320px)}}
.bird{animation:fly 7s linear infinite}
@keyframes fly{0%{transform:translate(-40px,110px)}50%{transform:translate(150px,90px) scaleY(.6)}100%{transform:translate(340px,110px)}}
""")

A["emir"] = ("""
<rect width="300" height="300" fill="#fff3e0"/>
<g class="crown"><g transform="translate(150 34)"><polygon points="-34,14 -34,-14 -17,2 0,-20 17,2 34,-14 34,14" fill="#ffc107" stroke="#ff8f00" stroke-width="3"/><circle cx="0" cy="6" r="4" fill="#e53935"/></g></g>
<rect x="68" y="58" width="164" height="20" rx="10" fill="#d7ccc8" stroke="#6d4c41" stroke-width="3"/>
<g class="paper"><rect x="78" y="68" width="144" height="190" fill="#fffde7" stroke="#8d6e63" stroke-width="3"/>
 <text x="150" y="104" class="title">EMİR</text>
 """ + "".join(f'<path class="ln" style="animation-delay:{1+i*.3}s" d="M95,{128+i*20} q12,-6 24,0 t24,0 t24,0 t24,0 t14,0" stroke="#5d4037" stroke-width="2.5" fill="none"/>' for i in range(5)) + """
</g>
<rect class="roll" x="68" y="248" width="164" height="20" rx="10" fill="#d7ccc8" stroke="#6d4c41" stroke-width="3"/>
<g class="seal"><circle cx="190" cy="232" r="18" fill="#c62828"/><circle cx="190" cy="232" r="11" fill="none" stroke="#ef9a9a" stroke-width="2"/></g>
""", """
.paper{transform-origin:150px 68px;animation:unroll 7s ease-out infinite}
@keyframes unroll{0%{transform:scaleY(0)}20%,92%{transform:scaleY(1)}100%{transform:scaleY(0)}}
.roll{animation:rolldown 7s ease-out infinite}
@keyframes rolldown{0%{transform:translateY(-180px)}20%,92%{transform:translateY(0)}100%{transform:translateY(-180px)}}
.title{font:bold 26px serif;text-anchor:middle;fill:#4e342e;letter-spacing:4px}
.ln{stroke-dasharray:140;stroke-dashoffset:140;animation:write 7s linear infinite}
@keyframes write{0%,15%{stroke-dashoffset:140}35%,92%{stroke-dashoffset:0}100%{stroke-dashoffset:140}}
.seal{transform-origin:190px 232px;opacity:0;animation:stamp 7s ease-in infinite}
@keyframes stamp{0%,55%{opacity:0;transform:scale(3)}62%{opacity:1;transform:scale(.9)}66%,92%{opacity:1;transform:scale(1)}100%{opacity:0}}
.crown{animation:bob 2s ease-in-out infinite}
@keyframes bob{50%{transform:translateY(-6px)}}
""")

A["fahriye"] = ("""
<rect width="300" height="300" fill="#fffde7"/>
""" + "".join(f'<rect class="conf" style="animation-delay:{(i*0.31)%3:.2f}s" x="{(i*37)%290}" y="-10" width="8" height="12" fill="{["#e53935","#43a047","#1e88e5","#fdd835","#8e24aa"][i%5]}"/>' for i in range(24)) + f"""
<g class="star"><g transform="translate(150 150) scale(2)"><path d="{STAR}" fill="#fff176" stroke="#424242" stroke-width="2"/>
 <circle cx="-9" cy="-8" r="4" fill="#333"/><circle cx="9" cy="-8" r="4" fill="#333"/>
 <circle cx="-15" cy="2" r="3.5" fill="#e53935"/><circle cx="15" cy="2" r="3.5" fill="#e53935"/>
 <path d="M-10,4 Q0,14 10,4" stroke="#333" stroke-width="2" fill="none"/></g></g>
<g class="medal"><path d="M215,180 L228,212 M245,180 L232,212" stroke="#1e88e5" stroke-width="7"/><circle cx="230" cy="228" r="20" fill="#ffc107" stroke="#ff8f00" stroke-width="3"/><text x="230" y="236" class="one">1</text></g>
<text x="150" y="285" class="bravo">Aferin! 🏆</text>
""", """
.star{transform-origin:150px 250px;animation:jump 1.6s ease-in-out infinite}
@keyframes jump{0%,100%{transform:translateY(0) scale(1,1)}10%{transform:scale(1.1,.9)}45%{transform:translateY(-30px) scale(.95,1.05)}}
.medal{transform-origin:230px 180px;animation:swing 2s ease-in-out infinite}
@keyframes swing{0%,100%{transform:rotate(-12deg)}50%{transform:rotate(12deg)}}
.one{font:bold 20px sans-serif;text-anchor:middle;fill:#fff}
.conf{animation:fall 3s linear infinite}
@keyframes fall{from{transform:translateY(0) rotate(0)}to{transform:translateY(320px) rotate(540deg)}}
.bravo{font:bold 26px sans-serif;text-anchor:middle;fill:#ef6c00}
""")

A["giray"] = ("""
<rect width="300" height="300" fill="#efebe9"/>
<g class="shield">
 <path d="M90,90 H210 V170 Q210,240 150,280 Q90,240 90,170Z" fill="#ff8a65" stroke="#3e2723" stroke-width="5"/>
 <path d="M90,150 H210 V170 Q210,240 150,280 Q90,240 90,170Z" fill="#81d4fa"/>
 <path d="M150,150 H210 V170 Q210,240 150,280Z" fill="#9ccc65"/>
 <path d="M90,90 H210 V170 Q210,240 150,280 Q90,240 90,170Z" fill="none" stroke="#3e2723" stroke-width="5"/>
 <line x1="90" y1="150" x2="210" y2="150" stroke="#3e2723" stroke-width="4"/><line x1="150" y1="150" x2="150" y2="280" stroke="#3e2723" stroke-width="4"/>
 <polygon class="bolt" points="125,165 108,200 122,200 112,232 136,192 122,192 132,165" fill="#ffeb3b" stroke="#3e2723" stroke-width="2"/>
 <g transform="translate(180 200) scale(.38)"><path class="spin2" d="M0,-50 L12,-16 L48,-16 L19,6 L30,40 L0,19 L-30,40 L-19,6 L-48,-16 L-12,-16Z" fill="#ffeb3b" stroke="#3e2723" stroke-width="5"/></g>
</g>
<g class="crown"><polygon points="105,135 105,95 128,118 150,85 172,118 195,95 195,135" fill="#ffeb3b" stroke="#3e2723" stroke-width="4"/>
 <circle cx="150" cy="122" r="6" fill="#e53935"/><circle cx="124" cy="126" r="4" fill="#1e88e5"/><circle cx="176" cy="126" r="4" fill="#1e88e5"/></g>
""" + "".join(f'<text class="spark" style="animation-delay:{d}s" x="{x}" y="{y}">✦</text>' for x, y, d in [(70,80,0),(230,70,.5),(60,200,1),(240,210,1.5),(150,40,2)]) + """
""", """
.crown{animation:crown 5s ease-in-out infinite}
@keyframes crown{0%{transform:translateY(-150px)}30%{transform:translateY(0)}36%{transform:translateY(-10px)}42%,90%{transform:translateY(0)}100%{transform:translateY(-150px)}}
.bolt{animation:flash 1s steps(2) infinite}
@keyframes flash{50%{fill:#fff}}
.spin2{transform-box:fill-box;transform-origin:center;animation:spin 4s linear infinite}
.spark{font-size:22px;fill:#ffb300;animation:tw 2.5s ease-in-out infinite}
""")

A["isik"] = ("""
<defs><radialGradient id="sunglow"><stop offset="0" stop-color="#fffde7"/><stop offset=".5" stop-color="#fff59d" stop-opacity=".8"/><stop offset="1" stop-color="#fff59d" stop-opacity="0"/></radialGradient></defs>
<rect width="300" height="300" fill="#e1f5fe"/>
<path d="M0,240 H300 V300 H0Z" fill="#aed581"/>
<g><rect x="30" y="195" width="50" height="45" fill="#ef9a9a"/><polygon points="25,195 55,170 85,195" fill="#c62828"/><rect x="48" y="215" width="14" height="25" fill="#6d4c41"/></g>
<g><rect x="240" y="190" width="10" height="50" fill="#795548"/><circle cx="245" cy="182" r="22" fill="#66bb6a"/></g>
<rect class="dark" width="300" height="300" fill="#0b1026"/>
<circle class="glow" cx="150" cy="120" r="110" fill="url(#sunglow)"/>
<g class="rays">""" + "".join(f'<rect x="147" y="18" width="6" height="{30 if i%2 else 44}" rx="3" fill="#fdd835" transform="rotate({i*22.5} 150 120)"/>' for i in range(16)) + """</g>
<circle cx="150" cy="120" r="46" fill="#ffeb3b" stroke="#f9a825" stroke-width="4"/>
<circle cx="135" cy="112" r="5" fill="#5d4037"/><circle cx="165" cy="112" r="5" fill="#5d4037"/>
<path d="M132,130 Q150,146 168,130" stroke="#5d4037" stroke-width="4" fill="none" stroke-linecap="round"/>
""", """
.dark{animation:dawn 6s ease-in-out infinite}
@keyframes dawn{0%,10%{opacity:.92}45%,85%{opacity:0}100%{opacity:.92}}
.glow{transform-origin:150px 120px;animation:pulse 2s ease-in-out infinite}
@keyframes pulse{50%{transform:scale(1.15)}}
.rays{transform-origin:150px 120px;animation:spin 8s linear infinite}
""")

A["ibrahim"] = ("""
<rect width="300" height="300" fill="#e3f2fd"/>
<path d="M0,270 H300 V300 H0Z" fill="#c5e1a5"/>
<g class="man">
 <rect x="128" y="190" width="18" height="78" fill="#90caf9" stroke="#333" stroke-width="2"/><rect x="154" y="190" width="18" height="78" fill="#90caf9" stroke="#333" stroke-width="2"/>
 <rect x="118" y="112" width="64" height="82" rx="10" fill="#ff8a65" stroke="#333" stroke-width="2"/>
 <rect x="104" y="118" width="16" height="64" rx="8" fill="#ff8a65" stroke="#333" stroke-width="2"/>
 <g class="arm"><rect x="178" y="118" width="16" height="58" rx="8" fill="#ff8a65" stroke="#333" stroke-width="2" transform="rotate(-140 186 124)"/>
  <circle cx="221" cy="86" r="10" fill="#ffccbc" stroke="#333" stroke-width="2"/></g>
 <rect x="143" y="96" width="14" height="18" fill="#ffccbc"/>
 <circle cx="150" cy="76" r="26" fill="#ffccbc" stroke="#333" stroke-width="2"/>
 <path d="M124,70 Q150,40 176,70 Q150,58 124,70Z" fill="#5d4037"/>
 <circle cx="140" cy="76" r="3.5" fill="#333"/><circle cx="160" cy="76" r="3.5" fill="#333"/>
 <path d="M138,84 Q150,90 162,84" fill="none" stroke="#5d4037" stroke-width="4"/>
 <path d="M140,90 Q150,98 160,90" fill="none" stroke="#333" stroke-width="2"/>
</g>
""" + "".join(
 f'<g class="kid" style="animation-delay:{d}s"><circle cx="{x}" cy="232" r="10" fill="{skin}"/><rect x="{x-9}" y="243" width="18" height="26" rx="5" fill="{c}"/></g>'
 for x, c, skin, d in [(40,"#ab47bc","#ffccbc",0),(78,"#26a69a","#8d6e63",.4),(222,"#fbc02d","#ffe0b2",.8),(262,"#5c6bc0","#a1887f",1.2)]) + """
<g class="bubble"><rect x="196" y="20" width="96" height="36" rx="16" fill="#fff" stroke="#333" stroke-width="2"/><text x="244" y="44" class="hi">Merhaba!</text></g>
""", """
.arm{transform-origin:186px 124px;animation:wave 1s ease-in-out infinite alternate}
@keyframes wave{from{transform:rotate(-14deg)}to{transform:rotate(14deg)}}
.kid{animation:hop 1.2s ease-in-out infinite}
@keyframes hop{50%{transform:translateY(-10px)}}
.bubble{animation:tw 3s ease-in-out infinite}
.hi{font:bold 16px sans-serif;text-anchor:middle;fill:#333}
""")

A["jale"] = ("""
<rect width="300" height="300" fill="#e0f7fa"/>
<circle cx="250" cy="50" r="24" fill="#fff59d"/>
<g transform="rotate(-25 150 200)">
 <path d="M30,200 Q150,120 280,200 Q150,260 30,200Z" fill="#81c784" stroke="#2e7d32" stroke-width="4"/>
 <path d="M30,200 L280,200" stroke="#2e7d32" stroke-width="3"/>
 """ + "".join(f'<path d="M{x},200 L{x+25},{180 if i%2 else 220}" stroke="#2e7d32" stroke-width="2"/>' for i, x in enumerate(range(60, 250, 30))) + """
</g>
<g transform="translate(70 70)"><g class="orchid">""" + "".join(f'<ellipse cx="0" cy="-16" rx="10" ry="18" fill="#f48fb1" transform="rotate({a})"/>' for a in range(0, 360, 72)) + """<circle r="7" fill="#ad1457"/></g></g>
""" + "".join(f'<g class="drop" style="animation-delay:{d}s"><path d="M{x},{y-14} Q{x+9},{y} {x},{y+6} Q{x-9},{y} {x},{y-14}Z" fill="#b3e5fc" stroke="#0288d1" stroke-width="2"/><circle cx="{x-3}" cy="{y-2}" r="2" fill="#fff"/></g>'
  for x, y, d in [(110,195,0),(160,175,.8),(205,150,1.6),(140,215,2.4)]) + """
""" + "".join(f'<text class="spark" style="animation-delay:{d}s" x="{x}" y="{y}">✧</text>' for x, y, d in [(100,170,.3),(200,125,1.1),(170,150,1.9)]) + """
""", """
.drop{animation:drip 4s ease-in infinite;opacity:0}
@keyframes drip{0%{opacity:0;transform:scale(.3)}20%{opacity:1;transform:scale(1)}70%{opacity:1;transform:translate(0,0)}100%{opacity:0;transform:translate(-30px,120px)}}
.orchid{animation:spin 14s linear infinite}
.spark{font-size:20px;fill:#0288d1;animation:tw 2s ease-in-out infinite}
""")

A["kivanc"] = ("""
<rect width="300" height="300" fill="#fce4ec"/>
<g class="face"><circle cx="150" cy="105" r="72" fill="#fff" stroke="#333" stroke-width="4"/>
 <g class="eyes"><circle cx="122" cy="88" r="11" fill="#333"/><circle cx="178" cy="88" r="11" fill="#333"/><circle cx="126" cy="84" r="4" fill="#fff"/><circle cx="182" cy="84" r="4" fill="#fff"/></g>
 <circle class="blush" cx="98" cy="118" r="11" fill="#f48fb1"/><circle class="blush" cx="202" cy="118" r="11" fill="#f48fb1"/>
 <path d="M108,118 Q150,170 192,118Z" fill="#e53935" stroke="#333" stroke-width="3"/></g>
<rect x="20" y="205" width="260" height="80" rx="6" fill="#333"/>
""" + "".join(f'<rect class="key" style="animation-delay:{i*0.25}s" x="{26+i*31}" y="211" width="28" height="68" rx="3" fill="#fff"/>' for i in range(8)) + "".join(f'<rect x="{48+i*31}" y="211" width="16" height="40" fill="#212121"/>' for i in (0,1,3,4,5)) + """
""" + "".join(f'<text class="note" style="animation-delay:{i*0.5}s" x="{40+i*45}" y="200" fill="{c}">{n}</text>' for i, (c, n) in enumerate([("#e53935","♪"),("#fb8c00","♫"),("#43a047","♪"),("#1e88e5","♬"),("#8e24aa","♪"),("#e91e63","♫")])) + """
""", """
.key{animation:press 2s infinite}
@keyframes press{0%,12%{fill:#ffeb3b;transform:translateY(3px)}20%,100%{fill:#fff;transform:none}}
.note{font:bold 30px sans-serif;opacity:0;animation:float 3s ease-out infinite}
@keyframes float{0%{opacity:0;transform:translateY(0)}20%{opacity:1}100%{opacity:0;transform:translate(10px,-170px)}}
.blush{animation:tw 1.5s ease-in-out infinite}
.face{transform-origin:150px 105px;animation:sway 2s ease-in-out infinite}
@keyframes sway{0%,100%{transform:rotate(-5deg)}50%{transform:rotate(5deg)}}
""")

A["lale"] = ("""
<rect width="300" height="300" fill="#f3e5f5"/>
<path d="M0,280 H300 V300 H0Z" fill="#8d6e63"/>
<g class="plant">
 <rect x="146" y="120" width="8" height="160" fill="#66bb6a"/>
 <path class="lleaf" d="M148,250 Q90,200 100,160 Q130,200 148,230Z" fill="#81c784" stroke="#388e3c" stroke-width="2"/>
 <path class="rleaf" d="M152,230 Q210,190 220,150 Q180,170 152,210Z" fill="#81c784" stroke="#388e3c" stroke-width="2"/>
 <g class="bloom">
  <path class="pl" d="M150,130 Q105,120 112,70 Q135,80 150,100Z" fill="#ab47bc"/>
  <path class="pr" d="M150,130 Q195,120 188,70 Q165,80 150,100Z" fill="#ab47bc"/>
  <path d="M150,132 Q128,100 150,62 Q172,100 150,132Z" fill="#ce93d8" stroke="#7b1fa2" stroke-width="2"/>
 </g>
</g>
<g class="bfly"><ellipse cx="-7" cy="0" rx="8" ry="11" fill="#ffb74d"/><ellipse cx="7" cy="0" rx="8" ry="11" fill="#ffb74d"/><rect x="-1.5" y="-9" width="3" height="18" fill="#333"/></g>
""", """
.plant{transform-origin:150px 280px;animation:rise 6s ease-out infinite}
@keyframes rise{0%{transform:scaleY(0)}30%,92%{transform:scaleY(1)}100%{transform:scaleY(0)}}
.pl{transform-origin:150px 130px;animation:openl 6s ease-out infinite}
.pr{transform-origin:150px 130px;animation:openr 6s ease-out infinite}
@keyframes openl{0%,30%{transform:rotate(25deg)}50%,90%{transform:rotate(-8deg)}}
@keyframes openr{0%,30%{transform:rotate(-25deg)}50%,90%{transform:rotate(8deg)}}
.bfly{animation:bfly 8s ease-in-out infinite}
@keyframes bfly{0%{transform:translate(30px,60px) scaleX(1)}25%{transform:translate(240px,40px) scaleX(.3)}50%{transform:translate(250px,180px) scaleX(1)}75%{transform:translate(40px,170px) scaleX(.3)}100%{transform:translate(30px,60px)}}
""")

A["melek"] = ("""
<rect width="300" height="300" fill="#e3f2fd"/>
""" + "".join(f'<text class="spark" style="animation-delay:{d}s" x="{x}" y="{y}">★</text>' for x, y, d in [(40,60,0),(250,50,.6),(30,230,1.2),(265,240,1.8),(200,280,.9),(90,285,1.5)]) + """
<g class="angel">
 <path class="wl" d="M110,160 L40,115 Q25,170 45,215Z" fill="#64b5f6" stroke="#1565c0" stroke-width="3"/>
 <path class="wr" d="M190,160 L260,115 Q275,170 255,215Z" fill="#64b5f6" stroke="#1565c0" stroke-width="3"/>
 <circle cx="150" cy="160" r="58" fill="#fff" stroke="#333" stroke-width="3"/>
 <circle cx="133" cy="148" r="6" fill="#555"/><circle cx="167" cy="148" r="6" fill="#555"/>
 <path d="M130,172 Q150,192 170,172" stroke="#333" stroke-width="3" fill="none"/>
 <ellipse class="halo" cx="150" cy="82" rx="34" ry="10" fill="none" stroke="#fdd835" stroke-width="6"/>
</g>
""", """
.angel{animation:hover 3s ease-in-out infinite}
@keyframes hover{50%{transform:translateY(-18px)}}
.wl{transform-origin:110px 160px;animation:flapl .6s ease-in-out infinite alternate}
.wr{transform-origin:190px 160px;animation:flapr .6s ease-in-out infinite alternate}
@keyframes flapl{to{transform:rotate(14deg) scaleX(.85)}}
@keyframes flapr{to{transform:rotate(-14deg) scaleX(.85)}}
.halo{animation:glowh 1.5s ease-in-out infinite}
@keyframes glowh{50%{stroke:#fff59d;stroke-width:9}}
.spark{font-size:18px;fill:#ffd54f;animation:tw 2s ease-in-out infinite}
""")

A["nihan"] = ("""
<rect width="300" height="300" fill="#efebe9"/>
<g class="beams">""" + "".join(f'<polygon points="150,170 {150+int(140*__import__("math").sin(__import__("math").radians(a)))-10},{170-int(140*__import__("math").cos(__import__("math").radians(a)))} {150+int(140*__import__("math").sin(__import__("math").radians(a)))+10},{170-int(140*__import__("math").cos(__import__("math").radians(a)))}" fill="#fff59d" opacity=".8"/>' for a in range(-60, 61, 20)) + """</g>
<g class="secret"><text x="150" y="80" class="q">?</text><text x="95" y="110" class="q s">?</text><text x="205" y="110" class="q s">?</text></g>
<rect x="70" y="170" width="160" height="100" fill="#a1887f" stroke="#3e2723" stroke-width="4"/>
<rect x="95" y="170" width="12" height="100" fill="#bdbdbd" stroke="#3e2723" stroke-width="2"/><rect x="193" y="170" width="12" height="100" fill="#bdbdbd" stroke="#3e2723" stroke-width="2"/>
<g class="lid"><path d="M70,170 V150 Q150,95 230,150 V170Z" fill="#8d6e63" stroke="#3e2723" stroke-width="4"/>
 <rect x="95" y="128" width="12" height="42" fill="#bdbdbd" stroke="#3e2723" stroke-width="2"/><rect x="193" y="128" width="12" height="42" fill="#bdbdbd" stroke="#3e2723" stroke-width="2"/></g>
<rect class="lock" x="139" y="162" width="22" height="22" fill="#ffc107" stroke="#3e2723" stroke-width="3"/>
<text x="150" y="295" class="shh">Şşş... bu bir sır! 🤫</text>
""", """
.lid{transform-origin:70px 170px;animation:open 5s ease-in-out infinite}
@keyframes open{0%,25%{transform:rotate(0)}40%,75%{transform:rotate(-28deg) translateY(-10px)}90%,100%{transform:rotate(0)}}
.beams,.secret{opacity:0;animation:reveal 5s ease-in-out infinite}
@keyframes reveal{0%,30%{opacity:0}45%,72%{opacity:1}85%,100%{opacity:0}}
.q{font:bold 44px sans-serif;text-anchor:middle;fill:#6a1b9a}
.s{font-size:30px}
.lock{animation:flash 1.2s steps(2) infinite}
.shh{font:bold 18px sans-serif;text-anchor:middle;fill:#4e342e}
""")

A["ozan"] = ("""
<rect width="300" height="300" fill="#e0f2f1"/>
<g class="saz" onclick="playTune()" style="cursor:pointer">
 <g transform="rotate(40 110 210)">
  <rect x="100" y="40" width="20" height="130" fill="#5d4037"/>
  <polygon points="96,40 124,40 130,14 90,14" fill="#3e2723"/>
  <ellipse cx="110" cy="210" rx="52" ry="62" fill="#d7ccc8" stroke="#3e2723" stroke-width="4"/>
  <ellipse cx="110" cy="200" rx="18" ry="22" fill="#3e2723"/>
  """ + "".join(f'<line class="str" style="animation-delay:{i*0.1}s" x1="{104+i*6}" y1="20" x2="{104+i*6}" y2="250" stroke="#eceff1" stroke-width="1.5"/>' for i in range(3)) + """
 </g>
</g>
""" + "".join(f'<text class="note" style="animation-delay:{i*0.45}s" x="{150+i*22}" y="150" fill="{c}">♪</text>' for i, c in enumerate(["#e53935","#fb8c00","#fdd835","#43a047","#1e88e5","#8e24aa"])) + """
<text x="215" y="285" class="tap">Saza dokun! 👆</text>
""", """
.saz{transform-origin:110px 210px;animation:sway 2.4s ease-in-out infinite}
@keyframes sway{0%,100%{transform:rotate(-4deg)}50%{transform:rotate(4deg)}}
.str{animation:vib .12s linear infinite alternate}
@keyframes vib{to{transform:translateX(1.5px)}}
.note{font:bold 34px sans-serif;opacity:0;animation:float 2.7s ease-out infinite}
@keyframes float{0%{opacity:0;transform:translate(0,0)}20%{opacity:1}100%{opacity:0;transform:translate(40px,-140px)}}
.tap{font:bold 16px sans-serif;text-anchor:middle;fill:#00695c}
""")

COMMON_CSS = """
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes tw{0%,100%{opacity:.3}50%{opacity:1}}
@keyframes flash{50%{opacity:.4}}
@media (prefers-reduced-motion: reduce){svg *{animation-duration:20s!important}}
"""

# ---------------------------------------------------------------- templates
STYLE = """
*{box-sizing:border-box}
body{margin:0;font-family:"Trebuchet MS","Segoe UI",system-ui,sans-serif;background:var(--c,#fff8e1);color:#3e2723;min-height:100vh;
 background-image:radial-gradient(rgba(255,255,255,.55) 2px,transparent 2px);background-size:22px 22px}
main{max-width:560px;margin:0 auto;padding:18px 16px 40px}
.top{display:flex;align-items:center;gap:14px}
.badge{flex:none;width:72px;height:72px;border-radius:22px;background:#fff;display:grid;place-items:center;font-size:44px;font-weight:bold;box-shadow:0 4px 0 rgba(0,0,0,.15)}
h1{margin:0;font-size:40px;letter-spacing:1px}
.harf{margin:0;font-size:15px;opacity:.75}
.stage{background:#fff;border-radius:28px;margin:16px 0;overflow:hidden;box-shadow:0 6px 0 rgba(0,0,0,.12)}
.stage svg{display:block;width:100%;height:auto}
.card{background:#fff;border-radius:22px;padding:16px 18px;box-shadow:0 4px 0 rgba(0,0,0,.1);font-size:19px;line-height:1.45}
.card p{margin:6px 0 12px}
.card b{display:block;font-size:13px;text-transform:uppercase;letter-spacing:1px;opacity:.6}
.card .ex{font-style:italic}
.btn{display:inline-flex;align-items:center;gap:8px;border:0;border-radius:999px;padding:12px 20px;font:inherit;font-size:18px;font-weight:bold;background:#3e2723;color:#fff;cursor:pointer;margin-top:4px}
nav{display:flex;justify-content:space-between;margin-top:18px;gap:8px}
nav a{background:#fff;border-radius:999px;padding:10px 16px;text-decoration:none;color:#3e2723;font-weight:bold;box-shadow:0 3px 0 rgba(0,0,0,.12)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:12px;margin-top:18px}
.grid a{display:block;background:var(--cc);border-radius:20px;padding:14px;text-align:center;text-decoration:none;color:#3e2723;box-shadow:0 4px 0 rgba(0,0,0,.12)}
.grid a span{display:block;font-size:42px;font-weight:bold}
footer{margin-top:24px;text-align:center;font-size:13px;opacity:.6}
"""

SCRIPT = """
function playTune(){const C=window.AudioContext||window.webkitAudioContext;if(!C)return;const a=new C();
 [392,440,494,523,494,440,392,330].forEach((f,i)=>{const o=a.createOscillator(),g=a.createGain();o.type='triangle';o.frequency.value=f;
 const t=a.currentTime+i*.22;g.gain.setValueAtTime(.0001,t);g.gain.exponentialRampToValueAtTime(.3,t+.02);g.gain.exponentialRampToValueAtTime(.0001,t+.3);
 o.connect(g).connect(a.destination);o.start(t);o.stop(t+.32)})}
"""

TITLE = "Yaşayan Sözlük"

def page(e, prev, nxt):
    svg, css = A[e["slug"]]
    h = html.escape
    ex = f'<b>Örnek cümle</b><p class="ex">“{h(e["sentence"])}”</p>' if e["sentence"] else ""
    return f"""<!doctype html><html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{h(e["name"])} · {TITLE}</title>
<link rel="stylesheet" href="../style.css"><style>{COMMON_CSS}{css}</style></head>
<body style="--c:{e["color"]}"><main>
<div class="top"><div class="badge">{h(e["letter"])}</div><div><p class="harf">{h(e["letter"])} Harfi</p><h1>{h(e["name"])}</h1></div></div>
<div class="stage"><svg viewBox="0 0 300 300" role="img" aria-label="{h(e["name"])} animasyonu">{svg}</svg></div>
<div class="card">
<b>Anlamı</b><p>{h(e["meaning"])}</p>
<b>Etimolojik kökeni</b><p>{h(e["origin"])}</p>
{ex}
</div>
<nav><a href="../{prev["slug"]}/">← {h(prev["name"])}</a><a href="../">Tüm harfler</a><a href="../{nxt["slug"]}/">{h(nxt["name"])} →</a></nav>
</main><script>{SCRIPT}</script></body></html>"""

def index():
    cards = "".join(f'<a href="{e["slug"]}/" style="--cc:{e["color"]}"><span>{html.escape(e["letter"])}</span>{html.escape(e["name"])}</a>' for e in E)
    return f"""<!doctype html><html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{TITLE}</title>
<link rel="stylesheet" href="style.css"></head><body><main>
<h1>📖 {TITLE}</h1><p>Bir harfe dokun, kelimenin canlandığını gör!</p>
<div class="grid">{cards}</div></main></body></html>"""

def build():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    open(os.path.join(OUT, "style.css"), "w").write(STYLE)
    open(os.path.join(OUT, "index.html"), "w").write(index())
    for i, e in enumerate(E):
        d = os.path.join(OUT, e["slug"]); os.makedirs(d)
        open(os.path.join(d, "index.html"), "w").write(page(e, E[i-1], E[(i+1) % len(E)]))
    build_qr()

def build_qr():
    import qrcode
    from PIL import Image, ImageDraw, ImageFont
    qdir = os.path.join(ROOT, "qr"); shutil.rmtree(qdir, ignore_errors=True); os.makedirs(qdir)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 40)
    except OSError:
        font = ImageFont.load_default()
    tiles = []
    for e in E:
        q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=12, border=3)
        q.add_data(f"{BASE_URL}/{e['slug']}/"); q.make(fit=True)
        img = q.make_image(fill_color="black", back_color="white").convert("RGB")
        w, hgt = img.size
        canvas = Image.new("RGB", (w, hgt + 60), "white"); canvas.paste(img, (0, 0))
        d = ImageDraw.Draw(canvas); label = f"{e['letter']} · {e['name']}"
        tw = d.textlength(label, font=font); d.text(((w - tw) / 2, hgt - 10), label, fill="black", font=font)
        canvas.save(os.path.join(qdir, f"{e['letter']}_{e['slug']}.png"), dpi=(300, 300))
        tiles.append(canvas)
    # A4 sheet @300dpi (2480x3508): 4 columns, each QR ~4.5 cm wide, cut along the grey lines
    sheet = Image.new("RGB", (2480, 3508), "white"); cols = 4; tw = 530
    th = int(tw * tiles[0].size[1] / tiles[0].size[0]); gx = (2480 - cols * tw) // (cols + 1); gy = 60
    dr = ImageDraw.Draw(sheet)
    for i, t in enumerate(tiles):
        t2 = t.resize((tw, int(tw * t.size[1] / t.size[0])), Image.NEAREST)
        x = gx + (i % cols) * (tw + gx); y = 120 + (i // cols) * (th + gy)
        sheet.paste(t2, (x, y))
        dr.rectangle([x - 10, y - 10, x + tw + 10, y + t2.size[1] + 10], outline="#aaaaaa", width=2)
    sheet.save(os.path.join(qdir, "TUM_QR_KODLARI_A4.pdf"), resolution=300)
    sheet.save(os.path.join(qdir, "TUM_QR_KODLARI_A4.png"), dpi=(300, 300))

if __name__ == "__main__":
    build()
    print("Built for", BASE_URL)
