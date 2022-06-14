from discord.ext import commands
class Error(commands.Cog, name="Error"):
    def __init__(self,client):
        self.client=client
    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.reply("Unknown command")
    @commands.Cog.listener()
    async def on_message(self, message):
        if "<@909367670833561600>" in message.content:
            await message.reply("The bot prefix is `gv!`")
def setup(client):
    client.add_cog(Error(client))
    
            