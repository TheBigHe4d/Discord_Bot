# cogs/loadReload.py
import discord
from discord.ext import commands
from core.any import Cog_Extension
import json, os

with open('items.json', 'r', encoding='utf8') as file:
   data = json.load(file)

class reloadCogs(Cog_Extension):
    @commands.command()
    # @commands.is_owner()
    # 管理者才能使用
    async def load(self, ctx, extension):
        self.bot.load_extension(f'cogs.{extension}')
        await ctx.author.send(f"{extension} 已上傳")

    @commands.command()
    # @commands.is_owner()
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f'cogs.{extension}')
        await ctx.author.send(f'{extension} 已卸載')

    @commands.command()
    # @commands.is_owner()
    # 如果直接更改程式碼的話就直接reload
    async def reload(self, ctx, extension):
        self.bot.reload_extension(f'cogs.{extension}')
        await ctx.author.send(f'{extension} 已更新')


def setup(bot):
    bot.add_cog(reloadCogs(bot))