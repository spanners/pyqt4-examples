import sys
import time
from PyQt4 import QtCore, QtGui

app = QtGui.QApplication(sys.argv)

try:
    due = QtCore.QTime.currentTime()
    message = "Alert!"
    if len(sys.argv) < 2:
        raise ValueError
    hours, mins = sys.argv[1].split(":")
    due = QtCore.QTime(int(hours), int(mins))
    if not due.isValid():
        raise ValueError
    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])
except ValueError:
    message = "Usage: alert.pyw HH:MM [optional message]" # 24hr clock

while QtCore.QTime.currentTime() < due:
    time.sleep(20) # 20 seconds

label = QtGui.QLabel("<font color=red size=72><b>" + message + "</b></font>")
label.setWindowFlags(QtCore.Qt.SplashScreen)
label.show()
QtCore.QTimer.singleShot(60000, app.quit) # 1 minute
app.exec_()
