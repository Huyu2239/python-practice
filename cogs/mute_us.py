from discord.ext import commands
import discord


class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ch_id = 971743639464198215


    @commands.command()
    async def mute(self, ctx):
        vc = self.bot.get_channel(self.ch_id)
        for member in vc.members:
            await member.edit(mute=True)

    @commands.command()
    async def unmute(self, ctx):
        vc = self.bot.get_channel(self.ch_id)
        for member in vc.members:
            await member.edit(mute=False)


def setup(bot):
    bot.add_cog(Mute(bot))
