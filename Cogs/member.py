from discord.ext import commands
import asyncio
from tool.log import log
from tool.database import get, post
class Member(commands.Cog, name="member"):
    def __init__(self, client):
        self.client=client
    @commands.Cog.listener()
    async def on_member_join(self, member):
        data=get(member.guild.id)
        if data is not None and not member.bot and data["kick"] is True:
            if member.id not in data["member"]:
                data["member"].append(member.id)
                post(member.guild.id, data)
            await asyncio.sleep(600)
            data=get(member.guild.id)
            if member.id in data["member"]:
                data["member"].remove(member.id)
                await log(member, "Kick")
                invite=""
                if data["invite"] is True:
                    try:
                        invite=await self.client.get_channel(data["channel"]).create_invite(max_uses=1, reason="10 minutes of being unverified")
                    except:
                        pass
                try:
                    await member.send(f"You have been kicked from {member.guild.name}.\n\nReason: 10 minutes of being unverified \n\n{invite}")
                except:
                    pass
                await member.kick(reason="10 minutes of being unverified")
            post(member.guild.id, data)
def setup(client):
    client.add_cog(Member(client))