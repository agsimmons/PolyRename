import sys

from PySide2.QtWidgets import QApplication

from polyrename.gui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
