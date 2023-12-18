FROM pwn.red/jail

COPY --from=ubuntu:jammy / /srv
RUN mkdir -p /srv/app && echo "TCF2024{asm(shellcraft.sh())}" > /srv/app/flag.txt
COPY chall /srv/app/run