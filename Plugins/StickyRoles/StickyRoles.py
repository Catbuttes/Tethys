import discord
from discord.ext import commands
import Tethys
from Plugins.StickyRoles import Persistance


class StickyRoles(commands.Cog):
    def __init__(self, bot: Tethys):
        self.bot = bot
        self.store = Persistance.Store(self.bot.config["data_dir"])

    @commands.group(invoke_without_command=True)
    async def stickyroles(self, ctx: commands.context):
        """
        Manages which roles are considered 'sticky'
        i.e. will be automatically reapplied if a user leaves then
        rejoins the server.
        """
        roles = self.store.get_roles(ctx.guild.id)

        embed = discord.Embed(color=discord.Color.blue())
        embed.title = "Current StickyRoles"
        for role in roles:
            role_detail = ctx.guild.get_role(role.role_id)
            embed.add_field(name=role_detail.name, value=role_detail.id, inline=True)

        await ctx.channel.send(embed=embed)

    @stickyroles.command()
    @commands.has_guild_permissions(manage_roles=True)
    async def add(self, ctx: commands.context, role: discord.Role) -> None:
        """
        Will make the mentioned role sticky
        """
        outcome = self.store.add_role(ctx.guild.id, role.id)
        if outcome:
            await ctx.channel.send("Added {0} to sticky list".format(role.name))
        else:
            await ctx.channel.send("Failed to add {0} to sticky list".format(role.name))

    @stickyroles.command()
    @commands.has_guild_permissions(manage_roles=True)
    async def clear(self, ctx: commands.context, role: discord.Role) -> None:
        """
        Will make the mentioned role unsticky
        """
        outcome = self.store.delete_role(ctx.guild.id, role.id)
        if outcome:
            await ctx.channel.send("Removed {0} from sticky list".format(role.name))
        else:
            await ctx.channel.send("Failed to remove {0} from sticky list".format(role.name))

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member) -> None:
        for role in member.roles:
            self.store.add_user_role(member.guild.id, member.id, role.id)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member) -> None:
        roles = self.store.get_user_roles(member.guild.id, member.id)
        for role in roles:
            role_detail = member.guild.get_role(role.role_id)
            await member.add_roles(role_detail, reason="Sticky Role")
            self.store.delete_user_role(member.id, role.role_id)
