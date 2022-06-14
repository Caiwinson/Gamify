import discord
from discord.ext import commands, tasks
import random
class Status(commands.Cog, name="status"):
    def __init__(self, client):
        self.client=client
        self.recent=""
        self.status.start()
    @tasks.loop(seconds=30)
    async def status(self):
        while True:
            s=["Pop it", "Colour","Math", "Name this Game","gv!help", "member", "guild"]
            c=random.choice(s)
            if c!=self.recent:
                if c=="guild":
                    ac=discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.client.guilds)} guilds")
                elif c=="member":
                    cc=0
                    for i in self.client.guilds:
                        cc+=len(i.members)
                    ac=discord.Activity(type=discord.ActivityType.watching, name=f"{cc} members")
                else:
                    ac=discord.Game(c)
                self.recent=c
                await self.client.change_presence(activity=ac)
                break

def setup(client):
    client.add_cog(Status(client))
    print("Status loaded")