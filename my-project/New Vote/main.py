import discord
from discord.ext import commands
from votecog import qa
TOKEN = 'Njg2Njc3OTA1MTE1NTc4NDAz.XpbnqA.nBvp5OxgFsJV0gRqBOEb_xa6GXc'
bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
    print('login')


bot.add_cog(qa(bot))

bot.run(TOKEN)