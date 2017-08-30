import discord
from discord.ext import commands
import random
import dice
import re

with open('private_token.txt', 'r') as f:
    token = f.readline().strip()

description = '''A first pass at an FFG/WEG Star Wars dice bot'''

bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command()
async def ffg(dice_roll : str):
    """Rolls a set of FFG dice in abc format.

       a = Ability
       b = Boost
       c = Challenge
       d = Difficulty
       f = Force
       s = Setback

       Example: aabdc = 2 ability, 1 boost, 1 difficulty, and 1 challenge"""

    roll = re.search(r'^[abcdfs]+$', dice_roll)
    if roll:
        await bot.say(dice.display_results(dice.roll_string(dice_roll)))
    else:
        await bot.say('Needs to be in a valid format! See !help ffg for details.')

bot.run(token)
