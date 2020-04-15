import discord
from discord.ext import commands
TOKEN = 'Njg2Njc3OTA1MTE1NTc4NDAz.XpZ25A.othOeTStn6Zl1mxZCpPlk7RjR2A'
bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
    print('login.')

class qa(commands.Cog):
    def __init__(self):
        self.Question = None
        self.do_q = False
        self.adm = None
        self.reaction_message = None
        self.asr_channel = None

    


    @commands.command()
    async def vote(self,ctx,*,Q):
        if self.Question is None:
            self.adm = ctx.author
            self.Question = Q
            await ctx.send('Answer pls startswith *asr answer1/answer2/an...(Max:4)')
        
    @commands.command()
    async def asr(self,ctx,a):
        if self.Question != None:
            self.asr_channel = ctx.channel
            answer= a
            answer_list = answer.split('/')
            num = len(answer_list)
            emoji=list()
            if num >= 1:
                emoji.append('1️⃣')
            if num >= 2:
                emoji.append('2️⃣')
            if num >= 3:
                emoji.append('3️⃣')
            if num >= 4:
                emoji.append('4️⃣')
            q_embed = discord.Embed(title='アンケート',description=(str(self.Question)),colour=discord.Colour.green())
            for (l_answer_num,l_answer) in zip(answer_list,emoji):
                q_embed.add_field(name=(l_answer_num),value=(l_answer),inline=False)
            self.reaction_message=await ctx.send(embed=q_embed)
            for reaction_emoji in emoji:
                await self.reaction_message.add_reaction(reaction_emoji)
            self.do_q = True

    @commands.command()
    async def fin(self,ctx):
        if self.do_q == True:
            f_re_msg = await self.asr_channel.fetch_message(self.reaction_message.id)
            result_e = discord.Embed(title='Result form',description=(f_re_msg.jump_url),colour=discord.Colour.magenta())
            for reaction in f_re_msg.reactions:
                result_e.add_field(name=str(reaction.emoji),value='The number of times this reaction was done'+str(reaction.count))
            await ctx.send(embed=result_e)
            self.do_q = False
        elif self.do_q == False:
            await ctx.send('You have not yet added votes')
        else:
            self.do_q = False
qa = qa()
bot.add_cog(qa)

bot.run(TOKEN)