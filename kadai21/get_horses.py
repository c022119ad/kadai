import json
from dataclasses import dataclass
from urllib.request import urlopen
from bs4 import BeautifulSoup


@dataclass
class RaceRecord:
    rank: int  # 0
    waku: int  # 1
    num: int  # 2
    name: str  # 3
    age: str  # 4
    weight: float  # 5
    jockey: str  # 6
    time: str  # 7
    diff: str  # 8
    pop: int  # 9
    odds: float  # 10


class RaceScraper:
    def __init__(self, url):
        html = urlopen(url).read().decode()
        self.soup = BeautifulSoup(html, "html.parser")
    
    def get_values(self):
        self.records = list()
        for ul in self.soup.find_all("table",class_ ="RaceTable01 RaceCommon_Table ResultRefund Table_Show_All"):
            
            for tr in ul.find_all("tr"):
                td1 = tr.td
                if td1==None:
                    continue
                v1=td1.div.string
                
                td2 = td1.find_next_sibling("td")
                v2=td2.div.string
                td3 = td2.find_next_sibling("td")
                v3=td3.div.string
                td4 =td3.find_next_sibling("td")
                v4=td4.span.a.string
                td5=td4.find_next_sibling("td")
                v5=td5.div.span.string
                v5 = v5.replace("\n","")
                td6=td5.find_next_sibling("td")
                v6=td6.div.span.string
                td7=td6.find_next_sibling("td")
                v7=td7.a.string
                v7 = v7.replace(" ","")
                td8 = td7.find_next_sibling("td")
                v8=td8.span.string
                td9 = td8.find_next_sibling("td")
                v9=td9.span.string
                if v9 == None:
                    v9=""
                td10 = td9.find_next_sibling("td")
                v10=td10.span.string
                td11 = td10.find_next_sibling("td")
                v11=td11.span.string
                self.records.append(RaceRecord(int(v1),int(v2),int(v3),v4,v5,float(v6),v7,v8,v9,int(v10),float(v11)))
            
            #for div in ul.find_all("span"):
             #   print(div)
                #print("あ")

        return self.records

    def save_as_json(self, file_path):
        with open(file_path, "w", encoding="utf-8") as wfo:
            jsonlst = []
            horsedict ={}
            for val in self.records:
                horsedict={}
                horsedict["rank"]=val.rank
                horsedict["waku"]=val.waku
                horsedict["num"]=val.num
                horsedict["name"]=val.name
                horsedict["age"]=val.age
                horsedict["weight"]=val.weight
                horsedict["jockey"]=val.jockey
                horsedict["time"]=val.time
                horsedict["diff"]=val.diff
                horsedict["pop"]=val.pop
                horsedict["odds"]=val.odds
                jsonlst.append(horsedict)
            json.dump(jsonlst,wfo,indent=2,ensure_ascii=False)


if __name__ == "__main__":
    url = "https://fsm-lab.cs.teu.ac.jp/lecture/ProA2/2023/netkeiba/"
    scr = RaceScraper(url)
    scr.get_values()
    scr.save_as_json("kadai21/race.json")
