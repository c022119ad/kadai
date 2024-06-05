import tkinter as tk
import tkinter.messagebox as tkm


class Calculator:
    operands  = ["."]+[str(num) for num in range(0, 10)]
    operators = {"＋":"+", "－":"-", "×":"*", "÷":"/"}
    functions = {"1/x":((1,0) ,lambda x:1.0/x),"x^2":((1,1), lambda x:x*x),"√x":((1,2),lambda x: x**(1/2)),"=":((5,3),lambda x:x),"+/-":((5,0),lambda x : x*-1)}

    def __init__(self, title):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.resizable(False, False)        
        self.exp = ""

    def show(self):
        r, c = 2, 2
        for n, num in enumerate(reversed(__class__.operands), 1):
            btn = tk.Button(self.root, text=num, width=4, height=2, font=("", 30))
            if num == "0":
                btn.grid(row=r, column=1)
            elif num == ".":
                btn.grid(row=r, column=2)
            else:
                btn.grid(row=r, column=c)
            btn.bind("<1>", self.click_button)
            c -= 1
            if n%3 == 0:
                r += 1
                c = 2

        for o, ope in enumerate(reversed(__class__.operators.keys()), 1):
            btn = tk.Button(self.root, text=ope, width=4, height=2, font=("", 30))
            btn.grid(row=o, column=3)
            btn.bind("<1>", self.click_button)
        
        for f, fnc in enumerate(__class__.functions.keys()):
            btn = tk.Button(self.root,text=fnc,width=4,height=2,font=("",30))
            print(f,fnc,__class__.functions[fnc][0][0],__class__.functions[fnc][0][1])
            btn.grid(row=__class__.functions[fnc][0][0],column=__class__.functions[fnc][0][1])
            btn.bind("<1>",self.click_func)
            

        self.entry = tk.Entry(self.root, font=("", 30), width=10, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, sticky=tk.EW)
        self.root.mainloop()

    def click_button(self, event:tk.Event):
        btn = event.widget
        key = btn["text"]
        self.entry.insert(tk.END, key)
        if key in __class__.operators:
            self.exp += __class__.operators[key]
        else:
            self.exp += key
        print(self.exp)

    def click_func(self, event:tk.Event):
        btn = event.widget
        key = btn["text"]
        calc = (__class__.functions[key][1](eval(self.exp)))
        if int(calc)==calc:
            calc = int(calc)
        self.entry.delete(0,tk.END)
        self.entry.insert(tk.END,calc)
        self.exp =str(calc)
        #print(self.functions[key][1])
        print(self.exp)

if __name__ == "__main__":
    Calculator("超高機能電卓").show()
