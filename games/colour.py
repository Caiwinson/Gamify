import asyncio
import random
import discord
from discord_components import Button
from __main__ import client

async def colour(res, msg):
    def check(i):
        return i.message==msg
    colours=["⚪", "⚫", "🔴", "🔵", "🟡", "🟢", "🟣", "🟤"]
    #pick 5 random circles
    picked_colours=random.sample(colours, 5)
    num=random.randint(3,5)
    order="".join(random.choices(picked_colours, k=num))
    embed=discord.Embed(title="Remember this, you have 5 seconds").add_field(name="⠀", value=order)
    await msg.edit( embed=embed, components=[], content="")
    await asyncio.sleep(5)
    buttons=[[]]
    for i in picked_colours:
        buttons[0].append(Button(label="⠀", emoji=i, custom_id=i))
    embed=discord.Embed(title="Your turn", description="Enter the order of the circles you saw")
    await msg.edit(embed=embed, components=buttons)
    ans=""
    for e in range(num):
        ctx=await client.wait_for('button_click',check=check)
        ans+=ctx.component.id
        if e+1<num:
            embed=discord.Embed(title="Your turn", description="Enter the order of the circles you saw").add_field(name="⠀", value=ans)
            await ctx.respond(type=7, embed=embed)
    if ans==order:
        embed=discord.Embed(title="You won", description="You got it right",colour=0x00ff00).add_field(name="⠀", value=ans)
        a="Verification successful"
        tf="Success"
    else:
        embed=discord.Embed(title="You lost", description="You got it wrong",colour=0xff0000).add_field(name="Your colours", value=ans).add_field(name="Correct colours", value=order)
        a="Verification Fail"
        tf="Fail"
    await ctx.respond(type=7, content=a,embed=embed, components=[])
    return tf