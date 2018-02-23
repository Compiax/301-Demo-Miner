FROM python:3.6.4-slim-stretch

WORKDIR /

COPY . .

CMD ["python3", "miner.py"]
