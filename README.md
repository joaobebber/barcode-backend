# Versão das ferramentas

- Python 3.11.3
- pip 22.3.1
- git 2.40.0

# Como executar o servidor

```bash
  python3 run.py
```

## Criar e ativar o ambiente virtual

```bash
  python3 -m venv .venv && source .venv/bin/activate
```

## Configurar o pylint

```bash
  pip3 install pylint && pylint --generate-rcfile > .pylintrc
```

## Configurar o pre-commit

- Lembre de criar o arquivo .pre-commit-config.yaml antes da instalação

```bash
  pip3 install pre-commit && pre-commit install
```

## Instalar as demais dependências

```bash
  pip3 install flask python-barcode pillow 
```

## Salvar as dependências e suas versões

```bash
  .venv/bin/pip3 freeze > requirements.txt
```
