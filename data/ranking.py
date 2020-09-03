import os
import yaml


#
# 順位Nからユーザーidを取得
#
def get_id(num):
    with open(os.path.dirname(os.path.abspath(__file__)) + '/../saves/player.yaml') as file:
        obj = yaml.safe_load(file.read())

    user_coin = {}
    for user in obj['player'].items():
        user_coin[user[0]] = obj['player'][user[0]]['coin']

    user_coin = sorted(user_coin.items(), key=lambda x: x[1], reverse=True)

    return user_coin[num-1][0]


#
# ユーザーidから順位を取得
#
def get_rank(user_id):
    i = 0
    while True:
        i += 1
        if int(get_id(i)) == int(user_id):
            return i
