#!/bin/sh
set -e

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source "${script_dir}/deps.sh"

process_directories 'sed -i "s/\(state:\s*\).*/\1hidden/" "./challenge.yml"'
