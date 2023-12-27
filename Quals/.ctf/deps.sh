export directories=$(find . -maxdepth 3 -type f \( -name "docker-compose.yaml" -o -name "docker-compose.yml" \) -exec dirname {} \; | sort -u)

process_directories() {
    IFS=$'\n'
    for dir in $directories; do
        if [[ "$dir" =~ \./\..* ]]; then
            continue
        fi

        echo "Processing directory: $dir"
        (
            cd "$dir"
            {
                bash -c "$1"
            }
        )&
    done

    wait
}
