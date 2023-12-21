FROM pwn.red/jail

COPY --from=ubuntu:jammy / /srv
RUN mkdir -p /srv/app && echo "TCF2024{foren_pwn?_pengen_turu_aja_lah_capek_challnya_gajelas}" > /srv/app/flag.txt
COPY elffile /srv/app/run
