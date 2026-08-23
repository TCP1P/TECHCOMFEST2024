FROM python:3.11-bookworm

EXPOSE 80

RUN apt-get -qqy update && \
    apt-get -qqy --no-install-recommends install \
    qutebrowser xvfb cron && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/*
RUN pip install flask

COPY ./flag.txt /flag.txt
RUN mkdir -p /flag && mv /flag.txt /flag/`cat /proc/sys/kernel/random/uuid`.txt

RUN useradd ctf --create-home
ENV DISPLAY=:99

WORKDIR /app

COPY ./app /app/
RUN echo "#!/bin/sh\nrm -rf /tmp/*" > /cls
RUN crontab -l | { cat; echo "*/30 * * * * /cls"; } | crontab

CMD ["bash","-c","cron & Xvfb :99 -screen 0 640x400x8 -nolisten tcp & runuser -u ctf -- python /app/server.py"]

# RSCTF dynamic-flag compatibility layer. The build-time scan records
# exact marker-bearing files; runtime replacement is therefore bounded
# to those files instead of walking the image on every team start.
USER root
COPY rsctf-entrypoint.sh /usr/local/bin/rsctf-entrypoint
RUN set -eu; \
    chmod 0555 /usr/local/bin/rsctf-entrypoint; \
    : > /etc/rsctf-flag-targets; \
    for root in /app /src /srv /home /opt /var/www /challenge /chall /ctf /root /usr/src /usr/local/bin /workspace /flag /flag.txt; do \
      if [ -e "$root" ]; then \
        find "$root" -xdev -type f ! -path /usr/local/bin/rsctf-entrypoint -exec grep -lF -e RSCTF_DYNAMIC_FLAG_438cdf566d1b690998e25661fa731c -e RSCTF_DYNAMIC_FLAG_76e5ea5abe07e69a3d317 {} + >> /etc/rsctf-flag-targets 2>/dev/null || true; \
      fi; \
    done; \
    sort -u /etc/rsctf-flag-targets > /etc/rsctf-flag-targets.sorted; \
    mv /etc/rsctf-flag-targets.sorted /etc/rsctf-flag-targets; \
    while IFS= read -r target; do [ -f "$target" ] && chmod a+w "$target"; done < /etc/rsctf-flag-targets
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
