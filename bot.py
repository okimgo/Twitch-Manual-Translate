from twitchio.ext import commands
import codecs
from datetime import datetime

class BotOptions():
    showtime = False

    def __init__(self, opts):
        self.__dict__.update(opts)

class Bot(commands.Bot):
    def __init__(self, twitchtoken: str, channel: str, options: BotOptions):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        self.channel_name = channel
        self.options = options
        super().__init__(token=twitchtoken, prefix='!', initial_channels=[channel])
        self.file = codecs.open("chat.txt", 'w', 'utf-8')

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        #print(message.content)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def 번역(self, ctx: commands.Context):
        if (ctx.author.is_mod or ctx.author.name == self.channel_name):
            content = ctx.message.content[4:]

            if self.options.showtime:
                now = datetime.now()
                timefstr = now.strftime("%H:%M:%S")
                content = f"[{timefstr}] {content}"

            self.file.write("\n" + content)
            self.file.flush()
            print(content)
    
    def end(self):
        self.file.close()