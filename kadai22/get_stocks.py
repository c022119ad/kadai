from dataclasses import dataclass
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By


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
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        
        self.driver.get(url)

    def get_title(self):
        return self.driver.title
    
    def get_values(self):
        values = list()
        tablev = self.driver.find_element(By.TAG_NAME,"table")
        tbodyv = self.driver.find_element(By.TAG_NAME,"tbody")
        trv = self.driver.find_elements(By.TAG_NAME,"tr")
        memolst = []
        c = 0
        for val in trv:
            memolst=[]
            
            thv = val.find_element(By.TAG_NAME,"th")
            
    
            textv = thv.text
            tdv = val.find_elements(By.TAG_NAME,"td")
            for val2 in tdv:
                valtex = val2.text.replace(",","")
                memolst.append(float(valtex))
            if len(memolst) ==0:
                c+=1
                if c== 1:
                    continue
            if c==2:
                break
            values.append(StockValue(textv,memolst[0],memolst[1],memolst[2],memolst[3],memolst[4],memolst[5]))
        return values


if __name__ == "__main__":
    url = "https://fsm-lab.cs.teu.ac.jp/lecture/ProA2/2023/stocks/"
    scr = StockScraper(url)
    print(scr.get_title())
    pprint(scr.get_values())
