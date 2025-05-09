import gui
import sys
import usbThread
import serial
import threading


app = gui.App()



try:
    usbThread = threading.Thread(target = usbThread.usbThreadEntry)
    usbThread.daemon = True
    usbThread.start()
    
    app.mainloop()
except KeyboardInterrupt:
    print("ctrl+c pressed")
    usbThread.join()
    app.destroy()
    sys.exit(0)