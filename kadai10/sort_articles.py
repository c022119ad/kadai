from dataclasses import dataclass
import sys

@dataclass
class Article:
    url: str
    title: str  # タイトル
    body: str  # 本文
    cate: str  # カテゴリ
    pub_date: str  # 配信日
    pub_time: str  # 配信時刻
    
    def get_datetime(self):
        hour, minute = self.pub_time.split(":")
        return int(hour)*60*60 + int(minute)*60
    def __len__(self):
        return len(self.body)
    def __repr__(self):
        return f"{self.title}\t({self.pub_date} {self.pub_time})"
    def __lt__(self,other):
        return  self.get_datetime() < other.get_datetime()
    def __gt__(self,other):
        return self.get_datetime()> other.get_datetime()
    def __eq__(self,other):
        return self.title == other.title
    def __hash__(self):
        return hash(self.title)


def read_articles(file_path):
    articles = list()
    with open(file_path, "r", encoding="utf-8") as rfo:
        for row in rfo:
            cols = row.rstrip().split("\t")
            art = Article(*cols)
            articles.append(art)
    return articles


if __name__ == "__main__":
    articles = read_articles(sys.argv[1])  # data/yahoo_news.txt
    print(f"投稿記事数：{len(articles)}")
    print(f"記事数：{len(set(articles))}")
    articles.sort()
    for a, art in enumerate(articles, 1):
        print(a, art, f"本文文字数：{len(art)}")
        if a == 10:
            break