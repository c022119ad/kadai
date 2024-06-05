import json
from dataclasses import dataclass
from urllib.request import urlopen
from bs4 import BeautifulSoup
import dl_image

@dataclass
class Product:
    name: str  # 商品名
    href: str  # 商品のURL（mognaviドメイン）
    src: str  # 画像のURL（fsm-labドメイン）


class ProductScraper:
    def __init__(self, url):
        html = urlopen(url).read().decode()
        self.soup = BeautifulSoup(html, "html.parser")
        self.base = url
        
        
    def get_values(self):
        self.products = list()
        for ul in self.soup.find_all("ul"):
            count = 0
            for div in ul.find_all("div",class_="pic"):
                prodic = {}
                a = div.find("a")
                
                if a == None:
                    continue
                
                href = a.attrs["href"]
                img = a.img
                src = img.attrs["src"]
                alt = img.attrs["alt"]
                src = f"{self.base}{src}"
                prodic["name"] = alt
                prodic["href"] = href
                prodic["src"] = f"{self.base}"
                self.products.append(Product(alt,href,src))
                #huref = a.attrs["href"]
                
                #print(href)
                
        #for i ,v in enumerate(self.products):
        #   print(v["src"])
                dl_image.download_file(src,f"kadai20/{count}.png")
                count += 1
            
        
        return self.products
    
    def save_as_json(self, file_path):
        pass
        with open(file_path, "w", encoding="utf-8") as wfo:
            
            #key = ["name","href","src"]
            
            json_lst = []
            prodict = {}
            for v in self.products:
                prodict = {}
                prodict["name"] =v.name
                prodict["href"] = v.href
                prodict["src"] = v.src
                json_lst.append(prodict)
            #   prodict = {}
            #  for k in key:
            #     prodict[k]=v.k
                #json_lst.append[prodict]
            json.dump(json_lst,wfo,indent=2,ensure_ascii=False)
                    


if __name__ == "__main__":
    url = "https://fsm-lab.cs.teu.ac.jp/lecture/ProA2/2023/mognavi/"
    scr = ProductScraper(url)
    scr.get_values()
    
    scr.save_as_json("kadai20/product.json")