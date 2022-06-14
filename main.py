#Import module
import discord
from discord.ext import commands
from tool.config import config
from discord_components import DiscordComponents

#discord client
intents = discord.Intents.default()
intents.guilds=True
intents.messages=True
intents.members=True
client=commands.Bot(command_prefix=config["Client"]["prefix"], intents=intents)
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
#run client 
if __name__=='__main__':
    client.run(config["Client"]["token"])
