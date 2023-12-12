# cogs/embeds.py
import json

import discord
from discord.ext import commands

from core.any import Cog_Extension

with open('./items.json', "r", encoding="utf8") as file:
  data = json.load(file)


class Embeds(Cog_Extension):

  @commands.command(pass_context=True)
  async def tai(self, ctx):
    await ctx.send(file=discord.File('tai.png'))

  @commands.command(pass_context=True)
  async def helping(self, ctx):
    sms = discord.Embed(title="指令", description="'忘記了嗎? 來看一下吧~~", color=0x4599)
    await ctx.send(embed=sms)


async def setup(bot):
  await bot.add_cog(Embeds(bot))
