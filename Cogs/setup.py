import discord
from discord.ext import commands
from discord_components import Button,ButtonStyle
from tool.database import post
from tool.embed import embed as Embed
class AddSetup(commands.Cog, name="setup command"):
    def __init__(self, client):
        self.client=client
    @commands.command(name="setup")
    async def _setup(self, ctx):
        data={}
        def check(m):
            return m.channel==ctx.channel and m.author==ctx.author
        perm=ctx.author.guild_permissions
        if perm.manage_guild is False or perm.manage_roles is False:
            await ctx.send(f"You don't have the Permission:\nManage Guild: {perm.manage_guild}\nManage Roles: {perm.manage_roles}")
            return
        embed=discord.Embed(title="Please make an verification channel and mention it here.",description="Example: Channel can be named anything.").set_image(url="https://cdn.discordapp.com/attachments/887944021627002891/983372406573895740/unknown.png")
        await ctx.reply(embed=embed)
        msg=await self.client.wait_for("message", check=check)
        if msg.channel_mentions==[]:
            await msg.reply("No Channel mentioned\nHow to mention channel: #(channel name)\n\nPlease run gv!setup again")
            return
        data["channel"]=msg.channel_mentions[0].id
        embed=discord.Embed(title="Mention Roles awarded for passing the verification process,\n\nNote: recommended that reward role are not permitted to view the verification channel", description="Example: you can mention more than one Roles or Type 'None' to skip.").set_image(url="https://cdn.discordapp.com/attachments/887944021627002891/983378003260239912/unknown.png")
        await msg.reply(embed=embed)
        role=await self.client.wait_for("message", check=check)
        if role.role_mentions!=[]:
            data["roles"]=[r.id for r in role.role_mentions]
        try:
            message=await msg.channel_mentions[0].send(f"Welcome to {ctx.guild.name}!\nPress the button below to get started", components=[Button(label="Verify", style=ButtonStyle.green)])
        except discord.errors.Forbidden:
            await msg.reply("I do not have access to send message in {}".format(msg.channel_mentions[0].mention))
        data["message"]=message.id
        data["kick"]=False
        data["invite"]=False
        post(ctx.guild.id, data)
        embed=Embed(ctx, ctx.guild.id)
        embed.title="Bot setup complete"
        embed.description="Please run `gv!settings next`."
        await role.reply(embed=embed)
def setup(client):
    client.add_cog(AddSetup(client))
    print("Setup loaded")