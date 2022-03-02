# RH-Bot

Fun Discord Bot for moving users around

## Dependencies

See requirements.txt

## Enviroment variables

You need to have the following enviroment variables loaded:

- RH_BOT_DISCTOKEN: token of the discord bot account
- RH_BOT_RHCHID: channel if of the RH channel

## Running directly

```sh
python src/main.py
```

## Running with pm2

First install pm2. I did with npm: `sudo npm install pm2 -g`

### First Start

pm2 start src/main.py --name RHBot --interpreter python3

### Reload App with envs

pm2 restart RHBot --update-env
