FROM node:latest

EXPOSE 80

RUN apt-get -qqy update && \
    apt-get -qqy --no-install-recommends install \
    xvfb && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN useradd ctf --create-home
ENV DISPLAY=:99

WORKDIR /app

COPY ./ui/.next/standalone/ /app/
COPY ./ui/.next/static /app/.next/static

COPY ./src/dist/baby-electron-* /bin/baby-electron

CMD ["bash","-c","Xvfb :99 -screen 0 640x400x8 -nolisten tcp & runuser -u ctf -- node /app/server.js"]
