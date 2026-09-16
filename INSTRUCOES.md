# Como aplicar no seu perfil (LimaGost/LimaGost)

## 1. Estrutura de arquivos
Copie esta estrutura para dentro do repositório `LimaGost/LimaGost` (o repo especial
que vira o README do seu perfil):

```
LimaGost/
├── assets/
│   └── system-panel.svg
├── .github/
│   └── workflows/
│       └── snake.yml
└── README.md
```

Se você já tem um README.md no repo, adapte-o em vez de sobrescrever — pode manter
suas seções extras (ex: badges de stats) abaixo do bloco do snake.

## 2. Ajuste antes de commitar
No arquivo `assets/system-panel.svg`, troque:
- `linkedin.com/in/SEU-USUARIO` → seu link real do LinkedIn (não me passou ainda)

Se algum dado mudar (cargo, stack, formação), edite `scripts/build_svg.py` e rode
de novo (veja passo 4) em vez de editar o SVG na mão — assim fica fácil manter
atualizado no futuro.

## 3. Habilite Actions no repositório
Vá em Settings → Actions → General e confirme que "Allow all actions" está ativo.
Depois, em Settings → Actions → General → Workflow permissions, marque
"Read and write permissions" (o snake precisa criar o branch `output`).

## 4. Rodando o gerador do painel localmente (Python)
Só necessário se quiser mudar algum dado do painel:

```bash
pip install shapely
python3 scripts/gen_map.py     # baixa o contorno do Brasil e gera scripts/dots.json
python3 scripts/build_svg.py   # monta assets/system-panel.svg a partir dos dados
```

Edite as listas `fields_top`, `fields_stack` e `fields_contact` dentro de
`build_svg.py` para atualizar as informações exibidas.

## 5. Primeiro disparo do snake
Depois do primeiro push na branch `main`, vá em Actions → "generate contribution
snake" → Run workflow (ou espere o push disparar sozinho). Ele cria o branch
`output` com `snake.svg` e `snake-dark.svg`, que o README já referencia.

## 6. O que é orgânico e não dá pra "copiar"
- Selos de **Achievements** (Pull Shark, YOLO, etc.) vêm do seu uso real do GitHub
  (PRs, merges) — aparecem sozinhos conforme você usa a plataforma.
- Contador de **seguidores** é do perfil nativo, cresce com o tempo/rede.
