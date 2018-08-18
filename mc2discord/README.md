# mc2discord
One-way bridge from Minecraft chat to Discord webhook

## Usage
```
docker run -e CONTAINER_NAME=minecraft
	-e WEBHOOK_URL=https://discordapp.com/api/webhooks/...
	-v /var/run/docker.sock:/var/run/docker.sock:ro
	deltawhy/mc2discord
```

### Docker Compose
```
version: '3.1'
services:
  minecraft:
    image: itzg/minecraft-server
    ...
  chat:
    image: deltawhy/mc2discord
    environment:
     - CONTAINER_NAME=minecraft_minecraft_1
     - WEBHOOK_URL=https://discordapp.com/api/webhooks/...
```
