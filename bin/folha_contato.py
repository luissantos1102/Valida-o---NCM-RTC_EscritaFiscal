#!/usr/bin/env python3
"""Monta uma folha de contato dos slides: os sete numa imagem só.

Uso:
    python3 bin/folha_contato.py <pacote> [largura_total] [--b64]

Gera <pacote>/criativo/folha-contato.png. Ela é commitada junto com o pacote e
**linkada** no e-mail de aprovação — um clique, e o usuário vê o carrossel
inteiro em resolução cheia no GitHub.

Por que NÃO anexamos: a ferramenta de e-mail recebe anexo como base64 dentro do
próprio argumento, o que obriga o conteúdo a passar pelo contexto do modelo. Uma
folha de 1600 px custa ~96 mil tokens numa execução de ~197 mil — metade do
gasto, para exibir na tela do e-mail algo que já está commitado e linkável por
algumas dezenas de tokens.

`--b64` gera o .b64 mesmo assim, para quando o usuário pedir anexo de verdade.
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
    args = [a for a in sys.argv[1:] if a != "--b64"]
    quer_b64 = "--b64" in sys.argv
    if not 1 <= len(args) <= 2:
        sys.exit(__doc__)
    pkg = os.path.abspath(args[0])
    largura = int(args[1]) if len(args) == 2 else LARGURA_PADRAO

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

    kb = os.path.getsize(png) / 1024
    print(f"{len(slides)} slides → folha-contato.png  {largura}x{altura}  {kb:.0f} KB")

    if quer_b64:
        b64 = base64.b64encode(open(png, "rb").read()).decode()
        open(png + ".b64", "w").write(b64)
        kb64 = len(b64) / 1024
        print(f"base64: {kb64:.0f} KB (~{kb64 * 1024 / 3.5 / 1000:.0f}k tokens) → {png}.b64")
        print("Lembre: anexar faz esse conteúdo passar pelo contexto. Prefira o link.")

    print("\nCommite e linke no e-mail. Os PNGs em 1080x1350 seguem intactos no")
    print("pacote — são eles que vão ao LinkedIn.")


if __name__ == "__main__":
    main()
