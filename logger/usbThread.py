import serial
import time
from serial.tools import list_ports
from dataclasses import dataclass
import math
import csv

VID = 11914
PID = 10

PICO_COMMS_VOLTAGE_DROP = 0.055

def usbThreadEntry(dataQueue):
    
    print("Starting USB Thread")
    
    try:
        conn = serial.Serial(str(getCOMPort()), 115200)
    except:
        print("FAILED TO CONNECT TO ADAPTER")
        exit(0)
        
    print(conn.name)
    
    picoInterface = PicoData(conn)
    

    
    writeCounter = 0
    
    while True:
        picoInterface.readData()
        picoInterface.convertData()
        #picoInterface.printData()
    
        sendDataToGui(picoInterface, dataQueue)
        
        # if writeCounter % 10 == 0:
        #     picoInterface.writecsvRows()
        #     writeCounter = 0
        # writeCounter += 1
        time.sleep(0.1)
        
def sendDataToGui(picoInterface, dataQueue):
    data = SMRTData(
        picoInterface.smrt1Temp,
        picoInterface.smrt1A,
        picoInterface.smrt1BPOS,
        picoInterface.smrt1BNEG,
        picoInterface.smrt2Temp,
        picoInterface.smrt2A,
        picoInterface.smrt2BPOS,
        picoInterface.smrt2BNEG,
        picoInterface.smrt3Temp,
        picoInterface.smrt3A,
        picoInterface.smrt3BPOS,
        picoInterface.smrt3BNEG)
    
    dataQueue.append(data)


@dataclass
class SMRTData:
    smrt1Temp: float
    smrt1A: float
    smrt1BPOS: float
    smrt1BNEG: float
    
    smrt2Temp: float
    smrt2A: float
    smrt2BPOS: float
    smrt2BNEG: float
    
    smrt3Temp: float
    smrt3A: float
    smrt3BPOS: float
    smrt3BNEG: float
        
