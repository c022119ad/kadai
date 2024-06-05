import tkinter as tk
import glob

class IllustMap:
    def __init__(self, category):
        self.category = category
        self.root = tk.Tk()
        self.root.title("kadai16")
        self.root.resizable(False, False)
        self.filenamelst = []
        self.path2coord = self.read_data("data/flags_tsne.txt")
            
        

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
        xmin_ = min(self.path2coord.items(),key=lambda x:x[1][0])[1][0]
        xmax_ = max(self.path2coord.items(),key=lambda x:x[1][0])[1][0]
        ymin_ = min(self.path2coord.items(),key=lambda x:x[1][1])[1][1]
        ymax_ = max(self.path2coord.items(),key=lambda x:x[1][1])[1][1]
        raito = 20
        vallst = []
        for l in self.path2coord.values():        
            vallst.append((float(l[0]),float(l[1])))
        #print(xmin_,xmax_,ymin_,ymax_)
        canvas =tk.Canvas(self.root, width=(xmax_-xmin_)*raito, height=(ymax_-ymin_)*raito)
        canvas.pack()
        flags = [tk.PhotoImage(file=f"data/flags/{flag}") for flag in self.path2coord]
        #print(vallst)
        c=0
        for f in flags:
            canvas.create_image((vallst[c][0]-xmin_)*raito,(vallst[c][1]-ymin_)*raito,image=f)
            c+=1
            
        self.root.mainloop()

if __name__ == "__main__":
    IllustMap("flags").show()