#!/usr/bin/env python3
"""Gera o carrossel do LinkedIn a partir de um roteiro JSON.

Uso:
    python3 bin/carrossel.py <pacote>

<pacote> é o diretório da publicação, que deve conter `roteiro.json`.
Saída: <pacote>/criativo/slide-NN.png em 1080x1350, e os HTML em criativo/html/.

Formato do roteiro.json — ver bin/roteiro.exemplo.json. Em qualquer campo de
texto, **assim** vira destaque na cor de realce.

Tipos de slide:
  capa        kicker, titulo, fonte, destaque
  texto       kicker, titulo (opcional), corpo (lista de parágrafos)
  comparativo kicker, blocos [{lab, val}], rodape (opcional)
  lista       kicker, titulo (opcional), itens (lista, numerada)
  fecho       kicker, titulo, assinatura (lista de 2 linhas)
"""
import html
import json
import os
import re
import shutil
import subprocess
import sys

W, H = 1080, 1350

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px}
body{background:#0E2A25;color:#F4F7F5;
     font-family:"DejaVu Sans","Liberation Sans",Arial,sans-serif;
     padding:88px 84px;display:flex;flex-direction:column;
     position:relative;overflow:hidden}
.kicker{font-size:26px;letter-spacing:.16em;text-transform:uppercase;
        color:#6FCF9F;font-weight:700}
h1{font-size:82px;line-height:1.07;font-weight:800;letter-spacing:-.02em}
h2{font-size:58px;line-height:1.13;font-weight:800;letter-spacing:-.01em}
p{font-size:38px;line-height:1.45;color:#D7E2DC}
p + p{margin-top:32px}
.hi{color:#6FCF9F;font-weight:700}
.grow{flex:1}
.rule{width:120px;height:8px;background:#6FCF9F;border-radius:4px}
.num{position:absolute;right:84px;bottom:40px;font-size:24px;color:#4A655C;
     font-weight:700}
.sig{font-size:26px;line-height:1.5;color:#8FA79D;font-weight:600}
.box{background:#153A33;border-left:8px solid #6FCF9F;border-radius:12px;
     padding:36px 42px}
.box + .box{margin-top:30px}
.box .lab{font-size:27px;color:#6FCF9F;font-weight:700;letter-spacing:.06em;
          text-transform:uppercase;margin-bottom:14px}
.box .val{font-size:35px;line-height:1.35;color:#F4F7F5}
ol{list-style:none;counter-reset:i}
ol li{counter-increment:i;font-size:37px;line-height:1.4;color:#D7E2DC;
      padding-left:82px;position:relative}
ol li + li{margin-top:38px}
ol li::before{content:counter(i);position:absolute;left:0;top:-2px;
      width:56px;height:56px;border-radius:28px;background:#6FCF9F;color:#0E2A25;
      font-size:32px;font-weight:800;display:flex;align-items:center;
      justify-content:center}
.gap{height:40px}
"""


def rich(text):
    """Escapa HTML e converte **destaque** em span de realce."""
    return re.sub(r"\*\*(.+?)\*\*", r'<span class="hi">\1</span>',
                  html.escape(text or ""))


def render(slide, idx, total):
    t = slide.get("tipo", "texto")
    out = []
    if slide.get("kicker"):
        out.append(f'<div class="kicker">{rich(slide["kicker"])}</div>')
        out.append('<div class="gap"></div>')

    if t == "capa":
        out.append(f'<h1>{rich(slide["titulo"])}</h1>')
        out.append('<div class="gap"></div><div class="rule"></div>')
        out.append('<div class="grow"></div>')
        pe = []
        if slide.get("fonte"):
            pe.append(rich(slide["fonte"]))
        if slide.get("destaque"):
            pe.append(f'<span class="hi">{rich(slide["destaque"])}</span>')
        if pe:
            out.append("<p>" + "<br>".join(pe) + "</p>")

    elif t == "comparativo":
        for b in slide.get("blocos", []):
            val = "<br>".join(rich(v) for v in str(b["val"]).split("\n"))
            out.append(f'<div class="box"><div class="lab">{rich(b["lab"])}</div>'
                       f'<div class="val">{val}</div></div>')
        if slide.get("rodape"):
            out.append('<div class="gap"></div>')
            out.append(f'<p>{rich(slide["rodape"])}</p>')
        out.append('<div class="grow"></div>')

    elif t == "lista":
        if slide.get("titulo"):
            out.append(f'<h2>{rich(slide["titulo"])}</h2><div class="gap"></div>')
        out.append("<ol>" + "".join(f"<li>{rich(i)}</li>"
                                    for i in slide.get("itens", [])) + "</ol>")
        out.append('<div class="grow"></div>')

    elif t == "fecho":
        out.append(f'<h2>{rich(slide["titulo"])}</h2>')
        out.append('<div class="grow"></div><div class="rule"></div>'
                   '<div class="gap"></div>')
        sig = slide.get("assinatura", [])
        out.append('<div class="sig">' + "<br>".join(rich(s) for s in sig)
                   + "</div>")

    else:  # texto
        if slide.get("titulo"):
            out.append(f'<h2>{rich(slide["titulo"])}</h2>')
            out.append('<div class="gap"></div>')
        for par in slide.get("corpo", []):
            out.append(f"<p>{rich(par)}</p>")
        out.append('<div class="grow"></div>')

    if idx > 1:
        out.append(f'<div class="num">{idx}/{total}</div>')
    return f'<meta charset="utf-8"><style>{CSS}</style>' + "".join(out)


def chromium():
    for root, _, files in os.walk("/opt/pw-browsers"):
        for name in ("headless_shell", "chrome"):
            if name in files:
                return os.path.join(root, name)
    for name in ("chromium", "chromium-browser", "google-chrome"):
        found = shutil.which(name)
        if found:
            return found
    sys.exit("Chromium não encontrado. Instale-o ou ajuste bin/carrossel.py.")


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    pkg = os.path.abspath(sys.argv[1])
    roteiro = os.path.join(pkg, "roteiro.json")
    if not os.path.exists(roteiro):
        sys.exit(f"roteiro.json não encontrado em {pkg}")

    slides = json.load(open(roteiro, encoding="utf-8"))["slides"]
    if not 5 <= len(slides) <= 8:
        print(f"aviso: {len(slides)} slides — o protocolo pede de 5 a 8.")

    out = os.path.join(pkg, "criativo")
    htmldir = os.path.join(out, "html")
    os.makedirs(htmldir, exist_ok=True)
    binary = chromium()

    for i, s in enumerate(slides, 1):
        hp = os.path.join(htmldir, f"slide-{i:02d}.html")
        pp = os.path.join(out, f"slide-{i:02d}.png")
        open(hp, "w", encoding="utf-8").write(render(s, i, len(slides)))
        subprocess.run([binary, "--headless", "--disable-gpu", "--no-sandbox",
                        "--hide-scrollbars", "--force-device-scale-factor=1",
                        f"--window-size={W},{H}", f"--screenshot={pp}",
                        f"file://{hp}"],
                       check=True, capture_output=True)
        print(f"slide-{i:02d}.png  ({s.get('tipo', 'texto')})")

    print(f"\n{len(slides)} slides em {W}x{H} → {out}")
    print("Confira ao menos a capa e o slide mais denso antes de enviar.")


if __name__ == "__main__":
    main()
