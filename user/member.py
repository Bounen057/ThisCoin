import discord
from discord.ext import commands

from data import player_database 

class Member(commands.Cog):
    def __init__(self, client):
        self.client = client

    # メンションされたらHELP
    @commands.Cog.listener()
    async def on_message(self, message):
        if str(self.client.user.id) in message.content:
            await self.help_message(message.channel)

    @commands.command()
    async def h(self, ctx):
        await self.help_message(ctx.message.channel)

    # * 
    # *  Help を表示
    # *
    async def help_message(self,channel):
        emoji_diamond = ':diamond_shape_with_a_dot_inside:'
        await channel.send(
            '**==< ' + emoji_diamond + '  ThisCoin  ' + emoji_diamond + ' >==** \n' +
            '> `/c profile` - プロフィール'
            )

    # *
    # *  Profile を表示
    # *
    @commands.command()
    async def profile(self, ctx):
        # 送信者
        sender = ctx.message.author

        # 値を読み込む
        player_database_class = player_database.Player_database(sender.id)


        # 内容
        embed = discord.Embed(title="<< Your profile >>", description="", color=0x00c0eb)
        embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)

        embed.add_field(name=":full_moon: 所持TC:",value = str( player_database_class.get_coin() ),inline=True)

        await sender.send(embed = embed)



def setup(client):
    client.add_cog(Member(client))