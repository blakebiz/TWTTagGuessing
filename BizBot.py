import datetime
import discord
import time

from aiohttp import ClientSession
from discord.ext import commands
from Storage import Storage
from tagguessing import mainHandler

init_cogs = ['cogs.commands']


class Bot(commands.AutoShardedBot):
    def __init__(self, nick):
        super().__init__(command_prefix=nick+'.', case_insensitive=True)
        self.session = ClientSession(loop=self.loop)
        self.start_time = datetime.datetime.utcnow()
        self.storage = Storage()
        self.handler = mainHandler.mainHandler()


    async def on_ready(self):
        print(f'Successfully logged in as {self.user}\nSharded to {len(self.guilds)} guilds')
        await self.change_presence(activity=discord.Game(name='hello :)"'))
        start = time.time()
        for ext in init_cogs:
            self.load_extension(ext)
        print(f'Loaded all extensions after {time.time() - start}')

    def stop(self):
        raise Exception('Force stop called on BizBot.Bot')

    # Discord Functions
    async def on_message(self, message):
        if message.author.bot:
            return
        print(message.content)

        await self.process_commands(message)

    async def on_raw_reaction_add(self, payload):
        if payload.user_id == self.user.id:
            return
        channel = self.get_channel(payload.channel_id)
        if 'open_guesses' in self.storage.data and str(payload.message_id) in self.storage.data['open_guesses']:
            await self.handle_guess(payload, channel)


    async def handle_guess(self, payload, channel):
        # if payload.user_id == 463166198335537162:
        msg = await channel.fetch_message(payload.message_id)
        if payload.emoji.name == '✅':
            self.handler.correct_guess(
                msg.content[msg.content.index(';')+2:],
                self.storage.data['open_guesses'][str(payload.message_id)])
            self.storage.dict_delete('open_guesses', str(payload.message_id))
            print('finished check')
        elif payload.emoji.name == '❌':
            self.storage.dict_delete('open_guesses', str(payload.message_id))
            print('finished x')
        elif payload.emoji.name == '❓':
            self.storage.add('wrong_guess', self.storage.data['open_guesses'][str(payload.message_id)])
            self.storage.dict_delete('open_guesses', str(payload.message_id))
            await channel.send(f'Please send wanted tag to {self.command_prefix}wrong_guess')
            print('finished ?')








