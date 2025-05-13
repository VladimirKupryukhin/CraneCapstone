import tkinter
from tkinter import *
import sys

import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from itertools import count
from matplotlib.pyplot import figure
from collections import deque
from usbThread import SMRTData
from collections import deque
from matplotlib.animation import FuncAnimation


class App(tkinter.Tk):
    def __init__(self, dataQueue):
        super().__init__()
        self.title("Crane Aerospace Capstone 2024-2025 Logger")    
        self.geometry("1000x500")
        
        self.recordButton = Button(self, text = str("Record"), command=self.button_clicked)
        self.recordButton.grid(row = 0, column = 0)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
        self.smrt1 = SMRTWidget(self, "SMRT 1")
        self.smrt2 = SMRTWidget(self, "SMRT 2")
        self.smrt3 = SMRTWidget(self, "SMRT 3")
        
        self.smrt1.grid(row=1,column=0)
        self.smrt2.grid(row=1,column=1)
        self.smrt3.grid(row=1,column=2)
        
        plt.style.use('fivethirtyeight')
        
        self.dataQueue:deque = dataQueue
        self.data:SMRTData
        
        self.graphXVals = []
        self.aFigureYVals = []
        self.bFigureYVals = []
        self.cFigureYVals = []
        
        self.aFigure = plt.figure(figsize=(20, 5), dpi=60)
        self.canvas = FigureCanvasTkAgg(self.aFigure, master=self)
        self.canvas.get_tk_widget().grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        self.a, self.b, self.c = self.aFigure.subplots(1,3)
        
        self.a.set_title("SMRT 1 Temperature")
        self.b.set_title("SMRT 2 Temperature")
        self.c.set_title("SMRT 3 Temperature")
        
        self.ani = FuncAnimation(plt.gcf(), self.animateGraphs, interval=200, blit=False)
        
        
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.after(ms=10, func=self.updateGuiData)
        

    def button_clicked(self):
        print("Yessir button clicked")
        
    def animateGraphs(self, i):        
        self.aFigureYVals.append(self.data.smrt1Temp)
        self.bFigureYVals.append(self.data.smrt2Temp)
        self.cFigureYVals.append(self.data.smrt3Temp)
        self.graphXVals.append(i)        
        
        
        if len(self.aFigureYVals) == 121:
            self.aFigureYVals.pop(0)
            self.bFigureYVals.pop(0)
            self.cFigureYVals.pop(0)
            self.graphXVals.pop(0)
        
        self.a.cla()
        self.a.set_title("SMRT 1 Temperature")
        self.a.plot(self.graphXVals, self.aFigureYVals)
        
        self.b.cla()
        self.b.set_title("SMRT 2 Temperature")
        self.b.plot(self.graphXVals, self.bFigureYVals)
        
        self.c.cla()
        self.c.set_title("SMRT 3 Temperature")
        self.c.plot(self.graphXVals, self.cFigureYVals)
        
        
    def updateGuiData(self):
        try:
            #print("Before")
            
            if self.dataQueue:    
                self.data:SMRTData = self.dataQueue.popleft()
                
                self.smrt1.tempData["text"] = str(self.data.smrt1Temp)[:6]
                self.smrt1.aOutData["text"] = str(self.data.smrt1A)[:6]
                self.smrt1.bPosOutData["text"] = str(self.data.smrt1BPOS)[:6]
                self.smrt1.bNegOutData["text"] = str(self.data.smrt1BNEG)[:6]
                
                self.smrt2.tempData["text"] = str(self.data.smrt2Temp)[:6]
                self.smrt2.aOutData["text"] = str(self.data.smrt2A)[:6]
                self.smrt2.bPosOutData["text"] = str(self.data.smrt2BPOS)[:6]
                self.smrt2.bNegOutData["text"] = str(self.data.smrt2BNEG)[:6]
                
                self.smrt3.tempData["text"] = str(self.data.smrt3Temp)[:6]
                self.smrt3.aOutData["text"] = str(self.data.smrt3A)[:6]
                self.smrt3.bPosOutData["text"] = str(self.data.smrt3BPOS)[:6]
                self.smrt3.bNegOutData["text"] = str(self.data.smrt3BNEG)[:6]
    

            
            self.after(ms=10, func=self.updateGuiData)
        except IndexError:
            pass    
        
        
    def on_close(self):
        plt.close('all')
        self.destroy()
        sys.exit(0)


class SMRTWidget(tkinter.Frame):
    def __init__(self, parent, smrtText):
        super().__init__(master = parent, padx=5, pady=5)
        
        self.smrtLabel = Label(self, text=smrtText, font='bold')
        
        self.tempLabel = Label(self, text='Temperature',justify=tkinter.LEFT)
        self.tempData = Label(self, text='0.00')
        
        self.aOutLabel = Label(self, text="3.3V Out (A OUT)",justify=tkinter.LEFT)
        self.aOutData = Label(self, text='0.00')
        
        self.bPosOutLabel = Label(self, text='+15V Out (B POS OUT)',justify=tkinter.LEFT)
        self.bPosOutData = Label(self, text='0.00')
        
        self.bNegOutLabel = Label(self, text='-15V Out (B NEG OUT)',justify=tkinter.LEFT)
        self.bNegOutData = Label(self, text='0.00')
        
        # Grids
        self.smrtLabel.grid(row=0,column=0)
        
        self.tempLabel.grid(row=1,column=0)
        self.tempData.grid(row=1,column=1)
        
        self.aOutLabel.grid(row=2,column=0)
        self.aOutData.grid(row=2,column=1)
        
        self.bPosOutLabel.grid(row=3,column=0)
        self.bPosOutData.grid(row=3,column=1)
        
        self.bNegOutLabel.grid(row=4,column=0)
        self.bNegOutData.grid(row=4,column=1)
        
        

