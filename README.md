# ShakePay Python Shakingbot

These scripts and bot are provided "as is" and do not have any guarantees on their outcome. By using these scripts you acknowledge this disclamer and assume full responsibility of using them.

If you wish to donate, send any amount other than 5$ to domi167. BTC and ETH Accepted :)

# What tools are there?

Shake bot
```bash
python shake.py 
```

# How to get it going

## ------------ Docker ------------
```bash
docker-compose build
docker-compose up -d shakingbot-tools
docker exec -it shakingbot-tools sh
python login.py
```
Now before you start the bot.
CTRL+D to detach

Once you are satisfied with the outcome:
Run the bot:
```bash
docker-compose up -d shakingbot
```

## ------------ No Docker ------------

```bash
pip install --no-cache-dir -r requirements.txt
pip install requests
python login.py
```

Once you are satisfied with the outcome, you can run the bot:
```bash
python shake.py
```
The shakingbot should be running from there on and shake every 6 to 10 hours.
