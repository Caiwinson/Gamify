from discord_components import Button, ButtonStyle
from __main__ import client
import time
async def popit(res, msg):
    count=0
    b=[]
    for i in range(5):
        a=[]
        for j in range(5):
            count+=1
            a.append(Button(label=str(count), style=ButtonStyle.green))
        b.append(a)
    await msg.edit(content="Click all these buttons in under 1 minute.", components=b)
    t=time.time()
    def check(ctx):
        return ctx.message==msg
    while True:
        ctx=await client.wait_for('button_click', check=check)
        for i in range(5):
            for j in range(5):
                if b[i][j].label==ctx.component.label:
                    b[i][j].style=ButtonStyle.red
                    b[i][j].disabled=True
                    break
        count-=1
        if count>0:
            await ctx.respond(type=7, components=b)
        else:
            break
    if time.time()-t<=60:
        await ctx.respond(type=7, content="Verification Successful",components=b)
        return "Success"
    else:
        await ctx.respond(type=7, content="Verification Fail",components=b)
        return "Fail"