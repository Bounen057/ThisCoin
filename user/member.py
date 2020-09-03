import discord
from discord.ext import commands
import sys
import yaml
import os
import function
from data import ranking
from data import player_database
sys.path.append('../')


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
    @staticmethod
    async def help_message(channel):
        emoji_diamond = ':diamond_shape_with_a_dot_inside:'
        await channel.send(
            '**==< ' + emoji_diamond + '  ThisCoin  ' + emoji_diamond + ' >==** \n' +
            '> `/c profile` - プロフィール \n' +
            '> `/c pay @ <amount>` - TCを送る'
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

        embed.add_field(name=":full_moon: 所持TC:", value=str(player_database_class.get_coin()), inline=True)
        embed.add_field(name=":crown: TCランキング:", value=str(ranking.get_rank(sender.id)), inline=True)

        # await sender.send(embed=embed) 　DMに送信
        await ctx.message.channel.send(embed=embed)

    # *
    # *  コインを譲渡
    # *
    @commands.command(aliases=['p'])
    async def pay(self, ctx, *args):
        channel = ctx.message.channel

        # エラーチェック
        if len(args) != 2 or not function.is_int(args[1]):
            await channel.send(':x: **>  /c pay @<mention> <数字>**')
            return

        if not function.is_int(function.mention_to_id(args[0])):
            await channel.send(':x: **>  そのユーザーは登録されていません**')
            return

        # 変数
        amount = int(args[1])
        sender = ctx.message.author
        sender_coin = player_database.Player_database(sender.id)
        receiver = function.mention_to_id(args[0])
        receiver_coin = player_database.Player_database(receiver)

        if amount < 1 or amount > sender_coin.get_coin():
            await channel.send(':x: **>  無効な値が入力されました**')
            return

        # コイン関係の処理
        sender_coin.add_coin(-1 * amount)
        receiver_coin.add_coin(amount)

        await channel.send(':moneybag: **> ' + str(amount) + 'TC => **' + args[0])

    # *
    # * ランキング
    # *
    @commands.command()
    async def top(self, ctx, *args):
        channel = ctx.message.channel

        top_user = [self.client.get_user(int(ranking.get_id(i))) for i in range(6)]
        top_user_coin = [str(player_database.Player_database(top_user[i].id).get_coin()) for i in range(6)]

        await channel.send(
                           '**= = = ===-=- :crown:  Top Users  :crown: -=-=== = = =** \n'
                           ' \n'
                           ':first_place:  **1位**     ' + top_user[1].name + '      `' + top_user_coin[1] + 'TC`\n'
                           ':second_place:  **2位**     ' + top_user[2].name + '      `' + top_user_coin[2] + 'TC`\n'
                           ':third_place:  **3位**     ' + top_user[3].name + '      `' + top_user_coin[3] + 'TC`\n'
                           ':medal:  **4位**     ' + top_user[4].name + '      `' + top_user_coin[4] + 'TC`\n'
                           ':medal:  **5位**     ' + top_user[5].name + '      `' + top_user_coin[5] + 'TC`\n'
                           ' \n'
                           '**= = = = = = = = = = = = = = = = = = = = = = = = = =**'
                           )


def setup(client):
    client.add_cog(Member(client))
