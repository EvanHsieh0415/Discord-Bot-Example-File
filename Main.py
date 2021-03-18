import discord
import json
import os
from discord.ext import commands

with open('.\\Setting\\Token.json') as TokenFile:
    TokenData = json.load(TokenFile)

with open('.\\Setting\\Setting.json') as SettingFile:
    SettingData = json.load(SettingFile)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=SettingData['Prefix'], intents=intents)

@bot.event()
async def on_ready():
    BotName = SettingData['BotName']
    print(f'{BotName} is on ready')

@bot.event()
async def on_member_join(member):
    print(f'{member} join {member.guild.name}')

@bot.event()
async def on_member_remove(member):
    print(f'{member} leave {member.guild.name}')

for Filename in os.listdir('.\\Commands'):
    if Filename.endswith('.py'):
        bot.load_extension(f'commands.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(TokenData['Token'])