class PicoData:
    def __init__(self, connection):
        self.smrt1Temp = -1
        self.smrt1A = -1
        self.smrt1BPOS = -1
        self.smrt1BNEG = -1
        
        self.smrt2Temp = -1
        self.smrt2A = -1
        self.smrt2BPOS = -1
        self.smrt2BNEG = -1
        
        self.smrt3Temp = -1
        self.smrt3A = -1
        self.smrt3BPOS = -1
        self.smrt3BNEG = -1
        
        self.conn = connection
        
        
    def readData(self):
        get = "g\n"
        self.conn.write(get.encode('utf-8'))
        
        self.conn.read_until("\r\n".encode('utf-8'))
        
        self.smrt1Temp = self.conn.read_until("\r\n".encode('utf-8')).decode("utf-8")
        self.smrt1A = self.conn.read_until("\r\n".encode('utf-8')).decode("utf-8")
        self.smrt1BPOS = self.conn.read_until("\r\n".encode('utf-8')).decode("utf-8")
        self.smrt1BNEG = self.conn.read_until("\r\n".encode('utf-8')).decode("utf-8")
        
        self.smrt2Temp = self.conn.read_until("\r\n".encode('utf-8')).decode("utf-8")
        self.smrt2A = self.conn.read_until("\r\n".encode('utf-8')).decode("utf-8")
        self.smrt2BPOS = self.conn.read_until("\r\n".encode('utf-8')).decode("utf-8")
        self.smrt2BNEG = self.conn.read_until("\r\n".encode('utf-8')).decode("utf-8")
        
        self.smrt3Temp = self.conn.read_until("\r\n".encode('utf-8')).decode("utf-8")
        self.smrt3A = self.conn.read_until("\r\n".encode('utf-8')).decode("utf-8")
        self.smrt3BPOS = self.conn.read_until("\r\n".encode('utf-8')).decode("utf-8")
        self.smrt3BNEG = self.conn.read_until("\r\n".encode('utf-8')).decode("utf-8")
        
        self.conn.read_until("\r\n".encode('utf-8'))
        
        
        
        self.processData()
        
    def processData(self):
        self.smrt1Temp = self.smrt1Temp[6:-2]
        self.smrt1A = self.smrt1A[6:-2]
        self.smrt1BPOS = self.smrt1BPOS[6:-2]
        self.smrt1BNEG = self.smrt1BNEG[6:-2]
        
        self.smrt2Temp = self.smrt2Temp[6:-2]
        self.smrt2A = self.smrt2A[6:-2]
        self.smrt2BPOS = self.smrt2BPOS[6:-2]
        self.smrt2BNEG = self.smrt2BNEG[6:-2]
        
        self.smrt3Temp = self.smrt3Temp[6:-2]
        self.smrt3A = self.smrt3A[6:-2]
        self.smrt3BPOS = self.smrt3BPOS[6:-2]
        self.smrt3BNEG = self.smrt3BNEG[6:-2]
        
        #print("SMRT3 ADC " + str(self.smrt3Temp))
        
    def printData(self):
        print("\n----")
        print("SMRT 1 TEMP: " + str(self.smrt1Temp))
        print("SMRT 1 A: " + str(self.smrt1A))
        print("SMRT 1 BPOS: " + str(self.smrt1BPOS))
        print("SMRT 1 BNEG: " + str(self.smrt1BNEG))
        
        print("SMRT 2 TEMP: " + str(self.smrt2Temp))
        print("SMRT 2 A: " + str(self.smrt2A))
        print("SMRT 2 BPOS: " + str(self.smrt2BPOS))
        print("SMRT 2 BNEG: " + str(self.smrt2BNEG))
        
        print("SMRT 3 TEMP: " + str(self.smrt3Temp))
        print("SMRT 3 A: " + str(self.smrt3A))
        print("SMRT 3 BPOS: " + str(self.smrt3BPOS))
        print("SMRT 3 BNEG: " + str(self.smrt3BNEG))
        
    def convertData(self):
        
        R0 = 1000
        A = 0.0039083 
        B = -0.0000005775
        
        
        self.smrt1Temp = (3.306 * int(self.smrt1Temp)) / 4096 + PICO_COMMS_VOLTAGE_DROP
        #print(self.smrt1Temp)
        I = (3.3 - self.smrt1Temp) / 1150
        radical = (R0 * A)*(R0 * A) - (4)*(R0*B)*(R0 - (self.smrt1Temp / I))
        
        if radical > 0:
            self.smrt1Temp = ((R0 * A * -1) + math.sqrt(radical)) / (2 * R0 * B)
        
        #----
        self.smrt2Temp = (3.306 * int(self.smrt2Temp)) / 4096 + PICO_COMMS_VOLTAGE_DROP + 0.02
        #print(self.smrt2Temp)
        I = (3.3 - self.smrt2Temp) / 1150
        radical = (R0 * A)*(R0 * A) - (4)*(R0*B)*(R0 - (self.smrt2Temp / I))
        
        if radical > 0:
            self.smrt2Temp = ((R0 * A * -1) + math.sqrt(radical)) / (2 * R0 * B)
        
        #----
        self.smrt3Temp = (3.306 * int(self.smrt3Temp)) / 4096 + PICO_COMMS_VOLTAGE_DROP + 0.01
        #print(self.smrt3Temp)
        I = (3.3 - self.smrt3Temp) / 1150
        radical = (R0 * A)*(R0 * A) - (4)*(R0*B)*(R0 - (self.smrt3Temp / I))
        
        if radical > 0:
            self.smrt3Temp = ((R0 * A * -1) + math.sqrt(radical)) / (2 * R0 * B)
            
        print("\n")
        
        
        #self.smrt1A = (3.3 * int(self.smrt1A)) / 4096 
        pass
        
# Gets the pi pico com port on windows  
def getCOMPort():
    device_list = list_ports.comports()
    
    for device in device_list:
        if (device.vid != None or device.pid != None):
            if (int(device.vid) == VID and int(device.pid) == PID):
                return device.device
            
    return None