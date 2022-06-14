import random
import discord
from __main__ import client

async def math(res, msg):
    while True:
        question=[]
        for _ in range(random.randint(2,5)):
            a=""
            for _ in range(random.randint(1,3)):
                num=random.randint(0,9)
                if not f"{a}{num}".startswith("0"):
                    a=f"{a}{num}"
            if a!="":
                question.append(a)
        question="".join([a+random.choice(["+", "-","×", "÷"]) for a in question])[:-1]
        ans=eval(question.replace("×", "*").replace("÷", "/"))
        if ans>0 and "." not in str(ans):
            ans=str(ans)
            break
    embed=discord.Embed(title="Solve",description=question).set_footer(text="type the answer below (number only)")
    await msg.edit(embed=embed, components=[], content="")
    ctx=await client.wait_for("message", check=lambda i: i.author==res.author and not i.guild)
    if ctx.content==ans:
        embed=discord.Embed(title="Correct answer",description=f"{question}={ans}", colour=0x00ff00)
        tf="Success"
    else:
        embed=discord.Embed(title="Incorrect answer",description=f"{question}={ans}", colour=0xff0000).add_field(name="Your answer", value=ctx.content)
        tf="Fail"
    await msg.edit(embed=embed)
    return tf