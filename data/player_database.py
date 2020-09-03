import yaml
import os

with open(os.path.dirname(os.path.abspath(__file__)) + '/../saves/player.yaml') as file:
    obj = yaml.safe_load(file.read())


class Player_database:
    def __init__(self, user_id):
        self.user_id = user_id

    # * ==================================================
    # * 
    # *    Player の コイン関係
    # *  
    # * ==================================================
    # コインを取得
    def get_coin(self):
        global obj 

        #
        # 初期
        #
        if obj['player'] is None:
            obj['player'] = {}

        if not str(self.user_id) in obj['player']:
            obj['player'][str(self.user_id)] = {}
            obj['player'][str(self.user_id)]['coin'] = 0

        #if obj['player'][str(self.user_id)]:

        self.save()

        return int(obj['player'][str(self.user_id)]['coin'])

    # コインをセット
    def set_coin(self, amount):
        global obj
        amount = int(amount)
        # 初期
        if obj['player'][str(self.user_id)] is None:
            obj['player'][str(self.user_id)] = {}
        
        if amount < 0:
            amount = 0

        obj['player'][str(self.user_id)]['coin'] = int(amount)
        self.save()
    
    # コインを増減
    def add_coin(self, amount):

        now = self.get_coin()
        self.set_coin(now + int(amount))

    # yamlのセーブ
    @staticmethod
    def save():
        with open(os.path.dirname(os.path.abspath(__file__)) + '/../saves/player.yaml', mode='w') as f:
            f.write(yaml.dump(obj, default_flow_style=False))
