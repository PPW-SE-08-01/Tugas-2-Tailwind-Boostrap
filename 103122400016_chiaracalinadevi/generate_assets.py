import os

def svg(out, name, bg1, bg2, body):
    os.makedirs(f"{out}/assets", exist_ok=True)
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{bg1}"/><stop offset="1" stop-color="{bg2}"/></linearGradient></defs><rect width="400" height="300" fill="url(#g)"/><circle cx="60" cy="50" r="6" fill="#fff" opacity=".7"/><circle cx="350" cy="90" r="9" fill="#fff" opacity=".6"/><circle cx="320" cy="250" r="5" fill="#fff" opacity=".7"/>{body}</svg>'''
    with open(f"{out}/assets/{name}.svg", "w", encoding="utf-8") as f:
        f.write(s)

def doll(x, dress, hair="#F6D58E", sc=1):
    return f'''<g transform="translate({x},0) scale({sc})"><ellipse cx="0" cy="105" rx="36" ry="62" fill="{hair}"/><rect x="-7" y="128" width="14" height="22" fill="#FBD5BF"/><circle cx="0" cy="105" r="28" fill="#FBD5BF"/><path d="M-30 98 Q0 55 30 98 Q10 80 -30 98Z" fill="{hair}"/><circle cx="-10" cy="106" r="3" fill="#5a3a3a"/><circle cx="10" cy="106" r="3" fill="#5a3a3a"/><path d="M-6 118 Q0 124 6 118" stroke="#E98FA8" stroke-width="3" fill="none" stroke-linecap="round"/><circle cx="-17" cy="115" r="5" fill="#F8B4C4" opacity=".7"/><circle cx="17" cy="115" r="5" fill="#F8B4C4" opacity=".7"/><path d="M-18 150 L18 150 L52 270 L-52 270Z" fill="{dress}"/><rect x="-14" y="148" width="28" height="14" fill="#fff" opacity=".35"/></g>'''

def generate(out):
    svg(out, "hero", "#FFE5D4", "#F8C8DC",
        doll(150, "#F29BB8", sc=1.05) + doll(255, "#FFB88C", hair="#8B5A3C", sc=.9) +
        '<path d="M330 40 l6 14 14 2 -10 10 3 14 -13 -7 -13 7 3 -14 -10 -10 14 -2z" fill="#fff" opacity=".8"/>')
    svg(out, "doll", "#FDE3EC", "#FFE8D6", doll(200, "#F29BB8"))
    svg(out, "outfit", "#FFE8D6", "#FBD3E0",
        '<path d="M200 60 L170 90 L185 100 L185 130 L130 250 L270 250 L215 130 L215 100 L230 90Z" fill="#F29BB8"/><path d="M185 130 L215 130" stroke="#fff" stroke-width="6"/><circle cx="200" cy="140" r="6" fill="#FFE5D4"/><path d="M185 100 Q200 118 215 100" fill="none" stroke="#fff" stroke-width="4"/>')
    svg(out, "house", "#FBD3E0", "#FFE5D4",
        '<rect x="90" y="130" width="220" height="130" fill="#FFF4EC"/><path d="M70 135 L200 55 L330 135Z" fill="#F29BB8"/><rect x="120" y="165" width="50" height="50" fill="#FFD3B8"/><rect x="230" y="165" width="50" height="50" fill="#FFD3B8"/><rect x="178" y="195" width="44" height="65" fill="#E98FA8"/><circle cx="214" cy="228" r="3" fill="#fff"/><path d="M200 38 l5 11 12 1 -9 8 3 12 -11 -6 -11 6 3 -12 -9 -8 12 -1z" fill="#fff"/>')
    svg(out, "car", "#FFE5D4", "#FBD3E0",
        '<path d="M70 190 L100 140 Q110 125 130 125 L260 125 Q285 125 298 150 L330 190 Z" fill="#F29BB8"/><rect x="55" y="180" width="290" height="45" rx="18" fill="#E98FA8"/><path d="M112 148 L132 140 L190 140 L190 180 L100 180Z" fill="#FFF4EC"/><path d="M200 140 L255 140 Q268 142 275 160 L282 180 L200 180Z" fill="#FFF4EC"/><circle cx="115" cy="228" r="26" fill="#6b4a55"/><circle cx="115" cy="228" r="11" fill="#FFE5D4"/><circle cx="290" cy="228" r="26" fill="#6b4a55"/><circle cx="290" cy="228" r="11" fill="#FFE5D4"/>')
    svg(out, "accessories", "#FDE3EC", "#FFE8D6",
        '<path d="M80 180 L115 130 L150 180 Q115 195 80 180Z" fill="#F29BB8"/><rect x="85" y="180" width="60" height="10" rx="4" fill="#fff"/><path d="M180 210 Q180 160 215 160 L255 190 L255 215 L180 215Z" fill="#FFB88C"/><path d="M180 215 L275 215" stroke="#E98FA8" stroke-width="6"/><rect x="215" y="120" width="70" height="42" rx="10" fill="#E98FA8"/><path d="M230 120 Q250 90 270 120" fill="none" stroke="#C86F88" stroke-width="6"/><circle cx="320" cy="140" r="26" fill="none" stroke="#FFD27F" stroke-width="7"/><circle cx="320" cy="114" r="9" fill="#F29BB8"/>')

generate("bootstrap-version")
generate("tailwind-version")
print("Selesai! Gambar dibuat di folder assets/ kedua versi.")