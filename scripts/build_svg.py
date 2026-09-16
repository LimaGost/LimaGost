import json

with open('/home/claude/profile-readme/dots.json') as f:
    dots = json.load(f)

W = 940
TITLEBAR_H = 34
PAD = 20
MAP_X, MAP_Y = PAD, TITLEBAR_H + 40
MAP_W, MAP_H = 380, 460
INFO_X = MAP_X + MAP_W + 40
INFO_Y = TITLEBAR_H + 30
INFO_W = W - INFO_X - PAD

CHAR_W = 7.35  # approx width per monospace char at 12.5px

def leader_dots(label, value, x_start, x_end):
    label_w = len(label) * CHAR_W
    value_w = len(value) * CHAR_W
    avail = (x_end - x_start) - label_w - value_w - 16
    n = max(2, int(avail / CHAR_W))
    return "." * n

dot_color = "#3fd0e8"
dot_dim = "#1c5f6e"
circles = []
for x, y, r in dots:
    fill = dot_color if r > 1.0 else dot_dim
    circles.append(f'<circle cx="{MAP_X+x:.2f}" cy="{MAP_Y+y:.2f}" r="{r:.2f}" fill="{fill}"/>')
circles_svg = "\n    ".join(circles)

def info_line(label, value, y, label_color="#6bb8c9"):
    dotted = leader_dots(label, value, INFO_X, INFO_X + INFO_W)
    return (f'<text x="{INFO_X}" y="{y}" class="lbl" fill="{label_color}">{label}</text>'
            f'<text x="{INFO_X+148}" y="{y}" class="dots">{dotted}</text>'
            f'<text x="{INFO_X+INFO_W}" y="{y}" text-anchor="end" class="val">{value}</text>')

lines = []
y = INFO_Y + 30
lh = 24.5

lines.append(f'<text x="{INFO_X}" y="{y}" class="section">SYSTEM.INFO</text>')
y += lh
lines.append(f'<text x="{INFO_X}" y="{y}" class="prompt">lima@fullstack:~$</text>')
y += lh * 1.5

fields_top = [
    ("Subject", "Iury Santos Lima"),
    ("Role", "Analista de Implantacao ERP"),
    ("Origin", "Aparecida de Goiania, GO - BR"),
    ("Education", "Tecnologo ADS - Estacio, 2026"),
    ("Status", "Implantando . Aprendendo . Integrando"),
    ("ToolChain", "VS Code, Git, Claude Code, Postman"),
]
for label, val in fields_top:
    lines.append(info_line(label, val, y))
    y += lh

y += lh * 0.4
lines.append(f'<line x1="{INFO_X}" y1="{y-15}" x2="{INFO_X+INFO_W}" y2="{y-15}" stroke="#1c3a42" stroke-width="1"/>')

fields_stack = [
    ("Core Domain", "Microvix ERP, NF-e/NFC-e, ICMS"),
    ("Core Frontend", "React, Vite, TypeScript"),
    ("Core Backend", "Node.js, Express, REST APIs"),
    ("Core Database", "PostgreSQL, Supabase"),
    ("Core Infra", "Docker, OAuth 2.0 / PKCE"),
]
for label, val in fields_stack:
    lines.append(info_line(label, val, y))
    y += lh

y += lh * 0.4
lines.append(f'<line x1="{INFO_X}" y1="{y-15}" x2="{INFO_X+INFO_W}" y2="{y-15}" stroke="#1c3a42" stroke-width="1"/>')
lines.append(f'<text x="{INFO_X}" y="{y+9}" class="section2">- Contact</text>')
y += lh + 9

fields_contact = [
    ("Grid Github", "github.com/LimaGost"),
    ("Grid LinkedIn", "linkedin.com/in/SEU-USUARIO"),
]
for label, val in fields_contact:
    lines.append(info_line(label, val, y, label_color="#e88fd6"))
    y += lh

y += lh * 0.3
lines.append(f'<line x1="{INFO_X}" y1="{y-8}" x2="{INFO_X+INFO_W}" y2="{y-8}" stroke="#1c3a42" stroke-width="1"/>')
lines.append(f'<text x="{INFO_X}" y="{y+14}" class="note">Live Stats</text>')
lines.append(f'<text x="{INFO_X}" y="{y+33}" class="note2">See live GitHub stats badges below in README &#8595;</text>')

y_final = y + 33
H = max(int(y_final) + 34, MAP_Y + MAP_H + 24)

info_svg = "\n    ".join(lines)

svg = f'''<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="'JetBrains Mono','Fira Code',Consolas,monospace">
  <defs>
    <style>
      .lbl {{ font-size: 12.5px; }}
      .dots {{ font-size: 12.5px; fill: #2a4a52; }}
      .val {{ font-size: 12.5px; fill: #d7ecef; }}
      .section {{ font-size: 13px; fill: #a08cf0; letter-spacing: 1px; font-weight: 700; }}
      .section2 {{ font-size: 12.5px; fill: #a08cf0; }}
      .prompt {{ font-size: 12.5px; fill: #4fd67a; }}
      .note {{ font-size: 11.5px; fill: #5a7a82; }}
      .note2 {{ font-size: 11px; fill: #3fd0e8; }}
      .title {{ font-size: 11.5px; fill: #5a7a82; }}
      .maplabel {{ font-size: 12px; fill: #5a7a82; letter-spacing: 1px; }}
    </style>
  </defs>

  <rect x="0" y="0" width="{W}" height="{H}" rx="10" fill="#0a1014" stroke="#1c3a42" stroke-width="1.5"/>

  <rect x="0" y="0" width="{W}" height="{TITLEBAR_H}" rx="10" fill="#0d1a1f"/>
  <rect x="0" y="{TITLEBAR_H-10}" width="{W}" height="10" fill="#0d1a1f"/>
  <circle cx="22" cy="{TITLEBAR_H/2}" r="6" fill="#ff5f57"/>
  <circle cx="42" cy="{TITLEBAR_H/2}" r="6" fill="#febc2e"/>
  <circle cx="62" cy="{TITLEBAR_H/2}" r="6" fill="#28c840"/>
  <text x="{W/2}" y="{TITLEBAR_H/2+4}" text-anchor="middle" class="title">lima@fullstack &#8226; ~ &#8226; $ ./profile.sh --live</text>
  <text x="{W-20}" y="{TITLEBAR_H/2+4}" text-anchor="end" class="title" fill="#3fd0e8">SCANNER</text>

  <text x="{MAP_X}" y="{MAP_Y-16}" class="maplabel">VISUAL.MAP</text>
  {circles_svg}

  <line x1="{MAP_X+MAP_W+20}" y1="{TITLEBAR_H+16}" x2="{MAP_X+MAP_W+20}" y2="{H-20}" stroke="#1c3a42" stroke-width="1"/>

  {info_svg}
</svg>'''

with open('/home/claude/profile-readme/assets/system-panel.svg', 'w') as f:
    f.write(svg)

print("SVG bytes:", len(svg), "H:", H)
