from dataclasses import dataclass
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sqlite3


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
        self.dep = dep
        link = self.driver.find_element(By.LINK_TEXT, "学部･大学院案内")
        link.click()
        sleep(1)
        link = self.driver.find_element(By.LINK_TEXT, gakubu)
        link.click()
        sleep(1)
        link = self.driver.find_element(By.LINK_TEXT, "教員紹介")
        link.click()
        sleep(1) 

    def get_title(self):
        return self.driver.title
        
    def get_profile(self):
        teachers = list()
        for ul in self.driver.find_elements(By.CLASS_NAME, f"{self.dep}dep_flex3col"):
            for a in ul.find_elements(By.TAG_NAME, "a"):
                href = a.get_attribute("href")
                name = a.find_element(By.TAG_NAME, "h2").text.replace("\u3000", " ")
                posi = a.find_element(By.TAG_NAME, "h4").text.replace("\u3000", " ")
                feld = a.find_element(By.TAG_NAME, "p").text.replace("\u3000", " ")
                teachers.append(Teacher(name, href, posi, feld))
        return teachers


class TeacherDB:
    def __init__(self, db_path):
        self.db_path = db_path

    def create_table(self, table, columns):
        self.con = sqlite3.connect(self.db_path)
        self.cur = self.con.cursor()
        lstcolumns = list(columns)
        try:
            self.cur.execute(f"CREATE TABLE {table} ({lstcolumns[0]},{lstcolumns[1]},{lstcolumns[2]},{lstcolumns[3]})")
        except sqlite3.OperationalError:
            self.cur.execute(f"DROP TABLE {table}")
            self.cur.execute(f"CREATE TABLE {table} ({lstcolumns[0]},{lstcolumns[1]},{lstcolumns[2]},{lstcolumns[3]})")
        
    def insert_data(self, table, data):
        print(type(data))
        lst = []
        for  val in data:
            tpl =(val.name,val.url,val.position,val.field)
            lst.append(tpl)
            #self.cur.execute(f"INSERT INTO {table} VALUES({val.name},{val.url},{val.position},{val.field})")
        self.cur.executemany(f"INSERT INTO {table} VALUES (?,?,?,?)",lst)
        self.con.commit()

    def __del__(self):
        self.con.close()


if __name__ == "__main__":
    url = "https://www.teu.ac.jp/"
    db_path = "kadai27/teachers.db"
    scr = TeacherScraper(url)
    db = TeacherDB(db_path)
    for dep, gakubu in {"cs": "コンピュータサイエンス学部", "ds": "デザイン学部", "es": "工学部"}.items():
        scr.jump_gakubu(dep, gakubu)
        print(scr.get_title())
        teachers = scr.get_profile()
        db.create_table(dep, teachers[0].__dict__.keys())
        db.insert_data(dep, teachers)
        
    db.__del__()