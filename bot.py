from discord.ext import commands 
import discord
import json
import os

with open('items.json', "r", encoding = "utf8") as file:
    data = json.load(file)

bot = commands.Bot(command_prefix = '!', 
                   owner_ids = data['owner_id'],
                   intents = discord.Intents.all())

# 只要是python檔案就會進行載入
for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

@bot.event
async def on_ready():
    print("Bot in ready")


bot.run(data['token']) 