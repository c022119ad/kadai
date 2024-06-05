import sqlite3
import sys

class SqlExecuter:
    def __init__(self,dbpath,tbname,col):
        self.dbpath = dbpath
        self.tbname = tbname
        self.col = col

    def __enter__(self):
        self.con = sqlite3.connect(self.dbpath)
        self.cur =self.con.cursor()
        create_order = f"CREATE TABLE {self.tbname} ({self.col[0]},{self.col[1]},{self.col[2]},{self.col[3]})"
        try:
            self.cur.execute(create_order)
            print("テーブルを構築しました")
        except sqlite3.OperationalError:
            self.cur.execute(f"DROP TABLE {self.tbname}")
            self.cur.execute(create_order)
            print(f"{self.tbname}は既に存在していたので一度削除してから構築しました")
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        if exc_value is None:
            print(f"正常にSQLが実行されました")
            print("切断しました")
        else:
            print(f"正常にSQLが実行されませんでした",exc_type, exc_value)
            print(f"切断しました")
        

    def insert(self,names):
        print("レコード挿入")
        self.cur.executemany(f"INSERT INTO {self.tbname} VALUES (?,?,?,?)",names)
        self.con.commit()


    def select(self,col_name,condition,order):
        self.cur.execute(f"SELECT {col_name[0]} FROM {self.tbname} WHERE {condition} ORDER BY {order}")
        lst = []
        
        for row in self.cur:
            lst.append(tuple(row))
        return lst
def read_names(file_path):
    names = []
    with open(encoding="utf8", file=file_path, mode="r") as rfo:
        for row in rfo:
            id_, tit, typ, *evo_lst = row.rstrip().split("\t")
            evo = " ".join(evo_lst)
            names.append((int(id_), tit, typ, evo))
    return names


if __name__ == "__main__":
    names = read_names("data/poke_names2.txt")
    db_path = "kadai29/pokemon.db"
    tbl_name = "names"
    col_lst = ["id", "name", "types", "evolvs"]
    col_name = sys.argv[1]  # name, hoge
    with SqlExecuter(db_path, tbl_name, col_lst) as se:
        se.insert(names)
        rows = se.select([col_name], condition="id > 245", order="id DESC")
        for row in rows:
            print(row)

