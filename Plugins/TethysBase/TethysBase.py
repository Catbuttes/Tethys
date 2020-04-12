import discord
from discord.ext import commands
from typing import List
import Tethys


class TethysBase(commands.Cog):
    def __init__(self, bot: Tethys):
        self.bot = bot

    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages: List[discord.Message]) -> None:
        # Logging bulk deletes (i.e when a user is banned)
        for message in messages:
            await self.on_message_delete(message)

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message) -> None:
        # Logging deleted messages
        embed = discord.Embed(color=discord.Color.red())
        embed.title = "Deleted Message"
        embed.add_field(name="Username", value=message.author)
        embed.add_field(name="UserId", value=message.author.id, inline=False)
        embed.add_field(name="Channel", value="<#%d>" % message.channel.id, inline=False)
        embed.add_field(name="Content", value=message.content, inline=False)
        channel = self.bot.get_edit_delete_log_channel(message.guild)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message) -> None:
        # Logging edited messages
        if before.content != "" and before.content is not after.content:
            embed = discord.Embed(color=discord.Color.blue())
            embed.title = "Edited Message"
            embed.add_field(name="Username", value=after.author)
            embed.add_field(name="UserId", value=after.author.id, inline=False)
            embed.add_field(name="Channel", value="<#%d>" % before.channel.id, inline=False)
            embed.add_field(name="Before", value=before.content, inline=False)
            embed.add_field(name="After", value=after.content, inline=False)
            channel = self.bot.get_edit_delete_log_channel(before.guild)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member) -> None:
        # Logging members leaving
        embed = discord.Embed(color=discord.Color.orange())
        embed.title = "User Left"
        embed.add_field(name="Username", value=member)
        embed.add_field(name="UserId", value=member.id, inline=False)
        channel = self.bot.get_join_leave_log_channel(member.guild)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member) -> None:
        # Logging members joining
        embed = discord.Embed(color=discord.Color.blue())
        embed.title = "User Joined"
        embed.add_field(name="Username", value=member)
        embed.add_field(name="UserId", value=member.id, inline=False)
        embed.set_image(url=member.avatar_url)
        channel = self.bot.get_join_leave_log_channel(member.guild)
        await channel.send(embed=embed)
