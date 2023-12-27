FROM ubuntu:jammy

RUN apt update && apt install socat -yq

WORKDIR /chall
COPY pwnable /chall/pwnable
RUN echo "TCF2024{dah_gede_masa_cuma_overwrite_variable_aja_pake_pwntools}" > /chall/flag.txt

RUN groupadd -r ctf && useradd -r -g ctf ctf
USER ctf

CMD ["/bin/bash", "-c", "exec socat -d TCP-LISTEN:23337,reuseaddr,fork EXEC:/chall/pwnable"]