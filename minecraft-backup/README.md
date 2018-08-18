# minecraft-backup
Automated backup script for Minecraft

Sends `save-off`, `save-all`, and `save-on` commands to the server via RCON to ensure the backup is a clean snapshot and is not modified while copying.

## Usage
```
docker run --volumes-from minecraft
	--link minecraft:minecraft
	-e RCON_HOST=minecraft
	-e RCON_PORT=25575
	-e RCON_PASSWORD=minecraft
	-e BACKUP_SRC=/data/world
	-e BACKUP_DEST=/backups/
	-e SCHEDULE="0 0 * * *"
	-v ./backups:/backups
	deltawhy/minecraft-backup
```

### Docker Compose
```
version: '3.1'
volumes:
  minecraft-data:
services:
  minecraft:
    image: itzg/minecraft-server
    volumes:
      - minecraft-data:/data
    ...
  backup:
    image: deltawhy/minecraft-backup
    volumes:
      - minecraft-data:/data
      - ./backups:/backups
```
