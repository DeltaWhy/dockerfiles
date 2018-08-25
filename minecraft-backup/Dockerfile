FROM alpine
ENV RCON_HOST=minecraft
ENV RCON_PORT=25575
ENV RCON_PASSWORD=minecraft
ENV BACKUP_SRC=/data/world
ENV BACKUP_DEST=/backups/
ENV SCHEDULE="0 0 * * *"
RUN apk add --update rsync tini dcron
ENTRYPOINT ["/sbin/tini", "--"]
ADD https://github.com/itzg/rcon-cli/releases/download/1.4.0/rcon-cli_1.4.0_linux_amd64.tar.gz /
RUN tar xf /rcon-cli_1.4.0_linux_amd64.tar.gz \
	&& mv /rcon-cli /usr/local/bin/ \
	&& rm /rcon-cli_1.4.0_linux_amd64.tar.gz
ADD backup.sh /
ADD run.sh /
CMD /run.sh
