# import gui
# import threading
# import serial

# import sys
# import usb
# from collections import deque

# message_queue = deque()
# message_queue.append
# shouldClose = False
# app = gui.App()

# def myUSBThread():
#         print("Starting USB Thread")
#         ser = serial.Serial("COM15", 115200)  # open serial port
#         print(ser.name)
        
#         while True:
#             #line = ser.readline()
#             #print(str(line))
            
#             if shouldClose is True:
#                 print("CLOSING USB")
#                 ser.close()
        

#     # backend = usb.backend.libusb1.get_backend(find_library=lambda x: "C:\\Users\\vlad\\Desktop\\ghgcuyt\\aeqrtgyswer\\VS2022\\MS64\\dll\\libusb-1.0.dll")
#     # dev = usb.core.find(idVendor=0x2E8A, idProduct=0x0003, backend=backend)
    
#     # data = dev.read(1, 100)
    

# try:
#     usbThread = threading.Thread(target = myUSBThread)
#     usbThread.daemon = True
#     usbThread.start()
    
        

#     app.mainloop()
    
    
# except KeyboardInterrupt:
#     print("ctrl+c pressed")
#     app.destroy()
#     usbThread.join()
#     shouldClose = True
    

