from dataclasses import dataclass
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@dataclass
class Teacher:
    name: str
    url: str
    position: str
    field: str


class TeacherScraper:
    def __init__(self, url):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        
        self.driver.get(url)
    
    def jump_gakubu(self, dep, gakubu):
        #0.引数のdep，gakubuがどんな値なのか，何のために受け取っているのか考える
        #1.「学部・大学院案内」を抽出しクリック（必要に応じてsleep)
        link = self.driver.find_element(By.LINK_TEXT, "学部･大学院案内")
        link.click()
        sleep(3)
        #2.学部名を抽出しクリック（必要に応じてsleep)
        link = self.driver.find_element(By.LINK_TEXT,f"{gakubu}トップ")
        link.click()
        sleep(3)
        #3.「教員紹介」を抽出しクリック（必要に応じてsleep）
        link = self.driver.find_element(By.LINK_TEXT,"教員紹介")
        link.click()
        sleep(3)
        self.dep = dep

    def get_title(self):
        return self.driver.title
        
    def get_profile(self):
        teachers = list()
        want = self.driver.find_elements(By.CLASS_NAME,f"{self.dep}dep_flex3col")
        # 1.クラス名「XXXdep_flex3col」を手がかりにulタグたちを検索
        for val in want:
            #val= val.find_elements(By.TAG_NAME("ul"))
            val = val.find_elements(By.TAG_NAME,"a")
            
            for val1 in val:
                
                href = val1.get_attribute("href")

                h2 = val1.find_element(By.TAG_NAME,"h2")

                h4 = val1.find_element(By.TAG_NAME,"h4")
                p = val1.find_element(By.TAG_NAME,"p")
                teachers.append(Teacher(h2.text,href,h4.text,p.text))
                
        #    2.aタグたちを検索
        #       3.href属性の取得
        #      4.教員氏名の取得
        #     5.教員職位の取得
            #    6.専門分野の取得
        return teachers


if __name__ == "__main__":
    url = "https://www.teu.ac.jp/"
    scr = TeacherScraper(url)
    for dep, gakubu in {"cs": "コンピュータサイエンス学部", "ds": "デザイン学部", "es": "工学部", "": "メディア学部"}.items():
        scr.jump_gakubu(dep, gakubu)
        print(scr.get_title())
        teachers = scr.get_profile()
        print(len(teachers))
        pprint(teachers[:5])
