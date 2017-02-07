# Api Crawler Challenge

## Objetivo

Desenvolver uma API que receba dois parametros:

1 - Uma url de um site qualquer

2 - Uma palavra qualquer

A API deve ser capaz de fazer um crawler no site informado e retornar uma resposta contendo um json com a quantidade de ocorrências da palavra informada.

## Versão

* Python 3.5.0
* Django==1.10.4


## Instalação

```bash
git clone https://github.com/rg3915/api_crawler_challenge.git
cd api_crawler_challenge
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/secret_gen.py
```

## Crawler

Temos um primeiro exemplo simples feito com Python puro. No terminal digite

```bash
python crawler.py -h
python crawler.py python.org Python
```

## Api Rest

```bash
python manage.py runserver
```

No Browser digite, por exemplo

```
localhost:8000/api/?url=python.org&w=Python
```

*pontotel*