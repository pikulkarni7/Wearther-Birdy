FROM --platform=$BUILDPLATFORM python:3.9-alpine AS builder

WORKDIR /app 

RUN pip3 install gunicorn

COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app 

ENTRYPOINT ["gunicorn"] 

EXPOSE 8000

CMD ["Birdy.wsgi:application", "--bind", "0.0.0.0:8000"]