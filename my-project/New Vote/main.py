import discord
from discord.ext import commands
from votecog import qa
TOKEN = ''
bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
    print('login')


bot.add_cog(qa(bot))

bot.run(TOKEN)
