from os import path
import configparser
from bot import Bot, BotOptions

if not path.isfile('config.ini'):
    print("no config.ini file")
    exit(1)

config = configparser.ConfigParser()
config.read('config.ini')

twitchtoken = config.get("TWITCH", "token")
channel = config.get("TWITCH", "channel")

if not twitchtoken:
    print("Invalid config.ini : TWITCH:TOKEN")
    exit(1)

if not channel:
    print("Invalid config.ini : TWITCH:CHANNEL")
    exit(1)

bot = Bot(twitchtoken, channel, BotOptions({
    "showtime": config.get("CHAT", "showtime")
}))
bot.run()