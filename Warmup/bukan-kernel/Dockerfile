FROM alpine:3.15

WORKDIR /app
COPY ./app .

RUN apk add --no-cache python2 socat 
CMD ["socat", "TCP-LISTEN:1321,reuseaddr,fork,nodelay", "EXEC:'python2 /app/main.py',pty,ctty"]