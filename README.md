# Birdy
This is the backend for Wearther - Application that suggests outfit based on current weather
Built using Django

(Mar 2023) Added user subscriptions and SMS notifications for this service, by linking this to another microservice - Cage. Check it out here
[github.com/pikulkarni7/cage/tree/dev](https://github.com/pikulkarni7/cage/tree/dev)
## Installation and Instructions
After cloning the repository, open terminal inside the current directory

```bash
$ cd Birdy
```
Activate virtual environment
```bash
$ ./env/Scripts/Activate
```
Install requirements
```bash
$ pip install -r requirements.txt
```
Install database migrations
```bash
$ python manage.py migrate
```
Run backend server locally
```bash
$ python manage.py runserver
```

