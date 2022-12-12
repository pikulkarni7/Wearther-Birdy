FROM python:3.9 AS builder

WORKDIR /app 

RUN apt update
RUN apt install libgeos-dev -y

COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
RUN pip3 install gunicorn

COPY . /app 

EXPOSE 8000

CMD ["gunicorn", "Birdy.wsgi:application", "--bind", "0.0.0.0:8000"]
