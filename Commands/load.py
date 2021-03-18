import discord
from discord.ext import commands
from core.classes import Cog_Extension

class load(Cog_Extension):
    @commands.command()
    async def load(self, ctx, extension):
        print(f"load {extension}")
        self.bot.load_extension(f'commands.{extension}')

    @commands.command()
    async def unload(self, ctx, extension):
        print(f"unload {extension}")
        self.bot.unload_extension(f'commands.{extension}')

    @commands.command()
    async def reload(self, ctx, extension):
        print(f"reload {extension}")
        self.bot.reload_extension(f'commands.{extension}')

def setup(bot):
    bot.add_cog(load(bot))