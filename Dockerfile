FROM python:3.7.4-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

CMD python ./ttn_tb_connector.py