from pprint import pprint
import sqlite3

COLUMNS = ["name", "lines", "latitude", "longitude"]

def read_stations(file_path):
    lst = list()
    with open(file_path, "r", encoding="utf-8") as rfo:
        for i, row in enumerate(rfo):
            id_, name, lines, latlng = row.rstrip().split("\t")
            lat, lng = latlng.split(",")
            lst.append([name, lines, float(lat), float(lng)])
    return lst


class SouthernMost:
    def __init__(self):
        self.argmin = None
        self.min1 = 100
    
    def step(self,argmin,min1):
        if self.min1 > min1:
            self.argmin = argmin
            self.min1 = min1
    
    def finalize(self):
        return self.argmin
    

if __name__ == "__main__":
    db_path = "kadai26/stations.db"
    table = "nodes"
    
    # データベースへの接続
    con = sqlite3.connect(db_path)
    
    # カーソルオブジェクトの生成
    con.create_aggregate("cal",2,SouthernMost)
    cur = con.cursor()
    create_order = f"CREATE TABLE {table} ({COLUMNS[0]},{COLUMNS[1]},{COLUMNS[2]},{COLUMNS[3]}) "
    # 例外処理（すでにテーブルが存在していたら，テーブルを削除する）
    try:
        cur.execute(create_order)
    except sqlite3.OperationalError:
        cur.execute(f"DROP TABLE {table}")
        cur.execute(create_order)
        
        
    # どのような例外が発生するか確認し，適切な例外をキャッチすること
    # テーブルの作成（定数COLUMNSを使用すること）
    # テーブルの削除

    stations = read_stations("data/station_nodes.txt")
    # pprint(stations[:10])  # 最初の10件を確認表示
    sql = f"INSERT INTO {table} VALUES (?,?,?,?)"  # バルクインサート
    cur.executemany(sql,stations)
    con.commit()
    print(sql)  # SQL文の確認表示
    # SQLの実行

    # SouthernMostクラスを用いて，緯度最小の駅を探す
    cur.execute(f"SELECT cal(name,latitude) FROM {table}")
    for row in cur:
        print(row)
    # データベースへの接続を切断
    con.close()
