from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import pyautogui
from utils.ui_generator import *

class MasterTab(QWidget):
    def __init__(self):
        super(MasterTab, self).__init__()

        self.startStopButton = createButton("Start", self, 0, 0)
        self.startStopButton.released.connect(self._PrintStart)

        self.terminateButton = createButton("Terminate", self, 1, 0)
        self.terminateButton.released.connect(self._PrintStop)

        self.controllerLabel = createLabelLText("Ready", self, 0, 1)

    def _PrintStart(self):
    	print('Start')
    def _PrintStop(self):
    	print('Stop')