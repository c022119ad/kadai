import sys
from dataclasses import dataclass
import collections

@dataclass
class Food:
    def __init__(self,name,katego,maker,bra,day,price):
        self.name = name
        self.price = price
    def __repr__(self) :
        return f"Food(name={self.name},price={self.price})"
    def __add__(self,other):
        return (self.price+other.price)
    def __radd__(self,other):
        return (int(self.price)+int(other))


class Cart(collections.UserList):
    def __init__(self,maxprice,data=None):
        self.maxprice = maxprice
        if not hasattr(data, '__iter__'):
            super().__init__(data)
        else:
            #if sum([i.price for i in data ]) > maxprice:
            if sum(data) >maxprice:
                total = sum(data)
                raise PriceBoundError("金額上限オーバーです",total)
            else:
                super().__init__(data)
    def append(self, more):
        if sum(self.data) + more.price > self.maxprice:
            total=sum(self.data)+more.price
            raise PriceBoundError("金額上限オーバーです",total)
        else:
            super().append(more)
class PriceBoundError(Exception):
        pass
    
    
        
        


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
    wantfoodslst = []
    for i, wantfood in enumerate(sys.argv):
        if i ==0 or i== 1:
            continue
        for j, k  in enumerate(foods):
            if k.name ==wantfood:
                wantfoodslst.append(k)
                break
    
    cart = Cart(1000, wantfoodslst)
    cart.append(Food("袋", "", "", "", "", 5))
    print(cart, f"合計金額：{sum(cart)}")