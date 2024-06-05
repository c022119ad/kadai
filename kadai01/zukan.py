import sys


class Monster:
    def __init__(self, id_, name, spec, types):
        self.id_ = id_
        self.name = name
        self.spec = spec
        self.types = types
    
    def set_stats(self,stats):
        self.stats = stats
        

    def __repr__(self):
        return f"番号：{self.id_}\n名前：{self.name}\nぶんるい：{self.spec}\nタイプ：{self.types}\n種族値：{sum(self.stats)}{self.stats}"


file_path = sys.argv[1]  # data/poke_names.txt
with open(file_path, "r", encoding="utf8") as rfo:
    monsters = list()
    for row in rfo:
        id_, name, spec, *types = row.rstrip().split("\t")
        monsters.append(Monster(id_, name, spec, types))

file_path = sys.argv[2]  # data/base_stats.txt
with open(file_path,"r",encoding="utf_8") as rfo:
    stats=list()
    for i , row in enumerate(rfo,0):
    
    
    #for row in rfo2:
        row = row.rstrip()
        stats.append([int(col) for col in row.split(" ")])
        
        
        monsters[i].set_stats(stats[i])
id_ = int(sys.argv[3])-1
print(monsters[id_])