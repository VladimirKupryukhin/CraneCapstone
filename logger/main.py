import gui
import sys

app = gui.App()



try:
    app.mainloop()
except KeyboardInterrupt:
    print("ctrl+c pressed")
    app.destroy()
    sys.exit(0)