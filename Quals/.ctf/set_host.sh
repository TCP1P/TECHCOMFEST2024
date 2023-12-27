#!/bin/sh
set -e

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 $1"
    exit 1
fi

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source "${script_dir}/deps.sh"

process_directories 'sed -i -E "s|(connection_info:\s*http://)localhost|\1'$1'|" "./challenge.yml"'
