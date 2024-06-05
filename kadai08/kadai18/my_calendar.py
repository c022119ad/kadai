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
        pass

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