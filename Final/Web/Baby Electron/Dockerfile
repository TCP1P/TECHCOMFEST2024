FROM node:latest

ENV XDG_CURRENT_DESKTOP XFCE

RUN apt-get -qqy update
RUN apt-get -qqy --no-install-recommends install libfuse2 libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libgtk-3-dev libasound2 libgbm1 fuse ca-certificates
RUN apt-get -qqy --no-install-recommends install xvfb
RUN apt-get -qqy --no-install-recommends install xfce4
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN useradd ctf --create-home
ENV DISPLAY=:0

WORKDIR /app

COPY ./ui/.next/standalone/ /app/
COPY ./ui/.next/static /app/.next/static

COPY ./src/dist/baby-electron-* /bin/baby-electron

COPY ./flag.txt /root/flag.txt
COPY ./readflag /readflag
RUN chmod u+s /readflag

EXPOSE 3000
CMD ["bash","-c","Xvfb :0 -screen 0 640x400x8 -nolisten tcp & runuser -u ctf -- node /app/server.js"]
