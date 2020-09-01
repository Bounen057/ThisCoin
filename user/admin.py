import discord
from discord.ext import commands

from data import player_database 
from .. import function

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # *
    # * 管理者専用コマンド
    # *
    @commands.command()
    async def admin(self, ctx, *args):
        # チャンネル
        channel = ctx.message.channel

        # 本人確認処理
        if ctx.author.id != 321266537266806784:
            await channel.send(':x: **>  あなたは権限を持っていません**')
            return
        
        if len(args) == 0:
            await self.help(channel)
            return

        # 長さ 1~

        if args[0] == 'help':
            await self.help(channel)
            return

        # 長さ 3~

        # /c admin add <メンション> <数字>
        if args[0] == 'add':
            # 変数
            id = int(function.MentionToID(args[1]))
            amount = args[2]

            player_database_class = player_database.Player_database(id)
            add_coin(amount)


    # *
    # * HELP
    # *
    async def help(self, channel):
        emoji_diamond = ':diamond_shape_with_a_dot_inside:'
        await channel.send(
        '**==< ' + emoji_diamond + '  ThisCoin Admin  ' + emoji_diamond + ' >==** \n' +
        '> くらふせば〜か！'
        )

def setup(client):
    client.add_cog(Admin(client))