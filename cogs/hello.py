# cogs/hello.py

from discord.ext import commands

from core.any import Cog_Extension


class Hello(Cog_Extension):

  @commands.command()
  async def hello(self, ctx):
    await ctx.send(f"!Hi <@{ctx.author.id}>")


async def setup(bot):
  await bot.add_cog(Hello(bot))
