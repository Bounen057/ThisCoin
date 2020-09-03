from data import player_database
import yaml
import os


# Mention から ID
def mention_to_id(mention):
    mention = mention.replace('<', '')
    mention = mention.replace('>', '')
    mention = mention.replace('!', '')
    mention = mention.replace('@', '')

    return mention


# int型に変換できるか
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# 指定したIDのプレイヤーが存在しているかどうか
# True = 存在している / False = 存在していない
#
def id_check(user_id):
    with open(os.path.dirname(os.path.abspath(__file__)) + '/saves/player.yaml') as file:
        obj = yaml.safe_load(file.read())

    try:
        obj['player'][str(user_id)]['coin']
    except KeyError:
        return False

    return True
