# 5/12/2016 jgunter
from tkinter import *
from tkinter import ttk

class TestApp:

    def __init__(self, master):
        #frame = ttk.Frame(master)
        #frame.pack()
        #frame.config(height = 100, width = 200)

        #self.button = ttk.Button(frame, text = 'Click Me').grid()
        #frame.config(padding = (30,15))

        #ttk.LabelFrame(master, height = 100, width = 200, text = 'My Frame').pack()
        panedwindow = ttk.Panedwindow(master, orient = HORIZONTAL)
        panedwindow.pack(fill = BOTH, expand = True)
        frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)
        frame2 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)
        frame3 = ttk.Frame(panedwindow, width = 50, height = 400, relief = SUNKEN)
        panedwindow.add(frame1, weight = 1)
        panedwindow.add(frame2, weight = 4)
        panedwindow.insert(1, frame3)
        panedwindow.forget(1)

def main():
    root = Tk()
    #window = Toplevel(root)
    #window.title('New Window')
    #window.lift(root)
    ## window.state() parameters 'normal', 'zoomed', 'withdrawn', 'iconic'
    ## window.iconify(), window.deiconify()
    #window.maxsize(500, 400)
    #window.minsize(200, 150)
    # window.destroy()

    app = TestApp(root)
    root.mainloop()

if __name__ == "__main__": main()
