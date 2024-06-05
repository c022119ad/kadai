import calendar as cal
from collections import defaultdict
import tkinter as tk
import tkinter.messagebox as tkm


class Calendar:
    def __init__(self, year, month):
        self.day_lst = cal.monthcalendar(year, month)
        # print(self.day_lst)
        self.root = tk.Tk()
        self.root.title(f"{year}年{month}月のカレンダー")
        self.root.resizable(False, False)
        self.schedule = __class__.read_schedule(f"data/schedule_{year}{month}.txt")
        
    @staticmethod
    def read_schedule(file_path):
        schedule = defaultdict(int)
        with open(file_path, "r", encoding="utf-8") as rfo:
            for row in rfo:
                date, num = row.rstrip().split("\t")
                schedule[int(date)] = int(num)
        return schedule
 
    def show(self):
        width_ = 100
        height_ = 80
        weeks = len(self.day_lst)
        self.root.geometry(f"{width_*7}x{weeks*height_}")
        self.canvas = tk.Canvas(self.root,width=width_*7,height=height_*weeks)
        self.canvas.pack()
        
        for w in range(weeks):
            for d in range(7):
                self.canvas.create_rectangle(d*width_,w*height_,d*width_+width_,w*height_+height_,fill="white",outline="grey",tag =f"cell{self.day_lst[w][d]}")
    
                if self.day_lst[w][d] == 0:#昨月か来月であれば以降の処理は行わない
                    continue
                self.canvas.tag_bind(f"cell{self.day_lst[w][d]}","<ButtonPress-1>",self.click_day)
                
                if d == 6:#土曜日であれば文字を青色に
                    color = "blue"
                elif d == 0:#日曜日であれば文字を赤色に
                    color = "red"
                else:#平日は黒
                    color = "black"
                self.canvas.create_text(d*width_+(width_/2),w*height_+(height_/2),text=self.day_lst[w][d],font=("",20),fill=color)
        
        
        
        self.root.mainloop()


    def click_day(self, event:tk.Event):
        # クリックされた座標の取得
        x = event.x
        y = event.y
        # クリックされた座標に一番近い図形（日にち）のID取得
        cell = self.canvas.find_closest(x, y)
        day = self.canvas.itemcget(cell, "tag").replace("cell", "").replace(" current", "")
        tkm.showinfo("予定", f"{day}日の予定は{self.schedule[int(day)]}件です")


if __name__ == "__main__":
    cal.setfirstweekday(cal.SUNDAY)  # 日曜始まりのカレンダー
    Calendar(2023, 11).show()
    test = Calendar(2023,11)
    #print(test.day_lst.show())
