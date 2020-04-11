import discord
from typing import List

class Tethys(discord.Client):
    def __init__(self, config):
        super().__init__()
        self.config = config

    def get_join_leave_log_channel(self, guild: discord.Guild) -> discord.TextChannel:
        # This gets the log channel for the specified guild's join/part logs
        # it will fall back to the default log channel if it can't find it 
        # using the name join-leave-logs
        for channel in guild.channels:
            if channel.name == "join-leave-logs":
                return channel
        return self.get_default_log_channel(guild)

    def get_edit_delete_log_channel(self, guild: discord.Guild) -> discord.TextChannel:
        # This gets the log channel for the specified guild's edit/delete logs
        # it will fall back to the default log channel if it can't find it 
        # using the name join-leave-logs
        for channel in guild.channels:
            if channel.name == "edit-delete-logs":
                return channel
        return self.get_default_log_channel(guild)

    def get_default_log_channel(self, guild: discord.Guild) -> discord.TextChannel:
        # This gets the default logging channel for the specified guild's logging
        # It will fall back to a global log channel if it fails
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
        watching = discord.Game(name="Watching you lot...")
        await self.change_presence(activity = watching)
        await self.get_channel(self.config["log_channel"]).send("Tethys has just started up")
        me = await self.application_info()
        invite = "https://discordapp.com/api/oauth2/authorize?client_id={0}&permissions=0&scope=bot".format(me.id)
        await self.get_channel(self.config["log_channel"]).send(invite)


    async def on_bulk_message_delete(self, messages: List[discord.Message]) -> None:
        # Logging bulk deletes (i.e when a user is banned)
        for message in messages:
            await self.on_message_delete(message)

    async def on_message_delete(self, message: discord.Message) -> None:
        # Logging deleted messages
        embed = discord.Embed(color=discord.Color.red())
        embed.title = "Deleted Message"
        embed.add_field(name="Username", value=message.author)
        embed.add_field(name="UserId", value=message.author.id, inline=False)
        embed.add_field(name="Channel", value="<#%d>" % message.channel.id, inline=False)
        embed.add_field(name="Content", value=message.content, inline=False)
        await self.get_edit_delete_log_channel(message.guild).send(embed=embed)
    
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
            await self.get_edit_delete_log_channel(before.guild).send(embed=embed)

    async def on_member_remove(self, member: discord.Member) -> None:
        # Logging members leaving
        embed = discord.Embed(color=discord.Color.orange())
        embed.title = "User Left"
        embed.add_field(name="Username", value=member)
        embed.add_field(name="UserId", value=member.id, inline=False)
        await self.get_join_leave_log_channel(member.guild).send(embed=embed)
    
    async def on_member_join(self, member: discord.Member) -> None:
        # Logging members joining
        embed = discord.Embed(color=discord.Color.blue())
        embed.title = "User Joined"
        embed.add_field(name="Username", value=member)
        embed.add_field(name="UserId", value=member.id, inline=False)
        embed.set_image(url=member.avatar_url)
        await self.get_join_leave_log_channel(member.guild).send(embed=embed)