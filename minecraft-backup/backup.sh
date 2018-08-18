#!/bin/sh
set -e
cleanup() {
	rcon-cli save-on
}
trap cleanup EXIT

rcon-cli save-off
rcon-cli save-all
rsync --delete -a --progress /data/world /backups
