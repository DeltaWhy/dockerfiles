#!/bin/sh
set -e
echo "$SCHEDULE" /backup.sh ">/proc/1/fd/1 2>/proc/1/fd/2" > /etc/crontabs/root
exec crond -f
