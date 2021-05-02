import discord, asyncio
import random
import os
from discord.ext import commands
from discord import message
from discord.ext.commands import Bot
from keep_alive import keep_alive

prefix = "pls"

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Ready to spam 'pls lottery' lol")
    print('Created by Cryptos1337. Give Credits if you\'re recording :)')
    print('Logged in as dababy')
    print('------')


@bot.command(pass_context=True)
async def start(ctx):
    if bot.user.id == ctx.message.author.id:
        await asyncio.sleep(2)
        await ctx.send('pls daily')
        await asyncio.sleep(3 + random.randint(1, 3))
        await ctx.send('pls dep all')
        await asyncio.sleep(3 + random.randint(1, 3))
        await ctx.send('pls beg')
        await asyncio.sleep(3 + random.randint(1, 3))
        await ctx.send('pls with 1e3')
        await asyncio.sleep(5 + random.randint(1, 3))
        await ctx.send('pls pet feed')
        await asyncio.sleep(3 + random.randint(1, 3))

        while True:
            await ctx.send('pls with 5e3')
            await asyncio.sleep(5 + random.randint(1, 3))
            await ctx.send('pls lottery')
            await asyncio.sleep(5 + random.randint(1, 3))
            await ctx.send('yes')
            await asyncio.sleep(5 + random.randint(1, 3))
            r = random.randint(1, 5)
            if r == 1:
                await asyncio.sleep(20)
                await ctx.send('pls beg')
            elif r == 2:
                await ctx.send('pls fish')
            elif r == 3:
                await ctx.send('pls hunt')
            await asyncio.sleep(5 + random.randint(1, 3))
            await ctx.send('pls slots max')
            await asyncio.sleep(8 + random.randint(1, 3))
            await ctx.send('pls slots max')
            await asyncio.sleep(3600)


#plsstart
keep_alive()
bot.run(os.getenv('TOKEN'), bot=False)
