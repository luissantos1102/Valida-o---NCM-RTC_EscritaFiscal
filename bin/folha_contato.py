#!/usr/bin/env python3
"""Monta uma folha de contato dos slides, leve o bastante para anexar por e-mail.

Uso:
    python3 bin/folha_contato.py <pacote> [largura_total]

Gera <pacote>/criativo/folha-contato.png e o .b64 pronto para o campo
`attachments[].content` da ferramenta do Gmail.

Por que existe: a ferramenta de e-mail recebe o anexo como base64 dentro do
próprio argumento. Sete PNGs de 1080x1350 viram ~800 KB de base64 numa única
chamada — caro e sujeito a truncamento. Uma folha de contato dos mesmos sete
slides fica na casa das dezenas de KB, porque o design é de cores chapadas e o
PNG comprime bem. O usuário vê o carrossel inteiro no corpo do e-mail; os PNGs
em resolução cheia ficam no pacote commitado.
"""
import base64
import glob
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carrossel import chromium  # noqa: E402

LARGURA_PADRAO = 1600
COLUNAS = 4


def main():
    if not 2 <= len(sys.argv) <= 3:
        sys.exit(__doc__)
    pkg = os.path.abspath(sys.argv[1])
    largura = int(sys.argv[2]) if len(sys.argv) == 3 else LARGURA_PADRAO

    out = os.path.join(pkg, "criativo")
    slides = sorted(glob.glob(os.path.join(out, "slide-*.png")))
    if not slides:
        sys.exit(f"nenhum slide-*.png em {out} — rode bin/carrossel.py antes.")

    gap = 12
    pad = 16
    cel = (largura - 2 * pad - (COLUNAS - 1) * gap) // COLUNAS
    linhas = -(-len(slides) // COLUNAS)
    altura = 2 * pad + linhas * int(cel * 1350 / 1080) + (linhas - 1) * gap

    cards = "".join(
        f'<div class="c"><img src="file://{s}"><span>{i}</span></div>'
        for i, s in enumerate(slides, 1)
    )
    html = f"""<meta charset="utf-8"><style>
      *{{margin:0;padding:0;box-sizing:border-box}}
      body{{background:#0a1c18;padding:{pad}px;display:grid;
           grid-template-columns:repeat({COLUNAS},{cel}px);gap:{gap}px}}
      .c{{position:relative;line-height:0}}
      .c img{{width:{cel}px;display:block;border-radius:6px}}
      .c span{{position:absolute;right:6px;top:6px;background:#6FCF9F;color:#0E2A25;
              font:700 13px/1 Arial,sans-serif;padding:4px 7px;border-radius:4px}}
    </style>{cards}"""

    hp = os.path.join(out, "html", "folha-contato.html")
    os.makedirs(os.path.dirname(hp), exist_ok=True)
    open(hp, "w", encoding="utf-8").write(html)

    png = os.path.join(out, "folha-contato.png")
    subprocess.run([chromium(), "--headless", "--disable-gpu", "--no-sandbox",
                    "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={largura},{altura}",
                    f"--screenshot={png}", f"file://{hp}"],
                   check=True, capture_output=True)

    b64 = base64.b64encode(open(png, "rb").read()).decode()
    open(png + ".b64", "w").write(b64)

    kb, kb64 = os.path.getsize(png) / 1024, len(b64) / 1024
    print(f"{len(slides)} slides → folha-contato.png  {largura}x{altura}  {kb:.0f} KB")
    print(f"base64: {kb64:.0f} KB  →  {png}.b64")
    if kb64 > 400:
        print("\nAVISO: base64 acima de 400 KB. Rode de novo com uma largura menor,")
        print("       por exemplo: python3 bin/folha_contato.py <pacote> 900")
    print("\nOs PNGs em 1080x1350 seguem intactos no pacote — são eles que vão ao")
    print("LinkedIn. Esta folha serve só para a aprovação por e-mail.")


if __name__ == "__main__":
    main()
