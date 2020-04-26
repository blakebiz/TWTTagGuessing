import discord
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self. bot = bot
        self.__docs__cache = None
        self.resp_to_tag = {'Hello! How are you': 'hello', 'Have a good night!': 'bye'}
        self.tag_to_resp = {'hello': 'Hello! How are you', 'bye': 'Have a good night!'}



    @commands.command()
    async def guess_tag(self, ctx):
        tag = ctx.message.content[ctx.message.content.index(' ')+1:]
        response = self.bot.handler.interpret(tag)
        if response in self.resp_to_tag:
            msg = await ctx.send(f'Tag: {self.resp_to_tag[response]}; {response}')
            emojis = ['✅', '❌', '❓']
            for emoji in emojis:
                await msg.add_reaction(emoji=emoji)
            self.bot.storage.dict_add('open_guesses', str(msg.id), tag)
        else:
            await ctx.send(response)

    @commands.command()
    async def wrong_guess(self, ctx):
        if 'wrong_guess' in self.bot.storage.data:
            self.bot.handler.correct_guess(self.tag_to_resp[ctx.message.content[ctx.message.content.index(' ')+1:]],
                                           self.bot.storage.data['wrong_guess'])
            self.bot.storage.delete('wrong_guess')
            await ctx.send('Intents successfully updated')
        else:
            await ctx.send('No wrong guess in storage, try again')







def setup(bot):
    bot.add_cog(Commands(bot))


