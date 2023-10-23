import discord
from discord.ext import commands

class image(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ap1")
    async def send_image(self, ctx):
            await ctx.send(file=discord.File(".\img\mostros/apostolo_1.png"))

async def setup(bot):
    await bot.add_cog(image(bot))