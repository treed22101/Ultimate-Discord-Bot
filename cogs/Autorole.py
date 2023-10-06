import discord
from discord.ext import commands

class Autorole(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Autorole.py is online.")
        print('______________________')


#auto role, local only
    @commands.Cog.listener()
    async def on_member_join(self, member):
        join_role = discord.utils.get(member.guild.roles, name='Friend')
        await member.add_roles(join_role)





async def setup(client):
    await client.add_cog(Autorole(client))