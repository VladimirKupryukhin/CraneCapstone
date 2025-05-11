import gui
import sys
import usbThread
import serial
import threading
from collections import deque




dataQueue = deque()
app = gui.App(dataQueue)

try:
    usbThread = threading.Thread(target = usbThread.usbThreadEntry, args=(dataQueue,))
    usbThread.daemon = True
    usbThread.start()
    
    app.mainloop()
except KeyboardInterrupt:
    print("ctrl+c pressed")
    usbThread.join()
    app.destroy()
    sys.exit(0)