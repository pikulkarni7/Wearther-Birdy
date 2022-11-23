FROM --platform=$BUILDPLATFORM python:3.9-slim AS builder

WORKDIR /app 

RUN pip3 install gunicorn

COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app 

EXPOSE 8000

CMD ["gunicorn", "Birdy.wsgi:application", "--bind", "0.0.0.0:8000"]
