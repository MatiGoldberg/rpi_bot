# rpi_bot

Telegram dispatcher bot running on RPi Zero W.

If you want to control your raspberry pi from telegram, this project might interest you.
The idea is that you can run a telegram bot throught the [Telegram bot api](https://core.telegram.org/bots/api), and open a chat with it.
Once the channel is open, you can send messages both ways :)

On top of a bot-based dispatcher, I'm adding a hardware library to control sensors and actuators, letting anyone create their own home automation project.

Have fun.

## Run

`python3 bot_runner.py`

## configuration file format

bot.config.json

```json
{
    "token": "your bot token",
    "name": "your bot name",
    "polling_period_sec": 0.5
}
```

## how to contribute

Don't at this point.
once the base is working, feel free to add libraries to it.
