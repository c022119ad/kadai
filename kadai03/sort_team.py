import sys


class Player:
    def __init__(self, name, team, war):
        self.name = name
        self.team = team
        self.war  = war

    def __repr__(self):
        return f"name: {self.name}\tteam: {self.team}\twar:  {self.war}"

def read_stats(file_name):
    with open(file_name,"r",encoding="utf_8") as rf:
        lst = []
        for i , row in enumerate(rf):
            row =row[:-1].split(',')
            if not row[2] == "---" and i  != 0:
                name, team,war = row[1],row[2],row[-1]
                lst.append(Player(name,team,war))
        return lst
            
def etc_war(player):

    
    if float(player.war) > 1.0:
        return True
    else:
        return False

if __name__ == "__main__":
    players = read_stats(sys.argv[1])  # data/mlb_players.txt
    players.sort(key=lambda pla:float(pla.war),reverse=True)
    etc_players = filter(etc_war,players)
    dic = {}
    for j ,team_ in enumerate(etc_players):
        print(f"{j+1} {team_}")
        if not  team_.team in dic:
            dic[team_.team] = 1
        else:
            dic[team_.team] += 1
    sort_dic = sorted(dic.items(),key =lambda tpl:tpl[1],reverse=True)
    for k,val in enumerate(sort_dic):
        print(f"{k+1},{val}")