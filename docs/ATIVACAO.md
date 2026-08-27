# Ativação — o que falta configurar na sua conta

Duas pendências, ambas resolvidas na **mesma tela**: a edição da Routine.
Nada disso está no código — é configuração da conta claude.ai.

Referências: [Routines](https://code.claude.com/docs/en/routines) ·
[Cloud environments](https://code.claude.com/docs/en/cloud-environments)

---

## Onde tudo acontece

1. Abra **https://claude.ai/code/routines**
2. Clique na Routine **"LinkedIn — Produção de Conteúdo (seg/qua 07:00)"**
3. Clique no **ícone de lápis** para abrir **Edit routine**

A partir daqui, as duas correções.

---

## Parte A — Conectores (o e-mail de aprovação)

Sem isso o pipeline produz o conteúdo e **não consegue enviar** o e-mail.

4. Role até **Connectors**, no fim do formulário
5. Garanta que **Gmail** está incluído
6. **Remova o que não for usado.** A documentação é explícita: durante a execução,
   Claude pode usar *qualquer* ferramenta de um conector incluído, **inclusive de
   escrita, sem pedir permissão**. Uma Routine autônoma não tem prompt de
   aprovação. Deixe só o necessário:

   | Conector | Incluir? | Por quê |
   |---|---|---|
   | **Gmail** | **Sim** | envia o e-mail de aprovação e lê a sua resposta |
   | **Jusratio** | Opcional | jurisprudência na etapa de pesquisa |
   | **Canva** | **Não** | o carrossel é gerado por `bin/carrossel.py`; o Canva não faz carrossel sem passo interativo |
   | Todos os outros | **Não** | superfície de escrita sem contrapartida |

> Conectores **não** precisam de liberação de rede: o tráfego deles passa pelos
> servidores da Anthropic, não pela rede da sessão. Por isso o Gmail funciona
> mesmo com a allowlist fechada.

---

## Parte B — Rede (a verificação em fonte primária)

Sem isso toda execução roda em **modo degradado** — funciona, mas sem abrir DOU,
Planalto, STF. Seu ambiente hoje é **"Luís Henrique"**, no nível **Trusted**, que
libera só registries de pacote, GitHub e SDKs de nuvem. Sites do governo brasileiro
não estão nessa lista — daí o `403`.

7. Ainda no **Edit routine**, logo abaixo da caixa **Instructions**, clique no
   **ícone de nuvem** com o nome do ambiente (**Luís Henrique**)
8. Passe o mouse sobre o ambiente na lista e clique no **ícone de engrenagem**
   que aparece à direita
9. No diálogo **Update cloud environment**, mude **Network access** de `Trusted`
   para **`Custom`**
10. Em **Allowed domains**, cole (um por linha):

```
*.gov.br
*.jus.br
*.conjur.com.br
*.jota.info
*.migalhas.com.br
*.contabeis.com.br
```

`*.gov.br` já cobre Planalto, DOU (in.gov.br), Receita Federal, CGIBS, Fazenda e
CONFAZ. `*.jus.br` cobre STF e STJ.

11. **Marque a caixa "Also include default list of common package managers".**
    Não pule este passo: sem ela, a allowlist passa a ser *só* a sua lista, e você
    perde npm, PyPI e `raw.githubusercontent.com`. Se usar artifacts neste
    ambiente, acrescente também `*.frame.claudeusercontent.com`.
12. Clique em **Save changes**

> O nível **Full** também resolveria, liberando qualquer domínio. `Custom` é
> preferível: a Routine roda sozinha, sem você olhando, e uma allowlist estreita
> limita o estrago se alguma página tentar levar a sessão para outro lugar.

---

## Fechar e testar

13. Salve a Routine
14. Na página de detalhe dela, clique em **Run now** para disparar fora do horário
15. Abra a sessão criada e confira as duas coisas:
    - o `bin/preflight.sh` deve imprimir **MODO=COMPLETO** (e não DEGRADADO)
    - o e-mail deve chegar em `luis.santos@copasul.coop.br`

Se o pré-voo ainda acusar bloqueio, o `Custom` não foi salvo ou a Routine ficou
apontada para outro ambiente. Se o e-mail não chegar, o Gmail não entrou nos
conectores.

> **Atenção ao status verde.** A documentação avisa: verde na lista de execuções
> significa apenas que a sessão iniciou e terminou sem erro de infraestrutura —
> **não** que a tarefa deu certo. Abra a execução e leia. Requisição de rede
> bloqueada e ferramenta de conector ausente aparecem lá dentro, não no indicador.

---

## Depois de ativado

A partir do primeiro disparo real (**segunda, 31/08, às 7h**), o ciclo é:

produção → e-mail para você → sua resposta (`APROVADO` / `REFAZER`) →
publicação agendada para 17:30 do dia seguinte.

Para pausar sem perder a configuração: use o botão na seção **Repeats** da página
de detalhe da Routine.
