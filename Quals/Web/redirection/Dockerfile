FROM python:alpine

RUN pip3 install requests flask gunicorn

WORKDIR /app
COPY ./src/app.py ./app.py

USER 1001

CMD [ "sh", "-c", "python3 -m gunicorn --bind 0.0.0.0:8080 -w 8 app:app" ]
