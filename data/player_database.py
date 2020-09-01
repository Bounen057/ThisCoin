import yaml
import os

with open(os.path.dirname(os.path.abspath(__file__)) + '/../saves/player.yaml') as file:
    obj = yaml.safe_load(file.read())

class Player_database:
    def __init__(self,id):
        self.id = id


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
        if obj['player']['coin'] is None:
            obj['player']['coin'] = {}
        
        if obj['player']['coin'][str(self.id)] is None:
            obj['player']['coin'][str(self.id)] = 1


        self.save()

        return obj['player']['coin'][str(self.id)]

    # コインをセット
    def set_coin(self, amount):
        global obj 
        # 初期
        if obj['player']['coin'] is None:
            obj['player']['coin'] = {}
        
        if amount < 0:
            amount = 0

        obj['player']['coin'][str(self.id)] = amount
        self.save()
    
    # コインを増減
    def add_coin(self, amount):
        now = get_coin()
        set_coin(now + amount)
    
    # yamlのセーブ
    def save(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/../saves/player.yaml', mode='w') as file:
            file.write( yaml.dump(obj, default_flow_style=False) )



