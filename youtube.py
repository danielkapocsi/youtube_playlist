import asyncio
import youtube_dl
import discord
from discord.ext import commands

class Youtube:
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency*1000)} ms')

        