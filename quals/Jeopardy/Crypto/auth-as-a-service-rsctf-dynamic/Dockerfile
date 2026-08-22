FROM ubuntu:jammy
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y xinetd qemu-system-x86-64
RUN groupadd -r ctf && useradd -r -g ctf ctf

COPY qemu/bzImage /home/ctf/bzImage
COPY qemu/rootfs.cpio.gz /home/ctf/rootfs.cpio.gz
COPY qemu/run.sh /home/ctf/run.sh

RUN echo '#!/bin/bash\nservice xinetd restart && /bin/sleep infinity' > /etc/init.sh
RUN echo 'service ctf\n\
{\n\
    disable = no\n\
    socket_type = stream\n\
    protocol = tcp\n\
    wait = no\n\
    user = ctf\n\
    type = UNLISTED\n\
    port = 13337\n\
    bind = 0.0.0.0\n\
    server = /home/ctf/run.sh\n\
}' > /etc/xinetd.d/ctf

RUN chmod 400 /etc/xinetd.d/ctf
RUN chmod 444 /home/ctf/*
RUN chmod 550 /home/ctf/run.sh /etc/init.sh
RUN chmod 1733 /tmp /var/tmp /dev/shm
RUN chown -R root:ctf /home/ctf

RUN service xinetd restart
RUN apt-get update && apt-get install -y --no-install-recommends python3 gzip \
    && rm -rf /var/lib/apt/lists/*

# RSCTF dynamic-flag compatibility layer. The build-time scan records
# exact marker-bearing files; runtime replacement is therefore bounded
# to those files instead of walking the image on every team start.
USER root
COPY rsctf-entrypoint.sh /usr/local/bin/rsctf-entrypoint
COPY rsctf-prepare-flag.sh /usr/local/bin/rsctf-prepare-flag
RUN set -eu; \
    chmod 0555 /usr/local/bin/rsctf-entrypoint; \
    : > /etc/rsctf-flag-targets; \
    for root in /home/ctf/run.sh /home/ctf/rootfs.cpio.gz /home/ctf/bzImage /app /src /srv /home /opt /var/www /challenge /chall /ctf /root /usr/src /usr/local/bin /workspace /flag /flag.txt; do \
      if [ -e "$root" ]; then \
        find "$root" -xdev -type f ! -path /usr/local/bin/rsctf-entrypoint -exec grep -lF -e RSCTF_DYNAMIC_FLAG_b1a3e3f0001edd4ecce0886a -e RSCTF_DYNAMIC_FLAG_9f080088e6b68a6 {} + >> /etc/rsctf-flag-targets 2>/dev/null || true; \
      fi; \
    done; \
    sort -u /etc/rsctf-flag-targets > /etc/rsctf-flag-targets.sorted; \
    mv /etc/rsctf-flag-targets.sorted /etc/rsctf-flag-targets; \
    while IFS= read -r target; do [ -f "$target" ] && chmod a+w "$target"; done < /etc/rsctf-flag-targets; \
    chmod 0555 /usr/local/bin/rsctf-prepare-flag
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
