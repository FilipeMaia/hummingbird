"""Displays the results of the analysis to the user, using images and plots.
"""

import sys
from interface.Qt import QtGui, QtCore
import signal

def start_interface(restore):
    """Initialize and show the Interface"""
    # Catch Ctrl+c and such
    signal.signal(signal.SIGINT, sigint_handler)
    QtCore.QCoreApplication.setOrganizationName("SPI")
    QtCore.QCoreApplication.setOrganizationDomain("spidocs.rtfd.org")
    QtCore.QCoreApplication.setApplicationName("Hummingbird")
    app = QtGui.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    GUI(restore).show()
    sys.exit(app.exec_())

def sigint_handler(*_):
    """Handler for the SIGINT signal."""
    if QtGui.QMessageBox.question(None, '', "Are you sure you want to quit?",
                                  QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                  QtGui.QMessageBox.No) == QtGui.QMessageBox.Yes:
        GUI.instance.close()


from interface.data_source import DataSource # pylint: disable=unused-import
from interface.plotdata import PlotData # pylint: disable=unused-import
from interface.recorder import H5Recorder # pylint: disable=unused-import
from interface.ringbuffer import RingBuffer # pylint: disable=unused-import
from interface.zmqcontext import ZmqContext # pylint: disable=unused-import
from interface.zmqsocket import ZmqSocket # pylint: disable=unused-import
from interface.gui import GUI
