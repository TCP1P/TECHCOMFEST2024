FROM ubuntu:jammy
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -yq xinetd git gcc make python3
RUN groupadd -r ctf && useradd -r -g ctf ctf

WORKDIR /home/ctf

# clone and build minivm pure from github
RUN git clone https://github.com/FastVM/minivm.git --recursive && \
    cd minivm && \
    git submodule update --init && \
    # make it fast
    make -Bj OPT='-O3 -flto'

RUN echo '#!/bin/bash\nservice xinetd restart && /bin/sleep infinity' > /etc/init.sh
RUN echo 'service ctf\n\
{\n\
    disable = no\n\
    socket_type = stream\n\
    protocol = tcp\n\
    wait = no\n\
    user = ctf\n\
    type = UNLISTED\n\
    port = 31337\n\
    bind = 0.0.0.0\n\
    server = /home/ctf/run.py\n\
}' > /etc/xinetd.d/ctf

COPY run.py /home/ctf/run.py
RUN echo 'RSCTF_DYNAMIC_FLAG_4696a6b9e1f891934247aa217288c' > /home/ctf/flag.txt

RUN chmod 400 /etc/xinetd.d/ctf
RUN chmod 550 /home/ctf/run.py /etc/init.sh
RUN chmod 1733 /tmp /var/tmp /dev/shm
RUN chown -R ctf:ctf /home/ctf

RUN service xinetd restart

# RSCTF dynamic-flag compatibility layer. The build-time scan records
# exact marker-bearing files; runtime replacement is therefore bounded
# to those files instead of walking the image on every team start.
USER root
COPY rsctf-entrypoint.sh /usr/local/bin/rsctf-entrypoint
RUN set -eu; \
    chmod 0555 /usr/local/bin/rsctf-entrypoint; \
    : > /etc/rsctf-flag-targets; \
    for root in /home/ctf/run.py /home/ctf /app /src /srv /home /opt /var/www /challenge /chall /ctf /root /usr/src /usr/local/bin /workspace /flag /flag.txt; do \
      if [ -e "$root" ]; then \
        find "$root" -xdev -type f ! -path /usr/local/bin/rsctf-entrypoint -exec grep -lF -e RSCTF_DYNAMIC_FLAG_4696a6b9e1f891934247aa217288c -e RSCTF_DYNAMIC_FLAG_ad20a2435b18e3c8bfce {} + >> /etc/rsctf-flag-targets 2>/dev/null || true; \
      fi; \
    done; \
    sort -u /etc/rsctf-flag-targets > /etc/rsctf-flag-targets.sorted; \
    mv /etc/rsctf-flag-targets.sorted /etc/rsctf-flag-targets; \
    while IFS= read -r target; do [ -f "$target" ] && chmod a+w "$target"; done < /etc/rsctf-flag-targets
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
