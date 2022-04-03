#!/bin/ash

/usr/local/bin/envsubst < /etc/alertmanager/alertmanager.yml > /etc/alertmanager/generated_config.yml
exec "$@"