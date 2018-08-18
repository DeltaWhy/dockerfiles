#!/bin/sh
set -e
echo "$SCHEDULE" /backup.sh > /crontab
exec devcron /crontab
