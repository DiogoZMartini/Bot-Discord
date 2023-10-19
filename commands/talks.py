import discord
from discord.ext import commands

class Talks(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ajuda")
    async def send_help(self, ctx):
        try:
            await ctx.author.send(f':notebook_with_decorative_cover: ***Lista de Comandos*** :notebook_with_decorative_cover:\n'+
                '***!roll d20*** --> :game_die: Rola um dado de 20 lados :game_die:\n'+
                '**!ap1** Mostra uma Imagme do Primeiro Apostolo\n'+
                '**!ap2** Mostra uma Imagme do Segundo Apostolo\n'+
                '**!ap3** Mostra uma Imagme do Trceiro Apostolo\n'+
                '**!ap4** Mostra uma Imagme do Quarto Apostolo\n'+
                '**!ap5** Mostra uma Imagme do Quinto Apostolo\n'+
                '**!apc5** Mostra uma Imagme do companheiro do Quinto Apostolo')
        except discord.errors.Forbidden:
            await ctx.send('Não foi possivel enviar a mensagem, habilite receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)')
    
async def setup(bot):
    await bot.add_cog(Talks(bot))