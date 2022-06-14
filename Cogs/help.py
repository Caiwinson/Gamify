import discord
from discord.ext import commands
class Help(commands.Cog, name="Help"):
    def __init__(self, client):
        self.client=client
        self.client.remove_command("help")
    @commands.command(name="help", aliases=["Help"])
    async def help(self, ctx):
        embed=discord.Embed(title="Help")
        embed.add_field(name="Setup",value="Setup Guild settings for bot to work.\n\nPermission: Manage Guild, Manage Roles")
        embed.add_field(name="Settings", value="Change Guild settings.\n\nPermission: Manage Guild, Manage Roles\nGuild must be setup",inline=False)
        await ctx.send(embed=embed)
def setup(client):
    client.add_cog(Help(client))
    print("Help loaded")

