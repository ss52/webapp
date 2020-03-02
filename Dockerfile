FROM python:3.7

COPY ./app /code/app
COPY ./microblog.py /code
COPY ./requirements.txt /code

WORKDIR /code

RUN pip install --no-cache-dir -r requirements.txt