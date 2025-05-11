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


class App(tkinter.Tk):
    def __init__(self, dataQueue):
        super().__init__()
        self.title("Crane Aerospace Capstone 2024-2025 Logger")    
        self.geometry("1000x500")
        
        self.recordButton = Button(self, text = str("Record"))
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
        # values for first graph
        x_vals = [1,2,3,4]
        y_vals = [1,2,4,8]
        
        index = count()
        
        self.dataQueue:deque = dataQueue
        
        
        self.aFigureXVals = []
        self.aFigureYVals = []
        self.aFigure = plt.figure(figsize=(5, 5), dpi=80)
        self.canvas = FigureCanvasTkAgg(self.aFigure, master=self)
        self.canvas.get_tk_widget().grid(row=2, column=0)
        self.a = plt.gcf().subplots(1)
        
        # self.a.cla()
        #self.a.plot(self.aFigureXVals, self.aFigureYVals)
        self.aFigure.suptitle("SMRT1 Temperature")
        
        # bFigure = plt.figure(figsize=(5, 5), dpi=80)
        # canvas2 = FigureCanvasTkAgg(bFigure, master=self)
        # canvas2.get_tk_widget().grid(row=2, column=1)
        # b = plt.gcf().subplots(1)
        
        # b.cla()
        # b.plot(y_vals, x_vals)
        # bFigure.suptitle("SMRT2 Temperature")
        
        # cFigure = plt.figure(figsize=(5, 5), dpi=80)
        # canvas2 = FigureCanvasTkAgg(cFigure, master=self)
        # canvas2.get_tk_widget().grid(row=2, column=2)
        # c = plt.gcf().subplots(1)
        
        # c.cla()
        # c.plot(y_vals, x_vals)
        # cFigure.suptitle("SMRT3 Temperature")
        

        
        
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.after(ms=10, func=self.updateGuiData)
        
        #frame = Frame(self, bg='lightblue', width=200, height=200)
        # frame.grid(row = 2, column = 2)
        
        
        # test1 = Label(master=frame, text = "Voltage", font="bold")
        # test1.grid(row = 0, column = 0)
        
        # test2 = Label(frame, text = "ADC Value")
        # test2.grid(row = 1, column = 1)
        
        # Label(frame, text = "12345")#.grid(row = 2, column = 1)
        # Label(frame, text = "Voltage Value")#.grid(row = 3, column = 0)
        # Label(frame, text = "5.4")#.grid(row = 3, column = 1)
        
    def updateGuiData(self):
        try:
            #print("Before")
            
            if self.dataQueue:    
                data:SMRTData = self.dataQueue.popleft()
                
                self.smrt1.tempData["text"] = str(data.smrt1Temp)[:6]
                self.smrt1.aOutData["text"] = str(data.smrt1A)[:6]
                self.smrt1.bPosOutData["text"] = str(data.smrt1BPOS)[:6]
                self.smrt1.bNegOutData["text"] = str(data.smrt1BNEG)[:6]
                
                self.smrt2.tempData["text"] = str(data.smrt2Temp)[:6]
                self.smrt2.aOutData["text"] = str(data.smrt2A)[:6]
                self.smrt2.bPosOutData["text"] = str(data.smrt2BPOS)[:6]
                self.smrt2.bNegOutData["text"] = str(data.smrt2BNEG)[:6]
                
                self.smrt3.tempData["text"] = str(data.smrt3Temp)[:6]
                self.smrt3.aOutData["text"] = str(data.smrt3A)[:6]
                self.smrt3.bPosOutData["text"] = str(data.smrt3BPOS)[:6]
                self.smrt3.bNegOutData["text"] = str(data.smrt3BNEG)[:6]
                
                self.aFigureYVals.append(data.smrt1Temp)
                self.aFigureXVals.append(self.aFigureXVals.count + 1)
                
                self.a.cla()
                self.a.plot(self.aFigureXVals, self.aFigureYVals)

            
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
        
        

