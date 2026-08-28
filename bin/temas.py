#!/usr/bin/env python3
"""Paleta e templates visuais do carrossel.

A identidade se mantém pela **paleta, tipografia e assinatura** — constantes em
toda publicação. O que varia é o **template**, escolhido conforme a natureza do
conteúdo. Isso evita as duas armadilhas opostas: um feed onde todo post é
idêntico (o leitor para de ver) e um feed sem identidade (o leitor não reconhece
o autor).
"""

# Paleta única — marinho profundo com acento âmbar. Não muda entre templates.
CORES = {
    "fundo":      "#0B1B2E",
    "superficie": "#152B44",
    "borda":      "#22405F",
    "texto":      "#F2F5F8",
    "secundario": "#A9BACB",
    "acento":     "#D6A544",
    "sutil":      "#5A7characteristic",
}
CORES["sutil"] = "#5A7590"

SERIFA = '"Bitstream Charter","DejaVu Serif",Georgia,serif'
SANS = '"DejaVu Sans","Liberation Sans",Arial,sans-serif'

TEMPLATES = {
    # Análise doutrinária, tese que se desenvolve em prosa.
    "editorial": {
        "titulo_fonte": SERIFA,
        "titulo_peso": "700",
        "capa_tamanho": "84px",
        "capa_espaco": "-0.015em",
        "h2_tamanho": "56px",
        "corpo_fonte": SANS,
        "corpo_tamanho": "37px",
        "kicker_estilo": "letter-spacing:.18em;font-size:24px",
        "regua": "largura:150px;altura:3px",
    },
    # Prazos, percentuais, comparação de regimes: números que falam sozinhos.
    "dossie": {
        "titulo_fonte": SANS,
        "titulo_peso": "800",
        "capa_tamanho": "74px",
        "capa_espaco": "-0.02em",
        "h2_tamanho": "50px",
        "corpo_fonte": SANS,
        "corpo_tamanho": "35px",
        "kicker_estilo": "letter-spacing:.14em;font-size:25px",
        "regua": "largura:100%;altura:2px",
    },
    # Uma tese única e forte, pouquíssimo texto.
    "tese": {
        "titulo_fonte": SERIFA,
        "titulo_peso": "700",
        "capa_tamanho": "104px",
        "capa_espaco": "-0.025em",
        "h2_tamanho": "68px",
        "corpo_fonte": SANS,
        "corpo_tamanho": "40px",
        "kicker_estilo": "letter-spacing:.2em;font-size:23px",
        "regua": "largura:64px;altura:6px",
    },
}

ASSINATURA = ["Luis Santos", "Direito Tributário, Empresarial e Contratual"]


def css(template):
    t = TEMPLATES[template]
    c = CORES
    lw, lh = [x.split(":")[1] for x in t["regua"].split(";")]
    return f"""
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px}}
body{{background:{c['fundo']};color:{c['texto']};font-family:{t['corpo_fonte']};
     padding:86px 82px;display:flex;flex-direction:column;position:relative;
     overflow:hidden}}
.kicker{{{t['kicker_estilo']};text-transform:uppercase;color:{c['acento']};
        font-weight:700;font-family:{SANS}}}
h1{{font-family:{t['titulo_fonte']};font-weight:{t['titulo_peso']};
   font-size:{t['capa_tamanho']};line-height:1.08;letter-spacing:{t['capa_espaco']}}}
h2{{font-family:{t['titulo_fonte']};font-weight:{t['titulo_peso']};
   font-size:{t['h2_tamanho']};line-height:1.16;letter-spacing:-.01em}}
p{{font-size:{t['corpo_tamanho']};line-height:1.46;color:{c['secundario']};text-align:justify}}
p + p{{margin-top:30px}}
.hi{{color:{c['acento']};font-weight:700}}
.grow{{flex:1}}
.gap{{height:38px}}
.rule{{width:{lw};height:{lh};background:{c['acento']}}}
.num{{position:absolute;right:82px;bottom:40px;font-size:23px;color:{c['sutil']};
     font-weight:700;font-family:{SANS}}}
.sig{{font-size:25px;line-height:1.5;color:{c['sutil']};font-weight:600;
     font-family:{SANS}}}
.box{{background:{c['superficie']};border:1px solid {c['borda']};
     border-left:5px solid {c['acento']};border-radius:10px;padding:34px 38px}}
.box + .box{{margin-top:26px}}
.box .lab{{font-size:25px;color:{c['acento']};font-weight:700;letter-spacing:.06em;
          text-transform:uppercase;margin-bottom:12px;font-family:{SANS}}}
.box .val{{font-size:34px;line-height:1.34;color:{c['texto']}}}
ol{{list-style:none;counter-reset:i}}
ol li{{counter-increment:i;font-size:36px;line-height:1.4;color:{c['secundario']};
      padding-left:78px;position:relative}}
ol li + li{{margin-top:34px}}
ol li::before{{content:counter(i);position:absolute;left:0;top:-2px;width:52px;
      height:52px;border-radius:26px;border:2px solid {c['acento']};
      color:{c['acento']};font:700 28px/1 {SANS};display:flex;
      align-items:center;justify-content:center}}
.dados{{display:grid;grid-template-columns:1fr 1fr;gap:22px}}
.dado{{background:{c['superficie']};border:1px solid {c['borda']};border-radius:10px;
      padding:30px 32px}}
.dado .n{{font-family:{t['titulo_fonte']};font-size:56px;font-weight:700;
         color:{c['acento']};line-height:1}}
.dado .d{{font-size:26px;color:{c['secundario']};margin-top:12px;line-height:1.3}}
.faixa{{position:absolute;left:0;right:0;height:10px;background:{c['acento']}}}
.faixa.top{{top:0}} .faixa.bot{{bottom:0}}
"""
