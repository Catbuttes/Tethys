import discord
from discord.ext import commands
import os
from typing import List


class Tethys(commands.Bot):
    def __init__(self, config):
        super().__init__(command_prefix="t!")
        self.config = config
        self.load_plugins()

    def load_plugins(self) -> None:
        plugins: List() = []
        for item in os.listdir("Plugins"):
            if os.path.isdir("Plugins/{0}".format(item)):
                if "__init__.py" in os.listdir("Plugins/{0}".format(item)):
                    plugins.append("Plugins.{0}".format(item))
            else:
                plugins.append("Plugins.{0}".format(item))

        for plugin in plugins:
            self.load_extension(plugin)

    def get_join_leave_log_channel(self, guild: discord.Guild) -> discord.TextChannel:
        """
        This gets the log channel for the specified guild's join/part logs
        it will fall back to the default log channel if it can't find it
        using the name join-leave-logs
        """
        for channel in guild.channels:
            if channel.name == "join-leave-logs":
                return channel
        return self.get_default_log_channel(guild)

    def get_edit_delete_log_channel(self, guild: discord.Guild) -> discord.TextChannel:
        """
        This gets the log channel for the specified guild's edit/delete logs
        it will fall back to the default log channel if it can't find it
        using the name join-leave-logs
        """
        for channel in guild.channels:
            if channel.name == "edit-delete-logs":
                return channel
        return self.get_default_log_channel(guild)

    def get_default_log_channel(self, guild: discord.Guild) -> discord.TextChannel:
        """
        This gets the default logging channel for the specified guild's logging
        It will fall back to a global log channel if it fails
        """
        for channel in guild.channels:
            if channel.name == "tethys-logs":
                return channel
        else:
            return self.get_channel(int(self.config["log_channel"]))

    def run(self, **kwargs):
        if len(kwargs) == 0:
            super().run(self.config["tethys_token"])
        else:
            super().run(self.config["tethys_token"], kwargs)

    async def on_ready(self) -> None:
        watching: discord.Activity = discord.Activity(name="you lot...", type=discord.ActivityType.watching)
        await self.change_presence(activity=watching)
        channel: discord.TextChannel = self.get_channel(int(self.config["log_channel"]))
        await channel.send("Tethys has just started up")
        me: discord.AppInfo = await self.application_info()
        invite: str = "https://discordapp.com/api/oauth2/authorize?client_id={0}&permissions=0&scope=bot".format(me.id)
        await channel.send(invite)
