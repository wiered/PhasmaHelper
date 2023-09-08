import ctypes
import time
from threading import Thread

import keyboard

from app import App, configure_colors
from config import cfg

__version__ = "1.0-rc2"

def on_closing(app):
    app.destroy()

if __name__ == "__main__":
    myappid = 'wrds.phasmahelper.phasmahelper.10rc2' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    configure_colors(cfg.appearance, cfg.color_theme)

    app = App(__version__)
    app.protocol("WM_DELETE_WINDOW", lambda: on_closing(app))
    app.mainloop()