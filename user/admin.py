from discord.ext import commands
import sys
from data import player_database
import function
sys.path.append('../')


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
        #
        # 長さ 1~
        #
        if args[0] == 'help':
            await self.help(channel)
            return

        #
        # 長さ 3~
        #

        # /c admin add <メンション> <数字>
        if args[0] == 'add':
            # 追加の処理
            user_id = int(function.mention_to_id(args[1]))
            amount = args[2]

            player_database_class = player_database.Player_database(user_id)
            player_database_class.add_coin(amount)

            # メッセージ
            await channel.send(':o:**>** You send ' + amount + 'TC to ' + args[1])

        # /c admin set <メンション> <数字>
        if args[0] == 'set':
            # 追加の処理
            user_id = int(function.mention_to_id(args[1]))
            amount = args[2]

            player_database_class = player_database.Player_database(user_id)
            player_database_class.set_coin(amount)

            # メッセージ
            await channel.send(':o:**>** set ' + args[1] + ' ' + str(amount) + 'TC')

    # *
    # * HELP
    # *
    @staticmethod
    async def help(channel):
        emoji_diamond = ':diamond_shape_with_a_dot_inside:'
        await channel.send(
            '**==< ' + emoji_diamond + '  ThisCoin Admin  ' + emoji_diamond + ' >==** \n'
            + '> `/c admin add @ <amount>` - コインを増減させる \n'
            + '> `/c admin set @ <amount>` - コインをセットする'
        )


def setup(client):
    client.add_cog(Admin(client))
