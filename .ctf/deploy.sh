#!/bin/sh
set -e

source "./functions.sh"

process_directories "sudo COMPOSE_HTTP_TIMEOUT=999999 docker-compose --compatibility up --build --detach"

