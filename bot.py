import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

# Examples of creating events.
# Function decorator uses 'client' because 'client'
# was used as variable to hold instance of my bot.
# Decorators should be consistent with name of bot.

# On_ready is called when the client is done preparing
# the data received from Discord after login is successful.
# Async def functions are used because events must be a
# coroutine (used between two closely related concepts).

@client.event  
async def on_ready(): 
    print('Bot is ready.')
    
# Called when a member joins.
# Event takes a member object and prints.

@client.event #
async def on_member_join(member):
    print(f'{member} has joined the server.')
    
# Called when a member leaves.
# Event takes a member object and prints.

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

# Command triggered when user tells it to run.
# Name of function = name of command.
# ctx = context parameter
# !ping command returns Pong! and shows latency of bot
# using client.latency * 1000 for ms.

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

# import random to get random response.
# 8 ball command uses list of strings used to invoke command.

@client.command('magic8ball')
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes – definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Dont count on it.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


client.run('token')
