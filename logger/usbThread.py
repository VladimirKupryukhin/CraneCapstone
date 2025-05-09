import serial
import time
from serial.tools import list_ports

VID = 11914
PID = 10

def usbThreadEntry():
    print("Starting USB Thread")
    
    conn = serial.Serial(str(getCOMPort()), 115200)
    #conn.timeout = 0.1
    print(conn.name)
    
    while True:
        get = "g\n"
        conn.write(get.encode('utf-8'))
        print("SENT:   " + str(get.encode('utf-8')))
        #line1 = conn.read_until("\r\n".encode('utf-8'))
        
        print("READ:   " + str(conn.read_until("\r\n".encode('utf-8'))))
        
        print("READ:   " + str(conn.read_until("\r\n".encode('utf-8'))))
        print("READ:   " + str(conn.read_until("\r\n".encode('utf-8'))))
        print("READ:   " + str(conn.read_until("\r\n".encode('utf-8'))))
        print("READ:   " + str(conn.read_until("\r\n".encode('utf-8'))))
        
        print("READ:   " + str(conn.read_until("\r\n".encode('utf-8'))))
        print("READ:   " + str(conn.read_until("\r\n".encode('utf-8'))))
        print("READ:   " + str(conn.read_until("\r\n".encode('utf-8'))))
        print("READ:   " + str(conn.read_until("\r\n".encode('utf-8'))))
        
        print("READ:   " + str(conn.read_until("\r\n".encode('utf-8'))))
        print("READ:   " + str(conn.read_until("\r\n".encode('utf-8'))))
        print("READ:   " + str(conn.read_until("\r\n".encode('utf-8'))))
        print("READ:   " + str(conn.read_until("\r\n".encode('utf-8'))))
        
        print("READ:   " + str(conn.read_until("\r\n".encode('utf-8'))))
        
        print("\n")
        time.sleep(1)
        
        
# Gets the pi pico com port on windows  
def getCOMPort():
    device_list = list_ports.comports()
    
    for device in device_list:
        if (device.vid != None or device.pid != None):
            if (int(device.vid) == VID and int(device.pid) == PID):
                return device.device
            
    return None