FROM ubuntu:jammy

RUN apt update && apt install socat -yq

WORKDIR /chall
COPY pwnable /chall/pwnable
RUN echo "RSCTF_DYNAMIC_FLAG_cead7f1fd232c8fba835ac9ba78ee12d7f781e8ed53a6" > /chall/flag.txt

RUN groupadd -r ctf && useradd -r -g ctf ctf
USER ctf

CMD ["/bin/bash", "-c", "exec socat -d TCP-LISTEN:23337,reuseaddr,fork EXEC:/chall/pwnable"]

# RSCTF dynamic-flag compatibility layer. The build-time scan records
# exact marker-bearing files; runtime replacement is therefore bounded
# to those files instead of walking the image on every team start.
USER root
COPY rsctf-entrypoint.sh /usr/local/bin/rsctf-entrypoint
RUN set -eu; \
    chmod 0555 /usr/local/bin/rsctf-entrypoint; \
    : > /etc/rsctf-flag-targets; \
    for root in /chall/pwnable /app /src /srv /home /opt /var/www /challenge /chall /ctf /root /usr/src /usr/local/bin /workspace /flag /flag.txt; do \
      if [ -e "$root" ]; then \
        find "$root" -xdev -type f ! -path /usr/local/bin/rsctf-entrypoint -exec grep -lF -e RSCTF_DYNAMIC_FLAG_cead7f1fd232c8fba835ac9ba78ee12d7f781e8ed53a6 -e RSCTF_DYNAMIC_FLAG_68e0468dd85934dc9dd43748946161b6cbdb {} + >> /etc/rsctf-flag-targets 2>/dev/null || true; \
      fi; \
    done; \
    sort -u /etc/rsctf-flag-targets > /etc/rsctf-flag-targets.sorted; \
    mv /etc/rsctf-flag-targets.sorted /etc/rsctf-flag-targets; \
    while IFS= read -r target; do [ -f "$target" ] && chmod a+w "$target"; done < /etc/rsctf-flag-targets
USER ctf
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
