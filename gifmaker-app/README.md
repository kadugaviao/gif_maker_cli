# GIF Maker

Ferramenta CLI para criar GIFs animados a partir de suas imagens.

## Setup

1. Clone e entre no diretório;

```bash
git clone <url-do-repositorio>
cd gifMaker
```

2. Crie e ative o ambiente virtual;

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências;

```bash
pip install -r requirements.txt
```

## Uso rápido

De arquivos específicos:

```bash
python3 create_gif.py img1.jpg img2.jpg img3.jpg --output animation.gif
```

De uma pasta:

```bash
python3 create_gif.py --folder images/ --output slideshow.gif
```

Apenas PNGs da pasta:

```bash
python3 create_gif.py --folder images/ --pattern "*.png" --output slideshow.gif
```

Com configurações personalizadas:

```bash
python3 create_gif.py img1.jpg img2.jpg --output fast.gif --duration 100 --loop 5
```

## Opções disponíveis

| Opção        | Curto | O que é                   | Padrão |
| ------------ | ----- | ------------------------- | ------ |
| `images`     | -     | Arquivos de imagem        | -      |
| `--folder`   | `-f`  | Pasta com imagens         | -      |
| `--pattern`  | `-p`  | Filtro (ex: `*.jpg`)      | `*`    |
| `--output`   | `-o`  | Nome do GIF (obrigatório) | -      |
| `--duration` | `-d`  | Ms por frame              | 500    |
| `--loop`     | `-l`  | Repetições (0 = infinito) | 0      |

## Formatos suportados

JPEG, PNG, BMP, GIF, TIFF, WebP

## Exemplos

```bash
python3 create_gif.py screenshot1.png screenshot2.png screenshot3.png -o demo.gif
python3 create_gif.py -f fotos/ -p "*.jpg" -o viagem.gif -d 200
python3 create_gif.py frame01.png frame02.png frame03.png -o anim.gif -d 750 -l 3
```

## Arquitetura

```
gifmaker/
├── constants.py       # Configurações
├── validators.py      # Validação de arquivos
├── image_processor.py # Carregamento
├── gif_creator.py     # Criação do GIF
└── cli.py             # Interface
```
