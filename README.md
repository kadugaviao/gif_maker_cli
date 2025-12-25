# 🎬 Meus Projetos Simples

Repositório com diversos projetos Python simples e úteis.

## 📁 Projetos

### [GIF Maker](./gifmaker-app/README.md)

Ferramenta CLI para criar GIFs animados a partir de imagens.

**Como usar:**

```bash
cd gifmaker-app
pip install -r requirements.txt
python3 create_gif.py img1.jpg img2.jpg --output animation.gif
```

---

## 🚀 Como começar

1. Clone o repositório

```bash
git clone <url>
cd gif
```

2. Para cada projeto, configure o ambiente:

```bash
cd gifmaker-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 📝 Estrutura

```
gif/
├── README.md (este arquivo)
├── .gitignore
└── gifmaker-app/
    ├── README.md
    ├── requirements.txt
    ├── create_gif.py
    ├── gifmaker/ (pacote Python)
    │   ├── __init__.py
    │   ├── cli.py
    │   ├── constants.py
    │   ├── gif_creator.py
    │   ├── image_processor.py
    │   └── validators.py
    └── images/
```
