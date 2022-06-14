import random
from discord import Embed
from discord_components import Button, ButtonStyle
from __main__ import client 
data=[]
async def get():
    if data==[]:
        channel=client.get_channel(985699818439598100)
        data_r=await channel.history(limit=200).flatten()
        for d in data_r:
            data.append([d.attachments[0].url, d.content])
    return random.sample(data,5)

async def ntg(res, msg):
    data=await get()
    picked=random.choice(data)
    buttons=[] 
    embed=Embed(title="Name this Game").set_image(url=picked[0])
    for i in data:
        buttons.append(Button(label=i[1],style=ButtonStyle.blue))
    await msg.edit(content="", embed=embed, components=buttons)
    ctx=await client.wait_for("button_click", check=lambda i: i.message==msg)
    if ctx.component.label==picked[1]:
        embed=Embed(title="Verification Succesful", description=picked[1], colour=0x00ff00).set_image(url=picked[0])
        tf="Success"
    else:
        embed=Embed(title="Verification Failed", description=picked[1], colour=0xff0000).set_image(url=picked[0]).set_footer(text="You pick "+ctx.component.label)
        tf="Fail"
    await ctx.respond(type=7,embed=embed, components=[])
    return tf
@client.command()
async def reload(ctx):
    if ctx.author.id==720900711260487681:
        global data
        data=[]
        await get()

