FROM ubuntu:jammy

RUN apt update && apt install socat -yq

WORKDIR /chall
COPY elffile /chall/elffile
RUN chmod 755 /chall/elffile
RUN echo "TCF2024{foren_pwn?_pengen_turu_aja_lah_capek_challnya_gajelas}" > /chall/flag.txt

RUN groupadd -r ctf && useradd -r -g ctf ctf
USER ctf

CMD ["/bin/bash","-c","exec socat -d TCP-LISTEN:20678,reuseaddr,fork EXEC:/chall/elffile"]
