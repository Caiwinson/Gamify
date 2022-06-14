#Import module
import discord
from discord.ext import commands
from replit import db
import os
import requests
from keep_alive import keep_alive
from discord_components import DiscordComponents

#discord client
intents = discord.Intents.default()
intents.guilds=True
intents.messages=True
intents.members=True
client=commands.Bot(command_prefix=["gv!", "Gv!", "GV!", "<@909367670833561600> "], intents=intents)
DiscordComponents(client)
#load cogs
def load():
    cogs=[x.replace(".py", "") for x in os.listdir("Cogs")]
    cogs.remove("__pycache__")
    for cog in cogs:
        try:
            client.load_extension("Cogs."+cog)
        except Exception as exp:
            print(f"{cog} failed to load: {exp.args[0]}")
@client.event
async def on_ready():
    load()
    print(client.user)
@client.command()
async def rint(ctx,*,command):
    if ctx.author.id!=720900711260487681:
        return
    try:
        pr=eval(command)
    except Exception as ex:
        pr=f"{type(ex).__name__}: {ex.args[0]}"
    await ctx.reply(pr)
@client.command()
async def run(ctx, *,command):
    if ctx.author.id==720900711260487681:
        try:
            exec(command)
        except Exception as ex:
            await ctx.reply(f"{type(ex).__name__}: {ex.args[0]}")
        else:
            await ctx.message.add_reaction("✅")
#run client 
if requests.get("https://verify.caiwinson.repl.co").text!="200":
    keep_alive()
    try:
        client.run(db["token"])
    except Exception as exp:
        a=exp
