import sys
import itertools

class Player:
    def __init__(self, name, team, avg):
        self.name = name
        self.team = team
        self.avg  = avg

    def __repr__(self):
        return f"name: {self.name}\tteam: {self.team}\tavg:  {self.avg}"
    

def read_stats(file_path):
    with open(file_path,"r",encoding="utf_8") as rfo:
        headers = rfo.readline().rstrip().split(",")
        plylst = []
        for row in rfo:
            row = row.rstrip().split(",")
            name, team, AVG = row[1],row[2],float(row[13])
            yield(Player(name,team,AVG))
    #return plylst


def check_order(lst):
    new = list(lst)
    for i in range(len(new)):
        swich = 1
        
        for j in range(4):
            if new[i][j].avg < new[i][j+1].avg:
                swich = 0
        if swich :
            yield tuple(new[i])
    

if __name__ == "__main__":
    ch = check_order(itertools.permutations(list(filter(lambda x: x.team == sys.argv[2] and x.avg > 0 ,read_stats(sys.argv[1]) )),5))  
    for i , num in enumerate(ch):
        print("-------------")
        print(f"{i+1}番目")
        for j in range(5):
            print(j+1,num[j])