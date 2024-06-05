from pprint import pprint
import sqlite3


COLUMNS = ["name", "category", "maker", "brand", "date", "price"]


def read_foods(file_path):
    lst = list()
    with open(file_path, "r", encoding="utf-8") as rfo:
        for row in rfo:
            cols = row.rstrip().split("\t")
            cols[-1] = int(cols[-1].replace("円", ""))
            lst.append([v for v in cols])
    return lst


if __name__ == "__main__":
    db_path = "kadai25/foods.db"
    table = "convenience_store"
    # データベースへの接続
    con = sqlite3.connect(db_path)
    # カーソルオブジェクトの生成
    cur = con.cursor()
    create_order  =  f"CREATE TABLE {table} ({COLUMNS[0]},{COLUMNS[1]},{COLUMNS[2]},{COLUMNS[3]},{COLUMNS[4]},{COLUMNS[5]})"
    # 例外処理（すでにテーブルが存在していたら，テーブルを削除する)
    try:
        cur.execute(create_order)
    except sqlite3.OperationalError  :
        cur.execute(f"DROP TABLE {table}")
        cur.execute(create_order)
    
    
    # どのような例外が発生するか確認し，適切な例外をキャッチすること
    # テーブルの作成（定数COLUMNSを使用すること）
    # テーブルの削除

    foods = read_foods("data/conv_foods.txt")
    # pprint(foods[:10])  # 最初の10件を確認表示
    sql = f"INSERT INTO {table} VALUES (?,?,?,?,?,?)"  # バルクインサート
    print(sql)  # SQL文の確認表示
    # SQLの実行
    cur.executemany(sql,foods)
    con.commit()
    cur.execute(f"SELECT name,price FROM {table} ORDER BY price DESC ")
    for row in cur.fetchmany(10):
        print(row)
    con.close()

    # データの検索（priceの降順に10件，nameとpriceを検索する）

    # データベースへの接続を切断