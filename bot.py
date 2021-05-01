import discord
import json, os
from discord.ext import commands

with open(r'.\setting\Token.json') as TokenFile:
    TokenData = json.load(TokenFile)

with open(r'.\setting\Setting.json') as SettingFile:
    SettingData = json.load(SettingFile)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=SettingData['Prefix'], intents=intents)

@bot.event
async def on_ready():
    BotName = SettingData['BotName']
    print(f'{BotName} is on ready')

for Filename in os.listdir(r'.\commands'):
    if Filename.endswith('.py'):
        bot.load_extension(f'commands.{Filename[:-3]}')

if __name__ == "__main__":
    bot.run(TokenData['Token'])