import sys


def mean(stats):
    cal = 0
    for i in range(0,6):
        cal += stats[i]
    ans = cal/ 6
    return ans
        
    


def norm(stats):
    cal = 0
    for i in range(0,6):
        cal += (stats[i])**2
    ans = cal**(1/2)
    return  ans


def normalize(stats):
    # リスト（ベクトル）を正規化（平均値を引き，ノルムで割る）する

    # 1. 平均値を求める
    cal = 0
    cal = mean(stats)
    new_stats = [0]*6
    staave = []
    for i in range(0,6):
        new_stats[i] = stats[i] - cal
    norcal = norm(new_stats)
    for j in range(0,6):
        new_stats[j] = new_stats[j]/norcal
    if new_stats[0] == 0 and new_stats[1] == 0.0 and new_stats[2] == 0 and new_stats[3] == 0 \
        and new_stats[4] == 0 and new_stats[5] == 0:
        for k in range(0,6):
            new_stats[k] = (1/(6**(1/2)))
    return new_stats
        
    # 2. statsの各要素から平均値を引く
    # 3. ノルムを求める
    # 4. statsの各要素をノルムで割る（例外が発生しうる）
    # 5. 4.で例外が発生した場合，statsの要素を全て 1/√6 にする
    # 6. 上記手順により正規化したstatsを返す


def corr_coef(stats1, stats2):
    nom_stats1=normalize(stats1)
    # 1. stats1を正規化する
    nom_stats2=normalize(stats2)
    # 2. stats2を正規化する
    nomcal = 0
    for i in range(len(nom_stats1)):
        nomcal += (nom_stats1[i]*nom_stats2[i])
    nomave1 =[0]*6
    nomave2 =[0]*6
    for i in range(0,6):
        nomave1[i] = nom_stats1[i]**2
        nomave2[i] = nom_stats2[i]**2
    nomave1 = sum(nomave1)
    nomave2 = sum(nomave2)
    a = nomave1**(1/2)
    b = nomave2**(1/2)
    concl = nomcal/(a*b)
    return concl
    # 3. stats1とstats2の内積を返す


class Monster:
    def __init__(self, id_, name, spec, types):
        self.id_ = id_
        self.name = name
        self.spec = spec
        self.types = types
    def set_stats(self,stats):
        self.stats=stats

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
print("-"*10)
max_ = 0
cal_ = 0
memo = 0
for i in range(len(monsters)):
    if not i == id_:
        cal_ = corr_coef(monsters[id_].stats,monsters[i].stats)
        #print(i,cal_)
    #print(i,(normalize(monsters[i].stats)),monsters[i].stats)
    #print()
    if cal_ > max_:
        max_ = cal_
        memo = i
#print(max_)
print(monsters[memo])