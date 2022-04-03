FROM prom/alertmanager

ENV ENVSUBST_VERSION="1.1.0"

USER root

RUN wget https://github.com/a8m/envsubst/releases/download/v${ENVSUBST_VERSION}/envsubst-Linux-x86_64 \
  && mkdir -p /usr/local/bin \
  && echo '10f957091859c04f62eeffbc6b23a29dc9c8c79721672c158f04a813144f4a12  envsubst-Linux-x86_64' | sha256sum -c \
  && mv envsubst-Linux-x86_64 /usr/local/bin/envsubst \
  && chmod +x /usr/local/bin/envsubst

COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh
USER nobody

ENTRYPOINT [ "/docker-entrypoint.sh" ]
CMD [ "/bin/alertmanager", \
  "--config.file=/etc/alertmanager/generated_config.yml", \
  "--storage.path=/alertmanager" ]