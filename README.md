# RH-Bot

Fun Discord Bot for moving users around

## Dependencies

See requirements.txt

## Env Script

Fill the required information on the `export_envs.sh`

## Running directly

```sh
./export_envs.sh && python src/main.py
```

## Running with pm2

First install pm2. I did with npm: `sudo npm install pm2 -g`

### First Start

./export_envs.sh && pm2 start src/main.py --name RHBot --interpreter python3

### Reload App with envs

./export_envs.sh && pm2 restart RHBot --update-env
