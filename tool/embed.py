import discord
from tool.database import get
def embed(ctx,guild):
    data=get(guild)
    embed=discord.Embed(title="Settings")
    embed.add_field(name="Verification channel", value="<#{}>".format(data["channel"]))
    embed.add_field(name="Verification message", value=f"[Message Link](https://discord.com/channels/{ctx.guild.id}/{data['channel']}/{data['message']})", inline=False)
    if "roles" in data:
        r="\n".join([ctx.guild.get_role(i).mention for i in data["roles"]])
    else:
        r="None"
    embed.add_field(name="Reward Role", value=r,inline=False)
    if "log" in data:
        log="<#{}>".format(data["log"])
    else:
        log="None"
    embed.add_field(name="Log channel", value=log,inline=False)
    if "ignore" in data:
        ignore="\n".join([ctx.guild.get_role(i).mention for i in data["ignore"]])
    else:
        ignore="None" 
    embed.add_field(name="Ignored Role", value=ignore, inline=False)
    embed.add_field(name="Kick unverified members", value=str(data["kick"]), inline=False)
    embed.add_field(name="Invite kicked unverified members", value="`Must have \"Kick unverified members\" set to True`\n"+str(data["invite"]), inline=False)
    return embed