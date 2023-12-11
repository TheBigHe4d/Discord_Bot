# cogs/embeds.py
from discord.ext import commands
import discord
from discord.ext.commands import bot
from core.any import Cog_Extension
import json

with open('./items.json', "r", encoding = "utf8") as file:
    data = json.load(file)

class embeds(Cog_Extension):
    
    @commands.command(pass_context = True)
    async def helping(self, ctx):
        sms = discord.Embed(title = "指令", description = "'忘記了嗎? 來看一下吧~~", color = 0x4599)
        await ctx.send(embed = sms)  


def setup(bot):
    bot.add_cog(embeds(bot))