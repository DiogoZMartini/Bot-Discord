import discord
from discord.ext import commands

class manager(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print (f'{self.bot.user} está online!!')
        

async def setup(bot):
    await bot.add_cog(manager(bot))