import discord
from discord.ext import commands
from tool.embed import embed
from tool.database import get, post
from discord_components import Button, ButtonStyle

class Change(commands.Cog, name="Change"):
    def __init__(self, client):
        self.client=client
    @commands.Cog.listener()
    async def on_select_option(self, res):
        data=get(res.guild.id)
        select=res.values[0]
        def check(i):
            return i.author==res.author and i.channel==res.channel
        if not res.message.content.endswith(str(res.author.id)):
            await res.respond(type=4, content="Only <@{}> can change the bot setting with this message".format(res.message.content.split()[-1]))
            return
        if select not in ["Kick unverified members", "Verification message", "Invite kicked unverified members"]:
            await res.respond(type=6)
            if select=="Verification channel":
                e=discord.Embed(title="Mention the new Verification channel you want to change here.",description="Example:").set_image(url="https://cdn.discordapp.com/attachments/887944021627002891/983372406573895740/unknown.png")
                await res.message.reply(content=res.author.mention,embed=e)
                msg=await self.client.wait_for("message", check=check)
                if msg.channel_mentions==[]:
                    await msg.reply("No Channel mentioned\nHow to mention channel: #(channel name)")
                    return
                else:
                    data["channel"]=msg.channel_mentions[0].id
                    try:
                        message=await msg.channel_mentions[0].send(f"Welcome to {res.guild.name}!\nPress the button below to get started", components=[Button(label="Verify", style=ButtonStyle.green)])
                    except discord.errors.Forbidden:
                        await res.message.reply("I do not have access to send message in <#{}>".format(data["channel"]))
                    data["message"]=message.id
            elif select=="Reward Role":        
                e=discord.Embed(title="Mention Roles awarded for passing the verification process,\n\nNote: recommended that reward role are not permitted to view the verification channel", description="Example: you can mention more than one Roles or Type 'None' to clear.").set_image(url="https://cdn.discordapp.com/attachments/887944021627002891/983378003260239912/unknown.png")
                await res.message.reply(content=res.author.mention,embed=e)
                msg=await self.client.wait_for("message", check=check)
                if msg.role_mentions!=[]:
                    data["roles"]=[r.id for r in msg.role_mentions]
                else:
                    data["roles"]=[]
            elif select=="Log channel":
                e=discord.Embed(title="Mention the log channel here",description="Example: type `None` to clear").set_image(url="https://cdn.discordapp.com/attachments/974944747019968532/985417312851095592/unknown.png")
                await res.message.reply(content=res.author.mention,embed=e)
                msg=await self.client.wait_for("message", check=check)
                if msg.channel_mentions!=[]:
                    data["log"]=msg.channel_mentions[0].id
                else:
                    data["log"]=None
            elif select=="Ignore Role":
                e=discord.Embed(title="Mention the Role to ignore here", description="Example: you can mention more than one Roles or Type 'None' to clear.").set_image(url="https://cdn.discordapp.com/attachments/974944747019968532/985418637659762768/unknown.png")
                await res.message.reply(content=res.author.mention,embed=e)
                msg=await self.client.wait_for("message", check=check)
                if msg.role_mentions!=[]:
                    data["ignore"]=[r.id for r in msg.role_mentions]
                else:
                    data["ignore"]=[]
            await msg.add_reaction("✅")
            post(res.guild.id, data)
            await res.message.edit( embed=embed(res, res.guild.id))
        else:
            if select=="Verification message":
                try:
                    message= await self.client.get_channel(data["channel"]).send(f"Welcome to {res.guild.name}!\nPress the button below to get started", components=[Button(label="Verify", style=ButtonStyle.green)])
                except discord.errors.Forbidden:
                    await res.respond(type=4, content="I do not have access to send message in <#{}>".format(data["channel"]))
                    return
                data["message"]=message.id
            elif select=="Kick unverified members":
                data["kick"]=not data["kick"]
            elif select=="Invite kicked unverified members":
                data["invite"]=not data["invite"]
            post(res.guild.id, data)
            await res.respond(type=7, embed=embed(res, res.guild.id))
        
def setup(client):
    client.add_cog(Change(client))
    