while true; do
    ls -d pages/* \
          assets/* \
          sass/* \
          sass/core/* \
          sass/components/* \
          config.toml \
          template.mustache \
        | entr -d ./scripts/build.sh

    if [ $? -gt 2 ]; then
        break
    fi
done
