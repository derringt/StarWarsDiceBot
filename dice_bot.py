import discord
from discord.ext import commands
import random

description = '''A first pass at an FFG/WEG Star Wars dice bot'''

bot = commands.Bot(command_prefix='!', description=description)

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

bot.run('MzUyNDYwNzIyNDA5NTcwMzA0.DIhkOA.lDbTPo0z-NWPWRk9UxruUUvMHPY')
