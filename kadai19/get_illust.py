import json
from urllib.request import urlopen
import dl_image
from pprint import pprint

class IllustDownloader:
    def __init__(self, url):
        self.sorce = urlopen(url)
        self.jsn = json.load(self.sorce)
        

    def get_illust(self, num):
        entry = self.jsn[num]
        print(entry)
        u = entry["urls"][0]
        dl_image.download_file(u,f"kadai19/{num}_{0}.png")
        
if __name__ == "__main__":
    url = "https://fsm-lab.cs.teu.ac.jp/lecture/ProA2/2023/illust/animals.json"
    IllustDownloader(url).get_illust(119)  # 学籍番号の下３桁
    #IllustDownloader(url)