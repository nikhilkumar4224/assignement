FROM python:3.8-slim@sha256:322e38e3056cf87280ad80be615a6282aae768090f30d43d99abe413e1dd081a

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

RUN pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

COPY . /app/