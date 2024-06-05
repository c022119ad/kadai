import random
import sys


class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team

    def __repr__(self):
        return f"{self.name}({self.team})"


class Team:
    def __init__(self, file_path, team_name):
        self.name = team_name
        members = __class__.read_stats(file_path, self.name)  # 全メンバー
        self.stamems = [members[random.randint(0,len(members)-1)] for k in range(9)]  # スタメン
    def __iter__(self) :
        return TeamIterator(self) 
    
    def __repr__(self):
        s1 = "---"+self.name+"-"*7+"\n"
        s2 = "\n".join([f"{p+1}:{player.name}" for p, player in enumerate(self.stamems)])
        s3 = "\n"+"-"*13
        return s1+s2+s3

    @staticmethod
    def read_stats(file_path, team_name):
        with open(file_path,"r",encoding="utf_8") as rfo:
            headers = rfo.readline().rstrip().split(",")
            plylst = []
            for row in rfo:
                row = row.rstrip().split(",")
                name, team = row[1],row[2]
                if row[2] == team_name:
                    plylst.append(Player(name,team))
        return plylst
            
    

class TeamIterator:
    def __init__(self,Team):
        self.source = Team
        self.idx = 0
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count == 3:
            self.count = 0
            raise StopIteration()
        
        
        if self.idx == len(self.source):
            self.idx = 0
        
        name = self.source[self.idx]
        self.idx += 1
        a = random.random()
        if a > 0.5:
            self.count += 1
        return name


if __name__ == "__main__":
    team1 = Team(sys.argv[1], sys.argv[2])  # data/mlb_players.txt NYY
    team2 = Team(sys.argv[1], sys.argv[3])  # data/mlb_players.txt LAA
    print(team1)
    print(team2)
    iter1 = iter(team1)
    iter2 = iter(team2)

    print("- Play ball.")
    for inning in range(5):
        print(f"-- Inning {inning+1}")
        """ team1の攻撃 """
        for i , z in enumerate(TeamIterator(team1.stamems)):
            print(i+1,z)
        print(f"--- Three out.")
        """ team2の攻撃 """
        for j , a in enumerate(TeamIterator(team2.stamems)):
            print(j+1,a)
        print(f"--- Three out.")
    print("- Game set.")