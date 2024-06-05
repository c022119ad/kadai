import tkinter as tk


class IllustMap:
    def __init__(self, category):
        self.category = category
        self.root = tk.Tk()
        self.root.title(タイトルの設定)
        self.root.resizable(False, False)
        self.path2coord = データの読み込み

    @staticmethod
    def read_data(file_path):
        path2coord = dict()
        with open(file_path, "r", encoding="utf-8") as rfo:
            for row in rfo:
                path_name, coord = row.rstrip().split("\t")
                x, y = coord.split()
                path, name = path_name.split()
                path2coord[path] = (float(x), float(y))
        return path2coord
    
    def show(self):
        pass


if __name__ == "__main__":
    IllustMap("flags").show()