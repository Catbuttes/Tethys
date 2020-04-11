import discord
from typing import List
class Tethys(discord.Client):
    def __init__(self, config):
        super().__init__()
        self.config = config

    def get_join_leave_log_channel(self, guild: discord.Guild) -> discord.TextChannel:
        for channel in guild.channels:
            if channel.name == "join-leave-logs":
                return channel
        return self.get_default_log_channel(guild)

    def get_edit_delete_log_channel(self, guild: discord.Guild) -> discord.TextChannel:
        for channel in guild.channels:
            if channel.name == "edit-delete-logs":
                return channel
        return self.get_default_log_channel(guild)

    def get_default_log_channel(self, guild: discord.Guild) -> discord.TextChannel:
        for channel in guild.channels:
            if channel.name == "tethys-logs":
                return channel
        return self.get_channel(self.config["log_channel"])

    def run(self, **kwargs):
        if len(kwargs) == 0:
            super().run(self.config["tethys_token"])
        else:
            super().run(self.config["tethys_token"], kwargs)

    async def on_ready(self) -> None:
        await self.get_channel(self.config["log_channel"]).send("Tethys has just started up")

    async def on_bulk_message_delete(self, messages: List[discord.Message]) -> None:
        # Logging
        for message in messages:
            await self.on_message_delete(message)

    async def on_message_delete(self, message: discord.Message) -> None:
        # Logging
        embed = discord.Embed(color=discord.Color.red())
        embed.title = "Deleted Message"
        embed.add_field(name="Username", value=message.author)
        embed.add_field(name="UserId", value=message.author.id, inline=False)
        embed.add_field(name="Channel", value="<#%d>" % message.channel.id, inline=False)
        embed.add_field(name="Content", value=message.content, inline=False)
        await self.get_edit_delete_log_channel(message.guild).send(embed=embed)
    
    async def on_message_edit(self, before: discord.Message, after: discord.Message) -> None:
        # Logging
        if before.content != "" and before.content is not after.content:
            embed = discord.Embed(color=discord.Color.blue())
            embed.title = "Edited Message"
            embed.add_field(name="Username", value=after.author)
            embed.add_field(name="UserId", value=after.author.id, inline=False)
            embed.add_field(name="Channel", value="<#%d>" % before.channel.id, inline=False)
            embed.add_field(name="Before", value=before.content, inline=False)
            embed.add_field(name="After", value=after.content, inline=False)
        await self.get_edit_delete_log_channel(before.guild).send(embed=embed)

    async def on_member_remove(self, member: discord.Member) -> None:
        # Logging
        embed = discord.Embed(color=discord.Color.orange())
        embed.title = "User Left"
        embed.add_field(name="Username", value=member)
        embed.add_field(name="UserId", value=member.id, inline=False)
        await self.get_join_leave_log_channel(member.guild).send(embed=embed)
    
    async def on_member_join(self, member: discord.Member) -> None:
        # Logging
        embed = discord.Embed(color=discord.Color.blue())
        embed.title = "User Joined"
        embed.add_field(name="Username", value=member)
        embed.add_field(name="UserId", value=member.id, inline=False)
        embed.set_image(url=member.avatar_url)
        await self.get_join_leave_log_channel(member.guild).send(embed=embed)
