from discord.ext import commands
import os
import pdf2image
import discord


class ExpandFiles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.attachments is None:
            return
        for attachment in message.attachments:
            if attachment.content_type != "application/pdf":
                continue
            await attachment.save(f"{message.id}.pdf")
            images = pdf2image.convert_from_path(f"{message.id}.pdf")
            fname = os.path.splitext(f"{message.id}.pdf")[0]
            for index, image in enumerate(images):
                image.save(fname +"-"+ str(index+1) + '.png')
                await message.channel.send(file=discord.File(fname +"-"+ str(index+1) + '.png'))
                os.remove(fname +"-"+ str(index+1) + '.png')
            os.remove(f"{message.id}.pdf")


def setup(bot):
    bot.add_cog(ExpandFiles(bot))
