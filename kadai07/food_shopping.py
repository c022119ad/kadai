import sys
from dataclasses import dataclass

@dataclass
class Food:
    def __init__(self,name,katego,maker,bra,day,price):
        self.name = name
        self.price = price
    def __repr__(self) :
        return f"name={self.name},price={self.price}"
    def __add__(self,other):
        return (self.price+other.price)
    def __radd__(self,other):
        return (int(self.price)+int(other))


def read_foods(file_path):
    lst = list()
    with open(file_path, "r", encoding="utf-8") as rfo:
        for row in rfo:
            cols = row.rstrip().split("\t")
            cols[-1] = int(cols[-1].replace("円", ""))
            lst.append(Food(*cols))
    return lst


if __name__ == "__main__":
    foods = read_foods(sys.argv[1])
    bought_foods = list()  # 購入したFoodインスタンスを格納するリスト
   

    # 購入商品をappendしていく
    for i, wantfood in enumerate(sys.argv):
        if i ==0 or i== 1:
            continue
        swich = 0
        for j, k  in enumerate(foods):
            if k.name ==wantfood:
                swich = 1
                break
        if swich:
            print(f"Food({foods[j]}) を買いました")
            bought_foods.append(foods[j])
        elif swich == False:
            print(wantfood,"は売ってません")
            


  
    print(f"合計金額：{sum(bought_foods)}")