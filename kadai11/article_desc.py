import sys
from abc import ABC,abstractmethod


class Validator(ABC):
    def __set_name__(self,objtype,attrname):
        self.attrname = attrname
    def __get__(self,obj,objtype=None):
        return obj.__dict__[self.attrname]
    def __set__(self,obj,value):
        self.validate(value)
        obj.__dict__[self.attrname] = value
    
    
    @abstractmethod
    def validate(self):
        pass
class CategoryValidator(Validator):
    def __init__(self,lst):
        self.lst = lst
    def validate(self,value):
        if not value in self.lst:
            raise Exception("カテゴリが存在しません")
class LengthValidator(Validator):
    def __init__(self,maxchara):
        self.maxchara = maxchara
    def validate(self,chara):
        if  len(chara) > self.maxchara:
            omg = len(chara)
            raise Exception("文字数オーバーです",omg)
class DateValidator(Validator):
    def __init__(self,wantdate):
        self.wantdate = wantdate
    def validate(self,itsdate):
        if not self.wantdate == itsdate:
            raise Exception(f"{itsdate}は対象外の日付です")

class Article:
    cate_lst = ["国内", "海外", "経済", "エンタメ", "スポーツ", "IT", "科学", "地域"]  # 本当は「国際」だが「海外」としている
    cate = CategoryValidator(cate_lst)
    body = LengthValidator(int(sys.argv[2]))  # 200, 5000
    pub_date = DateValidator(sys.argv[3])  # 10月7日, 10月8日
    def __init__(self, url, title, body, cate, pub_date, pub_time):
        self.url = url
        self.title = title
        self.body = body
        self.cate = cate
        self.pub_date = pub_date
        self.pub_time = pub_time

    def __len__(self):
        return len(self.body)
    
    def __repr__(self):
        return f"{self.title}\t<{self.cate}>\t({self.pub_date} {self.pub_time})"
    

def read_articles(file_path):
    articles = list()
    with open(file_path, "r", encoding="utf-8") as rfo:
        for row in rfo:
            cols = row.rstrip().split("\t")
            try:
                art = Article(*cols)
                articles.append(art)
            except Exception as e:
                print(e)
    return articles


if __name__ == "__main__":
    articles = read_articles(sys.argv[1])  # data/yahoo_news.txt
    print("-"*30)
    print(f"投稿記事数：{len(articles)}")
    for a, art in enumerate(articles, 1):
        print(a, art, f"本文文字数：{len(art)}")
