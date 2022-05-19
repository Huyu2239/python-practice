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
        if before.channel is None:
            if after.channel.id == 971743639464198215:
                return await self.welcome(member)
        elif after.channel is None:
            if before.channel.id == 971743639464198215:
                return await self.bye(member) 

    
    async def welcome(self, member):
        channel = self.bot.get_channel(968500591837986866)
        embed = discord.Embed(title=f"{member.display_name}が参加しました。", colour=discord.Colour.green(), img=member.avatar_url)
        await channel.send(embed=embed)

    async def bye(self, member):
        channel = self.bot.get_channel(968500591837986866)
        embed = discord.Embed(title=f"{member.display_name}が退出しました。", colour=discord.Colour.red(), img=member.avatar_url)
        await channel.send(embed=embed)

    

def setup(bot):
    bot.add_cog(Notice(bot))