import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QListView, QWidget, QTextEdit, \
    QListWidget, QDesktopWidget, QGridLayout, QGroupBox, QPushButton, QFileDialog, QAction

from polyrename.file_sequence import FileSequence


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.file_sequence = FileSequence([])

        self.init_window()
        self.init_menuBar()
        self.init_statusBar()
        self.init_layout()

        self.show()

    def init_window(self):
        self.setWindowTitle('PolyRename')
        self.resize(1280, 720)

        # Center window on screen
        # TODO: Test on multi-monitors
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def init_layout(self):
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

        pipeline_editor = QGroupBox('Pipeline Editor')
        grid_layout.addWidget(pipeline_editor, 0, 0)

        transformation_library = QGroupBox('Transformation Library')
        grid_layout.addWidget(transformation_library, 1, 0)

        file_picker_group = QGroupBox('File Picker')
        file_picker_group_layout = QVBoxLayout()
        file_picker_group.setLayout(file_picker_group_layout)
        file_picker = QListView()
        file_picker.setModel(self.file_sequence)
        file_picker_group.layout().addWidget(file_picker)
        select_files = QPushButton("Select Files")
        select_files.clicked.connect(self.select_files_listener)
        file_picker_group.layout().addWidget(select_files)
        grid_layout.addWidget(file_picker_group, 0, 1)

        transformation_config = QGroupBox('Transformation Config')
        grid_layout.addWidget(transformation_config, 1, 1)

        central_widget = QWidget()
        central_widget.setLayout(grid_layout)
        self.setCentralWidget(central_widget)

    def init_menuBar(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        editMenu = menuBar.addMenu('&Edit')
        helpMenu = menuBar.addMenu('&Help')

        selectFileAction = QAction('S&elect Files', self)
        selectFileAction.setShortcut('Ctrl+e')
        selectFileAction.setStatusTip('Select Files')
        selectFileAction.triggered.connect(self.select_files_listener)
        fileMenu.addAction(selectFileAction)

        quitAction = QAction('&Quit', self)
        quitAction.setShortcut('Ctrl+q')
        quitAction.setStatusTip('Quit PolyRename')
        quitAction.triggered.connect(self.close)
        fileMenu.addAction(quitAction)

        undoAction = QAction("&Undo", self)
        undoAction.setShortcut("Ctrl+Z")
        undoAction.setStatusTip('Undo last action')
        editMenu.addAction(undoAction)

        redoAction = QAction("&Redo", self)
        redoAction.setShortcut("Ctrl+Shift+Z")
        redoAction.setStatusTip('Redo last action')
        editMenu.addAction(redoAction)

        aboutAction = QAction('&About', self)
        aboutAction.setShortcut('Ctrl+?')
        aboutAction.setStatusTip('About PolyRename')
        helpMenu.addAction(aboutAction)

    def init_statusBar(self):
        statusBar = self.statusBar()
        statusBar.showMessage('Ready')

    def select_files_listener(self):
        files = QFileDialog.getOpenFileNames(self, 'Select Files', '.')
        self.file_sequence = FileSequence(files[0])
        print(self.file_sequence)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
