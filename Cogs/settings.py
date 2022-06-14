from discord.ext import commands
from discord_components import Select, SelectOption
from tool.embed import embed
from tool.database import get

class Settings(commands.Cog, name="Settings"):
    def __init__(self, client):
        self.client=client
    @commands.command(name="settings", aliases=["Settings"])
    async def settings(self, ctx):
        data=get(ctx.guild.id)
        perm=ctx.author.guild_permissions
        if perm.manage_guild is False or perm.manage_roles is False:
            await ctx.send(f"You don't have the Permission:\nManage Guild: {perm.manage_guild}\nManage Roles: {perm.manage_roles}")
            return
        if data is None:
            await ctx.send("Your guild haven't been setup yet\nPls run `gv!setup`")
            return
        options=[SelectOption(label=i, value=i) for i in ["Verification channel", "Verification message", "Reward Role", "Log channel", "Ignore Role", "Kick unverified members", "Invite kicked unverified members"]]
        await ctx.reply(content=f"user id: {ctx.author.id}",embed=embed(ctx,ctx.guild.id), components=[Select(placeholder="Pick which to change", options=options)])
def setup(client):
    client.add_cog(Settings(client))
    print("Settings loaded")