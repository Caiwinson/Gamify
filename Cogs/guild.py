import discord
from discord.ext import commands
class Guild(commands.Cog, name="Guild join"):
    def __init__(self, client):
        self.client=client

    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        channels=guild.text_channels
        embed=discord.Embed(title="Thank you for inviting!", description="Thank you for inviting Gamify to {}!.\nTo get started type `gv!help` for more info\n\n`Incase you forgot the bot prefix, just ping the Bot.`".format(guild.name)).set_author(name="Gamify", icon_url="https://cdn.discordapp.com/avatars/909367670833561600/ae7b0acc222c2c9cda70d051357ff20a.png?size=1024")
        for c in channels:
            try:
                await c.send(embed=embed)
            except:
                continue
            else:
                break
def setup(client):
    client.add_cog(Guild(client))
    print("Guild loaded")
