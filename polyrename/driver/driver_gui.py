import signal
import sys

from PySide2.QtWidgets import QApplication

from polyrename.driver.gui.main_window import MainWindow


def main(files):
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication(sys.argv)

    # TODO: Use files as initial file sequence
    window = MainWindow()

    sys.exit(app.exec_())
