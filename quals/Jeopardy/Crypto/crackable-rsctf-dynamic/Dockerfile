FROM python:alpine

RUN apk add --no-cache socat
COPY app.py /app.py
RUN chmod 755 /app.py

CMD ["socat","TCP-LISTEN:42069,reuseaddr,fork", "EXEC:/app.py"]

# RSCTF dynamic-flag compatibility layer. The build-time scan records
# exact marker-bearing files; runtime replacement is therefore bounded
# to those files instead of walking the image on every team start.
USER root
COPY rsctf-entrypoint.sh /usr/local/bin/rsctf-entrypoint
RUN set -eu; \
    chmod 0555 /usr/local/bin/rsctf-entrypoint; \
    : > /etc/rsctf-flag-targets; \
    for root in /app.py /app /src /srv /home /opt /var/www /challenge /chall /ctf /root /usr/src /usr/local/bin /workspace /flag /flag.txt; do \
      if [ -e "$root" ]; then \
        find "$root" -xdev -type f ! -path /usr/local/bin/rsctf-entrypoint -exec grep -lF -e RSCTF_DYNAMIC_FLAG_0a1b2df451ca8b38dd182c6cf440af91d0a10f07706fb96af9e431f51d4c06000a1b2df451ca8b38dd182c6cf4 -e RSCTF_DYNAMIC_FLAG_fc25aa3eed196c4ea0fd1a41deb47a75fa25d662d9da84bc197e601187da406ffc25aa3eed196c4ea {} + >> /etc/rsctf-flag-targets 2>/dev/null || true; \
      fi; \
    done; \
    sort -u /etc/rsctf-flag-targets > /etc/rsctf-flag-targets.sorted; \
    mv /etc/rsctf-flag-targets.sorted /etc/rsctf-flag-targets; \
    while IFS= read -r target; do [ -f "$target" ] && chmod a+w "$target"; done < /etc/rsctf-flag-targets
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
