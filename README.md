# ShakePay Python Shakingbot

These scripts and bot are provided "as is" and do not have any guarantees on their outcome. By using these scripts you acknowledge this disclamer and assume full responsibility of using them.

If you wish to donate, send any amount to domi167. BTC and ETH accepted :)

# What tools are there?

Shake bot
```bash
python shake.py 
```

# How to get it going

## ------------ Docker ------------
```bash
docker-compose up -d shakingbot-tools
docker exec -it shakingbot-tools sh
python login.py

# once you are logged in, you can try a shake by running:

python shake.py
```
CTRL+D to detach from the shakingbot-tools container, and shut it down
```bash
docker-compose down
```

Once you are satisfied with the outcome:
Run the bot:
```bash
docker-compose up -d shakingbot
```

## ------------ No Docker ------------

```bash
cd docker-shakingbot
pip install --no-cache-dir -r requirements.txt
pip install requests
cd shakingbot
python login.py
```

Once you are satisfied with the outcome, you can run the bot:
```bash
python shake.py
```
The shakingbot should be running from there on and shake every 6 to 10 hours.
