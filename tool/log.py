import discord
from __main__ import client
from tool.database import get
async def log(res, tf):
    data=get(res.guild.id)
    if data is None:
        return
    if "log" not in data:
        return
    if tf=="Success":
        embed=discord.Embed(description=f"**{res.author.mention} has succesfully verify to {res.guild.name}!**", colour=0x00ff00).set_thumbnail(url=res.author.avatar_url)
    elif tf=="Fail":
        embed=discord.Embed(description=f"**{res.author.mention} has failed to verify.**\n\nReason: Failing the game given", colour=0xff0000).set_thumbnail(url=res.author.avatar_url)
    elif tf=="Kick":
        embed=discord.Embed(description=f"**{res.mention} has been kicked.**\n\nReason: 10 minutes of uninteraction after joining", colour=0xffa500).set_thumbnail(url=res.avatar_url)
    await client.get_channel(data["log"]).send(embed=embed)
    