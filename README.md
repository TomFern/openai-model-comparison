# Compare output of different OpenAI LLMs

## Setup

You will need an OpenAI API key. Source it from the `.env` file.

```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ cp env-example .env
$ nano .env
$ source .env
$ mkdir results
```

All output is stored in the `results` folders

## Get list of models

```bash
$ python models.py
```

## Test prompt for interesting models

```bash
$ python compare.py
```