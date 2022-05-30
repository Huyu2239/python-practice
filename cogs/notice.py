from discord.ext import commands, tasks
import aiohttp
import asyncio
import discord
import json
import os


class Notice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        title, colour = None, discord.Embed.Empty
        if before.channel is None:
            if after.channel.id == 971743639464198215:
                title = f"{member.display_name}が参加しました。"
                colour = discord.Colour.green()
        elif after.channel is None:
            if before.channel.id == 971743639464198215:
                title = f"{member.display_name}が退出しました。"
                colour = discord.Colour.red()
        else:
            return

        channel = self.bot.get_channel(968500591837986866)
        embed = discord.Embed(title=title, colour=colour)
        embed.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Notice(bot))
