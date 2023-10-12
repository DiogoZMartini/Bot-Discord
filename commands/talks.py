from discord.ext import commands

class Talks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_Cog(Talks(bot))