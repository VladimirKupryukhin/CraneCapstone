import tkinter
from tkinter import *
import sys

import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from itertools import count


class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Crane Aerospace Capstone 2024-2025 Logger")    
        self.geometry("1000x500")
        
        recordButton = Button(self, text = str("Record"))
        recordButton.grid(row = 0, column = 0)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        smrt1 = SMRTWidget(self, "SMRT 1")
        smrt2 = SMRTWidget(self, "SMRT 2")
        smrt3 = SMRTWidget(self, "SMRT 3")
        
        smrt1.grid(row=1,column=0)
        smrt2.grid(row=1,column=1)
        smrt3.grid(row=1,column=2)
        
        plt.style.use('fivethirtyeight')
        # values for first graph
        x_vals = [1,2,3,4]
        y_vals = [1,2,4,8]
        
        index = count()
        
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self)
        canvas.get_tk_widget().grid(row=2, column=0)
        plt.gcf().subplots(1, 1)
        plt.cla()
        plt.plot(x_vals, y_vals)
        #plt.show(block=False)
        
        
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        #frame = Frame(self, bg='lightblue', width=200, height=200)
        # frame.grid(row = 2, column = 2)
        
        
        # test1 = Label(master=frame, text = "Voltage", font="bold")
        # test1.grid(row = 0, column = 0)
        
        # test2 = Label(frame, text = "ADC Value")
        # test2.grid(row = 1, column = 1)
        
        # Label(frame, text = "12345")#.grid(row = 2, column = 1)
        # Label(frame, text = "Voltage Value")#.grid(row = 3, column = 0)
        # Label(frame, text = "5.4")#.grid(row = 3, column = 1)
        
    def on_close(self):
        print("asdasdasdsa")
        plt.close('all')
        self.destroy()
        sys.exit(0)


class SMRTWidget(tkinter.Frame):
    def __init__(self, parent, smrtText):
        super().__init__(master = parent, bg='lightblue', padx=5, pady=5)
        
        smrtLabel = Label(self, text=smrtText, font='bold')
        
        tempLabel = Label(self, text='Temperature',justify=tkinter.LEFT)
        tempData = Label(self, text='0.00')
        
        aOutLabel = Label(self, text="3.3V Out (A OUT)",justify=tkinter.LEFT)
        aOutData = Label(self, text='0.00')
        
        bPosOutLabel = Label(self, text='+15V Out (B POS OUT)',justify=tkinter.LEFT)
        bPosOutData = Label(self, text='0.00')
        
        bNegOutLabel = Label(self, text='-15V Out (B NEG OUT)',justify=tkinter.LEFT)
        bNegOutData = Label(self, text='0.00')
        
        # Grids
        smrtLabel.grid(row=0,column=0)
        
        tempLabel.grid(row=1,column=0)
        tempData.grid(row=1,column=1)
        
        aOutLabel.grid(row=2,column=0)
        aOutData.grid(row=2,column=1)
        
        bPosOutLabel.grid(row=3,column=0)
        bPosOutData.grid(row=3,column=1)
        
        bNegOutLabel.grid(row=4,column=0)
        bNegOutData.grid(row=4,column=1)
        
        

