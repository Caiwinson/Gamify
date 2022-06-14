import discord
from discord.ext import commands
from discord_components import Button,ButtonStyle
import random
from tool.database import get, post
import os
games=[]
from tool.log import log
for i in os.listdir("games"):
    if i.endswith(".py") and not i.startswith("ignore"):
        exec(f'from games.{i.replace(".py", "")} import {i.replace(".py", "")}')
        games.append(eval(i.replace(".py", "")))

class Verify(commands.Cog, name="verify"):
    def __init__(self, client):
        self.client=client
    @commands.Cog.listener()
    async def on_button_click(self,res):
        def check(self, i):
            return i.message==msg
        if not res.channel or not res.guild:
            return
        data=get(res.guild.id)
        if res.channel.id!=data["channel"]:
            await res.respond(type=4, content="invalid channel")
            return
        elif res.channel.id==data["channel"] and res.message.id!=data["message"]:
            await res.respond(type=4, content="invalid message")
            return
        if "ignore" in data:
            for i in res.author.roles:
                if i.id in data["ignore"]:
                    await res.respond(type=4, content="You are not permitted to verify")
                    return
        try:
            msg=await res.author.send("Are you ready", components=[Button(label="Yes", style=ButtonStyle.green)])
        except discord.errors.Forbidden:
            await res.respond(type=4, content="Please enable DM.")
            return
        await res.respond(type=4, content="Check your DM")
        ctx=await self.client.wait_for("button_click", check=lambda i: i.message==msg)
        await ctx.respond(type=6)
        result=await random.choice(games)(ctx, msg)
        await log(res, result)
        if result=="Success":
            if "roles" in data:
                for i in data["roles"]:
                    try:
                        await res.author.add_roles(res.guild.get_role(i), reason="Verification Successful")
                    except discord.errors.Forbidden:
                        i=res.guild.get_role(i).name
                        await res.author.send("I do not have access to give you the role {}\nContact the server owner".format(i))
            if res.author.id in data["member"]:
                data["member"].remove(res.author.id)
                post(res.guild.id, data)
def setup(client):
    client.add_cog(Verify(client))
    print("Verify loaded")