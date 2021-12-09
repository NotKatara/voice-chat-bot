import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '[')

@client.event
async def on_ready():
    print('Bot is ready')

client.run('OTE4NDM4NzA2MDk0OTQ0MjY3.YbHQsw.U5BcZXl6w3SPME7ugLRlVtIg_Ck')