from core import keyFunctions, export
from view import gui

class Controller(object):
    def __init__(self):
        self.kf = keyFunctions.KeyFunctions()

        self.cbFunctions = {
            "recordKeys": self.kf.start,
            "executeKeys": self.kf.execute,
            "exportSingle": export.exportSingle,
            "exportMulti": export.exportMulti,
        }

        self.gui = gui.MainGUI(self.cbFunctions)
    


controller = Controller()