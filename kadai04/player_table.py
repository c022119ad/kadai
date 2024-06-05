import sys
import functools
def num_rows(func):
    @functools.wraps(func)
    
    def _func(t):
        print(f"{len(func(t))}件該当しました")
        return(func(t))
    return _func

def select_team(team_name):
    def _team(func):
        def _select(t):
            
            new_lst =[i for i in func(t) if i.team == team_name]
            return new_lst                  
        return _select
    return _team

def tag_decorator(tag_,deri,chara):
    def _decorator(func):
        def _tag(t):
            anslst = []
            for j in range(len(func(t))):
                anslst.append(func(t)[j])
                anslst[j][-1].append(deri)
            count = 0
            for k in anslst:
                for l in anslst:
                    pass

class Player:
    def __init__(self, name, team, values):
        self.name = name
        self.team = team

        self.values = values

    def __repr__(self):
        return "\t".join([self.name, self.team]+self.values[:6])  # Name Team G PA HR R RBI SB

@num_rows
@select_team(sys.argv[2])
@num_rows
def read_stats(file_path):
    players = list()
    with open(file_path, "r") as rfo:
        headers = rfo.readline().rstrip().split(",")
        for row in rfo:
            _, name, team, *values = row.rstrip().split(",")
            players.append(Player(name, team, values))
    return players

        


def concat_strs(lst):
    return "\n".join(lst)    



if __name__ == "__main__":
    players = read_stats(sys.argv[1])  # data/mlb_players.txt
    
    print
    #concat_strs([player.__repr__() for player in players])
    #print(concat_strs)