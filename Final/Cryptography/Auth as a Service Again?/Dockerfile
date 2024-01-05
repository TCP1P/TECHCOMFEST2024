FROM python:alpine

RUN apk add --no-cache socat
RUN pip install sympy pycryptodome==3.16.0
COPY auth.py /auth.py

CMD socat TCP-LISTEN:21337,fork,reuseaddr EXEC:"python3 auth.py"