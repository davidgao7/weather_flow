# Kafka Producers in Python

## example program to get data from firehose and send it to kafka

## how to setup environment

1. create virtual environment

```bash
pyenv install 3.12.4
```

2. set the local python version

```bash
pyenv local 3.12.4
```

3. create virtual environment with `venv`

```bash
pyenv exec python -m venv kafka_env
```

4. activate the virtual environment

```bash
source kafka_env/bin/activate
```

5. install the required packages

```bash
kafka_env/bin/pip3 install -r requirements.txt
```

## how to run

```bash
kafka env/bin/python3 stream.py
```
