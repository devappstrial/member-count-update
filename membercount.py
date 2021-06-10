import os
from asyncio import sleep
from discord.ext import commands

class MemberCount(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.wait_until_ready()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        allmembers = self.client.get_channel('''All members count channel id''')
        bots = self.client.get_channel('''Bot count channel id''')
        members = self.client.get_channel('''Human count channel id''')
        guild = self.client.get_guild('''discord server id''')
        await allmembers.edit(name=f'All Members: {int(len(member.guild.members))}')
        bcount = int(len(list(filter(lambda m: m.bot, member.guild.members))))
        mcount = int(len(list(filter(lambda m: not m.bot, member.guild.members))))
        await bots.edit(name = f'Bots: {bcount}')
        await members.edit(name=f'Members: {mcount}')
        print("Count Updated")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        allmembers = self.client.get_channel('''All members count channel id''')
        bots = self.client.get_channel('''Bot count channel id''')
        members = self.client.get_channel('''Human count channel id''')
        guild = self.client.get_guild('''discord server id''')
        await allmembers.edit(name=f'All Members: {int(len(member.guild.members))}')
        bcount = int(len(list(filter(lambda m: m.bot, member.guild.members))))
        mcount = int(len(list(filter(lambda m: not m.bot, member.guild.members))))
        await bots.edit(name = f'Bots: {bcount}')
        await members.edit(name=f'Members: {mcount}')
        print("Count Updated")

def setup(client):
    client.add_cog(MemberCount(client))
    print("Member Count Cog is loaded")
