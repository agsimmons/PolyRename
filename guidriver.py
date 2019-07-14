import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QListView, QWidget, QTextEdit, \
    QListWidget, QDesktopWidget, QGridLayout, QGroupBox, QPushButton, QFileDialog, QAction, QAbstractItemView, QLabel
from PySide2.QtGui import QStandardItem, QStandardItemModel

from polyrename.file_sequence import FileSequence
from polyrename.transformation import TRANSFORMATIONS, TRANSFORMATIONS_BY_NAME


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
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(10)

        # Init each quadrant
        self.pipeline_editor_layout()
        self.transformation_library_layout()
        self.file_picker_layout()
        self.transformation_configuration_layout()

        central_widget = QWidget()
        central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(central_widget)

    def pipeline_editor_layout(self):
        pipeline_editor = QGroupBox('Pipeline Editor')
        self.grid_layout.addWidget(pipeline_editor, 0, 0)

    def transformation_library_layout(self):
        transformation_library_group = QGroupBox('Transformation Library')

        transformation_library_group_layout = QVBoxLayout()
        transformation_library_group.setLayout(transformation_library_group_layout)

        self.transformation_library = QListView()
        self.transformation_library.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.transformation_library_model = QStandardItemModel()
        self.transformation_library.setModel(self.transformation_library_model)
        self.transformation_library.clicked.connect(self.configure_transformation)

        for transformation in TRANSFORMATIONS:
            transformation_name = transformation.schema['metadata']['name']
            transformation_description = transformation.schema['metadata']['description']

            transformation_element = QStandardItem()
            transformation_element.setText(transformation_name)
            transformation_element.setToolTip(transformation_description)

            self.transformation_library_model.appendRow(transformation_element)

        transformation_library_group.layout().addWidget(self.transformation_library)

        self.grid_layout.addWidget(transformation_library_group, 1, 0)

    def file_picker_layout(self):
        file_picker_group = QGroupBox('File Picker')
        file_picker_group_layout = QVBoxLayout()
        file_picker_group.setLayout(file_picker_group_layout)
        self.file_picker = QListView()
        self.file_picker.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.file_model = QStandardItemModel()
        file_picker_group.layout().addWidget(self.file_picker)
        select_files = QPushButton("Select Files")
        select_files.clicked.connect(self.select_files_listener)
        file_picker_group.layout().addWidget(select_files)
        self.grid_layout.addWidget(file_picker_group, 0, 1)

    def transformation_configuration_layout(self):
        transformation_config = QGroupBox('Transformation Config')
        self.grid_layout.addWidget(transformation_config, 1, 1)

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

        # Update File Picker list from files[]
        self.file_model.clear()
        for f in range(self.file_sequence.rowCount()):
            item = QStandardItem()
            item.setText(files[0][f])
            self.file_model.appendRow(item)
        self.file_picker.setModel(self.file_model)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
