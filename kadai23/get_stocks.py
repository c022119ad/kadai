from dataclasses import dataclass
from pprint import pprint
import re
from urllib.request import urlopen


@dataclass
class StockValue:
    date: str
    hajimene: float
    takane: float
    yasune: float
    owarine: float
    dekidaka: float
    choseigo: float


class StockScraper:
    def __init__(self, url):
        self.html = urlopen(url).read().decode().replace("\n", "")

    def get_title(self):
        #1.titleタグのパターン
        pattern = '<title>(.*?)</title>'
        memo = re.findall(pattern,self.html)
        return memo[0]
        #return self.html[memo1[1]:memo[0]]
    
    def get_values(self):
        values = list()
        
        #1.table，tbodyタグのパターン
        tabpattern = '<table.*?>(.*?)</table>'
        tbodypattern = '<tbody.*?>(.*?)</tbody>'
        search = re.findall(tabpattern,self.html)
        search= re.findall(tbodypattern,search[0])
        #print(search)
        #2.パターンの検索
        trpattern = '<tr.*?>(.*?)</tr>'
        thpattern = '<th.*?>(.*?)</th>'
        tdpattern = '<td.*?>(.*?)</td>'
        delpattern = re.compile('<.*?>')
        search= re.findall(trpattern,search[0])
        for val in search:
            memolst =[]
            thval = re.findall(thpattern,val)
            
            tdval = re.findall(tdpattern,val)
            for val1 in tdval:
                val1 = (delpattern.sub("",val1))
                memolst.append(float(val1.replace(",","")))
            values.append(StockValue(thval[0],memolst[0],memolst[1],memolst[2],memolst[3],memolst[4],memolst[5]))
        
            
            
        
        #4.thタグのパターン
        #5.tdタグのパターン
        #6.タグのパターン        
        #7.trタグたちの検索
        #   8.thタグの検索
        #  9.tdタグたちの検索
        #     10.不要タグを削除し，株価の値を抽出
        return values
        


if __name__ == "__main__":
    url = "https://fsm-lab.cs.teu.ac.jp/lecture/ProA2/2023/stocks/"
    scr = StockScraper(url)
    print(scr.get_title())
    pprint(scr.get_values())
