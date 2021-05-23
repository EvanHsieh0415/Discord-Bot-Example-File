import discord
from discord.ext import commands
from core.classes import Cog_Extension
from datetime import datetime

def loadLog(loadType, author, extension):
    now = f"[{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}]"
    out = f"{now} {author} {loadType} {extension}.py"
    return out

class load(Cog_Extension):
    @commands.command()
    async def load(self, ctx, extension):
        print(loadLog("load", ctx.author, extension))
        self.bot.load_extension(f'commands.{extension}')

    @commands.command()
    async def unload(self, ctx, extension):
        print(loadLog("unload", ctx.author, extension))
        self.bot.unload_extension(f'commands.{extension}')

    @commands.command()
    async def reload(self, ctx, extension):
        print(loadLog("reload", ctx.author, extension))
        self.bot.reload_extension(f'commands.{extension}')

def setup(bot):
    bot.add_cog(load(bot))