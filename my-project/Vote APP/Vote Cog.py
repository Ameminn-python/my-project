import discord
from discord.ext import commands
TOKEN = ''
bot = commands.Bot(command_prefix='*')


@bot.event
async def on_ready():
    print('login.')

class qa(commands.Cog):
    def __init__(self):
        self.Question = dict()
        self.do_q = dict()
        self.adm = dict()
        self.reaction_message = dict()
        self.asr_channel = dict()
        
    @commands.Cog.listener()
    async def on_ready():
        for g in client.guilds:
            self.Question[g.id] = None
            self.do_q[g.id]=False
            self.adm[g.id]=None
            self.reaction_message[g.id] = None
            self.asr_channel[g.id] = None

    @commands.Cog.listener()
    async def on_guild_join(guild):
        self.Question[guild.id] = None
        self.do_q[guild.id]=None
        self.adm[guild.id]=None
        self.reaction_message[guild.id] = None
        self.asr_channel[guild.id] = None
            
        
   

    


    @commands.command()
    async def vote(self,ctx,*,Q):
        if ctx.guild.id in self.Question is True:
            if self.Question[ctx.guild.id] is None
                self.adm[ctx.guild.id] = ctx.author
                self.Question[ctx.guild.id] = Q
                await ctx.send('Answer pls startswith *asr answer1/answer2/an...(Max:4)')
            else:
                await ctx.send('You have any question in guild')
        else:
            await ctx.send('dict Error(Vote): pls feedback to ameminn')
        
    @commands.command()
    async def asr(self,ctx,a):
        if ctx.guild.id in self.Question is True:
            if self.Question[ctx.guild.id] is not None:
                self.asr_channel[ctx.guild.id] = ctx.channel.id
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
                q_embed = discord.Embed(title='アンケート',description=(str(self.Question[ctx.guild.id])),colour=discord.Colour.green())
                for (l_answer_num,l_answer) in zip(answer_list,emoji):
                    q_embed.add_field(name=(l_answer_num),value=(l_answer),inline=False)
                self.reaction_message[ctx.guild.id] = await ctx.send(embed=q_embed)
                for reaction_emoji in emoji:
                    await self.reaction_message[ctx.guild.id].add_reaction(reaction_emoji)
                self.do_q[ctx.guild.id] = True
                

    @commands.command()
    async def fin(self,ctx):
        if self.do_q[ctx.guild.id] == True:
            f_re_msg = await self.asr_channel[ctx.guild.id].fetch_message(self.reaction_message[ctx.guild.id].id)
            result_e = discord.Embed(title='Result form',description=(f_re_msg.jump_url),colour=discord.Colour.magenta())
            for reaction in f_re_msg.reactions:
                result_e.add_field(name=str(reaction.emoji),value='The number of times this reaction was done'+str(reaction.count))
            await ctx.send(embed=result_e)
            self.do_q[ctx.guild.id] = False
        elif self.do_q[ctx.guild.id] == False:
            await ctx.send('You have not yet added votes')
        else:
            self.do_q[ctx.guild.id] = False
qa = qa()
bot.add_cog(qa)

bot.run(TOKEN)
