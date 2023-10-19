import asyncio
import discord
from discord.ext import commands
import os
intents = discord.Intents.default()
intents. message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def load():    
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await bot.load_extension(f'commands.{filename[:-3]}')

async def main():
    await load()    
    await bot.start('')

asyncio.run(main())