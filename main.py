import asyncio
import json
import os

import discord
from discord.ext import commands

with open('items.json', "r", encoding="utf8") as file:
  data = json.load(file)

bot = commands.Bot(command_prefix='!',
                   owner_ids=data['owner_id'],
                   intents=discord.Intents.all())


@bot.event
async def on_ready():
  print("Bot in ready")


# 載入py檔案
async def load_cogs():
  for file in os.listdir("./cogs"):
    if file.endswith('.py'):
      print(file)
      await bot.load_extension(f"cogs.{file[:-3]}")


async def main():
  async with bot:
    await load_cogs()
    await bot.start(data['token'])


# 確定執行此py檔才會執行
if __name__ == "__main__":
  asyncio.run(main())

#bot.run(data['token'])
