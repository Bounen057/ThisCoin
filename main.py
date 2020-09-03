from discord.ext import commands

# 変数
TOKEN = ''
client = commands.Bot(command_prefix='/c ')
extensions = ['user.member', 'user.admin']


@client.event
async def on_ready():
    print('=================')
    print('>   Connected!')
    print('=================')


if __name__ == '__main__':
    for obj in extensions:
        client.load_extension(obj)

    client.run(TOKEN)
