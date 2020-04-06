import discord
import yaml

class Tethys(discord.Client):
    def __init__(self):
        super().__init__()

        config_file = open("config.yaml")
        self.config = yaml.load(config_file, Loader=yaml.FullLoader)
        config_file.close()

    async def on_ready(self):
        await self.get_channel(self.config["log_channel"]).send("Tethys has just started up")

    async def on_bulk_message_delete(self, messages):
        # Logging
        for message in messages:
            await self.on_message_delete(message)

    async def on_message_delete(self, message):
        # Logging
        embed = discord.Embed(color=discord.Color.red())
        embed.title = "Deleted Message"
        embed.add_field(name="Username", value=message.author)
        embed.add_field(name="UserId", value=message.author.id, inline=False)
        embed.add_field(name="Channel", value="<#%d>" % message.channel.id, inline=False)
        embed.add_field(name="Content", value=message.content, inline=False)
        await self.get_channel(self.config["log_channel"]).send(embed=embed)
    
    async def on_message_edit(self, before, after):
        # Logging
        if before.content != "" and before.content is not after.content:
            embed = discord.Embed(color=discord.Color.blue())
            embed.title = "Edited Message"
            embed.add_field(name="Username", value=after.author)
            embed.add_field(name="UserId", value=after.author.id, inline=False)
            embed.add_field(name="Channel", value="<#%d>" % before.channel.id, inline=False)
            embed.add_field(name="Before", value=before.content, inline=False)
            embed.add_field(name="After", value=after.content, inline=False)
            await self.get_channel(self.config["log_channel"]).send(embed=embed)

    async def on_member_remove(self, member):
        # Logging
        embed = discord.Embed(color=discord.Color.orange())
        embed.title = "User Left"
        embed.add_field(name="Username", value=member)
        embed.add_field(name="UserId", value=member.id, inline=False)
        await self.get_channel(self.config["log_channel"]).send(embed=embed)
    
    async def on_member_join(self, member):
        # Logging
        embed = discord.Embed(color=discord.Color.blue())
        embed.title = "User Joined"
        embed.add_field(name="Username", value=member)
        embed.add_field(name="UserId", value=member.id, inline=False)
        embed.set_image(url=member.avatar_url)
        await self.get_channel(self.config["log_channel"]).send(embed=embed)
