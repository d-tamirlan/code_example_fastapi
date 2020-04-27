FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /project

WORKDIR /project

COPY requirements.txt /project/

RUN pip install -r requirements.txt

COPY . /project/

CMD uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
