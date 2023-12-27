FROM python:alpine

RUN apk add --no-cache socat
COPY app.py /app.py
RUN chmod 755 /app.py

CMD ["socat","TCP-LISTEN:42069,reuseaddr,fork", "EXEC:/app.py"]