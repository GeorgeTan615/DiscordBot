# bot.py
#py -m pip install 
import os
import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()    #must be added so that we can access info inside of server
client = discord.Client(intents=intents) #must be added so that we can access info inside of server

#bot upon joining channel actions, show bot and member detail
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name = GUILD)      #get guild according to discord guild defined in .env

    print(
        f'{client.user.name} has connected to the following guild:\n'   #{botname} has connected to ....
        f'{guild.name}(id: {guild.id})'
    )

#send dm to member when join channel
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to {GUILD}\'s server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:       #important to check this to prevent handling a message that the bot sent, prevent recurisve calls
        return
    
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if 'happy birthday' in message.content.lower():
        await message.channel.send('WOOHOO ITS YOUR BIG DAY 🎂🎉 HAPPY BIRTHDAYYY 🥳')


    if 'love' in message.content.lower():
        gif_url_choices = ['https://media.giphy.com/media/26FLdmIp6wJr91JAI/giphy.gif?cid=ecf05e47zix60aka8u0lb1bqcwe89mw3j64a00q50xfdnb6u&rid=giphy.gif&ct=g',
                            'https://media.giphy.com/media/4N1wOi78ZGzSB6H7vK/giphy.gif?cid=ecf05e47rvlc9xtma3qm5j2wdqydgparv5tgldr60k9c4l7g&rid=giphy.gif&ct=g',
                            'https://media.giphy.com/media/M90mJvfWfd5mbUuULX/giphy.gif?cid=ecf05e47zix60aka8u0lb1bqcwe89mw3j64a00q50xfdnb6u&rid=giphy.gif&ct=g',
                            'https://media.giphy.com/media/BMVS53dkX8pYaR9IMD/giphy.gif?cid=ecf05e47rvlc9xtma3qm5j2wdqydgparv5tgldr60k9c4l7g&rid=giphy.gif&ct=g',
                            'https://media.giphy.com/media/l2R0cE5EqO3QHiCoU/giphy.gif?cid=ecf05e47rvlc9xtma3qm5j2wdqydgparv5tgldr60k9c4l7g&rid=giphy.gif&ct=g',
                            'https://media.giphy.com/media/iGDx7wJkQykUM/giphy.gif?cid=ecf05e47rvlc9xtma3qm5j2wdqydgparv5tgldr60k9c4l7g&rid=giphy.gif&ct=g']
        gif_url = random.choice(gif_url_choices)
        embed = discord.Embed()
        embed.set_image(url=gif_url)
        await message.channel.send(embed=embed)

    if message.content.lower() == '!members':
        guild = discord.utils.get(client.guilds, name = GUILD)
        member_list = [member.name for member in guild.members if member.name != client.user.name]
        members = '\n - '.join(member_list)
        members = f'FiscalTea Members({len(member_list)}):\n - {members}'

        await message.channel.send(members)

client.run(TOKEN)
