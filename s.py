Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
>>> banana = "banana.gif"
>>> bodercolor = [('aliceblue', '#F0F8FF'), ('blue', '#0000FF'), ('beige', '#F5F5DC'), ('red', '#ff0000'), ('lightgreen', '#90EE90')]
>>> class BgChange:
    def __init__(self, label, color):
        self.label = label
        self.color = color

    def __call__(self, event=None):
        self.label.configure(bg=self.color)

        
>>> class MyWindow(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('select bordercolor')
        f_button = tk.Frame(self)
        f_button.pack(side=tk.LEFT, padx=5, pady=1)
        self.banana = tk.PhotoImage(file=banana)
        label = tk.Label(image=self.banana, relief=tk.RAISED, bd=6)
        label.pack(side=tk.RIGHT, padx=7)

        for name, code in bodercolor:
            b = tk.Button(f_button, text=name, bg=code, command=BgChange(label, code))
            b.pack(fill=tk.X)

            
>>> if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('750x600+10+10')
    myframe = MyWindow(root)
    myframe.pack()
    root.mainloop()

    
''
Traceback (most recent call last):
  File "<pyshell#8>", line 4, in <module>
    myframe = MyWindow(root)
  File "<pyshell#6>", line 7, in __init__
    self.banana = tk.PhotoImage(file=banana)
  File "C:\Users\Owner\AppData\Local\Programs\Python\Python37-32\lib\tkinter\__init__.py", line 3542, in __init__
    Image.__init__(self, 'photo', name, cnf, master, **kw)
  File "C:\Users\Owner\AppData\Local\Programs\Python\Python37-32\lib\tkinter\__init__.py", line 3498, in __init__
    self.tk.call(('image', 'create', imgtype, name,) + options)
_tkinter.TclError: couldn't open "banana.gif": no such file or directory
>>> 
