import discord
import asyncio
TOKEN = ''
client = discord.Client()
Question=None
do_q = False
adm = None
reaction_message = None
asr_channel = None

#ログイン通知
@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')

@client.event
async def on_message(message):
    global Question
    global do_q
    global adm
    global reaction_message
    global asr_channel
    guild = message.guild
    if message.content.startswith('/vote')and Question==None:
        adm = message.author
        Question = (message.content[6:])
        await message.channel.send('Answer pls startswith /asr answer1:answer2:an...(Max:4)')
    if Question != None and message.content.startswith('/asr'):
        asr_channel = message.channel
        answer= (message.content[5:])
        answer_list = answer.split('/')
        answer_num = len(answer_list)
        num = answer_num
        emoji=list()
        if num >= 1:
            emoji.append('1️⃣')
        if num >= 2:
            emoji.append('2️⃣')
        if num >= 3:
            emoji.append('3️⃣')
        if num >= 4:
            emoji.append('4️⃣')
        q_embed = discord.Embed(title='qusetion',description=(str(Question)),colour=discord.Colour.green())
        for (l_answer_num,l_answer) in zip(answer_list,emoji):
            q_embed.add_field(name=(l_answer_num),value=(l_answer),inline=False)
        reaction_message=await message.channel.send(embed=q_embed)
        for reaction_emoji in emoji:
            await reaction_message.add_reaction(reaction_emoji)
        do_q = True

    if message.content == '/fin':
        if do_q == True:
            f_re_msg = await asr_channel.fetch_message(reaction_message.id)
            result_e = discord.Embed(title='Result form',description=(f_re_msg.jump_url),colour=discord.Colour.magenta())
            for reaction in f_re_msg.reactions:
                result_e.add_field(name=str(reaction.emoji),value='The number of times this reaction was done'+str(reaction.count))
            await message.channel.send(embed=result_e)
            do_q = False
        elif do_q == False:
            await message.channel.send('You have not yet added votes')
        else:
            do_q = False

                
        
    if message.content == '/future':
        f_emb = discord.Embed(title='Future cmd',discription='Vote Bot Future cmd',colour=discord.Colour.blue())
        f_emb.add_field(name='Now Version',value='V1.1',inline=False)
        f_emb.add_field(name='New Feature 1',value='Only people with the same role as the bot can vote',inline=False)
        f_emb.add_field(name='New Feature 2',value='Allows you to specify a voting deadline',inline=False)
        f_emb.add_field(name='New Feature 3',value='Help users recognize where they voted',inline=False)
        await message.channel.send(embed=f_emb)
    
    if message.content == '/state':
        await message.channel.send('Qusetion = '+str(Question))
        await message.channel.send('do_q = '+str(do_q))
        if adm == None:
            await message.channel.send('adm = None')
        else:
            await message.channel.send('adm = '+str(adm.display_name))
        
        if reaction_message == None:
            await message.channel.send('reaction_message = None')
        else:
            await message.channel.send('reaction_message = '+str(reaction_message.id))
        
        if asr_channel == None:
            await message.channel.send('asr_channel = None')
        else:
            await message.channel.send('asr_channel = '+str(asr_channel.id))    
    if message.content == '/reset':
        Question = None
        do_q = False
        adm = None
        reaction_message = None
        asr_channel = None
        await message.channel.send('all reseted')

    if message.content == '/emoji':
        if reaction_message != None:
            await message.channel.send('length of reaction list in reaction_message'+str(len(reaction_message.reactions)))
        else:
            await message.channel.send('reaction_message is NoneType')

    
        



            
            

        

client.run(TOKEN)