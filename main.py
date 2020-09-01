import discord
from discord.ext import commands

# 変数
TOKEN = 'NTA5Mzc2NjEyNzk0NjMwMTQ0.W-Gn8A.0vWtZuVn8cLWhjho72oqhjTAetY'
client = commands.Bot(command_prefix='/c ')
extensions = ['user.member','user.admin']

class Main:
    @client.event
    async def on_ready():
        print('=================')
        print('>   Connected!')
        print('=================')

if __name__ == '__main__':
    for obj in extensions:
        client.load_extension(obj)
    client.run(TOKEN)