FROM python:3.8

RUN mkdir /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/

CMD ["python3", "app.py"]

