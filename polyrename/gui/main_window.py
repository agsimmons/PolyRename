from PySide2.QtWidgets import QMainWindow, QWidget, QDesktopWidget, QGridLayout, QAction

from polyrename.gui import (
    FilePicker,
    TransformationLibrary,
    TransformationConfiguration,
    PipelineEditor,
)
from polyrename.transformation.pipeline import Pipeline


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pipeline = Pipeline()

        self.init_window()
        self.init_layout()
        self.init_menu_bar()

        self.show()

    def init_window(self):
        """Initialize main window size and position"""

        self.setWindowTitle("PolyRename")
        self.resize(1280, 720)

        # Center window on screen
        # TODO: Test on multi-monitors
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def init_menu_bar(self):
        """Initialize Menu Bar and contained menus"""

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&File")
        editMenu = menuBar.addMenu("&Edit")
        helpMenu = menuBar.addMenu("&Help")

        selectFileAction = QAction("S&elect Files", self)
        selectFileAction.setShortcut("Ctrl+e")
        selectFileAction.setStatusTip("Select Files")
        selectFileAction.triggered.connect(self.file_picker._select_files_listener)
        fileMenu.addAction(selectFileAction)

        quitAction = QAction("&Quit", self)
        quitAction.setShortcut("Ctrl+q")
        quitAction.setStatusTip("Quit PolyRename")
        quitAction.triggered.connect(self.close)
        fileMenu.addAction(quitAction)

        undoAction = QAction("&Undo", self)
        undoAction.setShortcut("Ctrl+Z")
        undoAction.setStatusTip("Undo last action")
        editMenu.addAction(undoAction)

        redoAction = QAction("&Redo", self)
        redoAction.setShortcut("Ctrl+Shift+Z")
        redoAction.setStatusTip("Redo last action")
        editMenu.addAction(redoAction)

        aboutAction = QAction("&About", self)
        aboutAction.setShortcut("Ctrl+?")
        aboutAction.setStatusTip("About PolyRename")
        helpMenu.addAction(aboutAction)

        # Initialize Status Bar
        statusBar = self.statusBar()
        statusBar.showMessage("Ready")

    def init_layout(self):
        """Initialize layout of main window, including the four main sections of the UI"""

        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

        # Initialize each quadrant
        self.pipeline_editor = PipelineEditor()
        grid_layout.addWidget(self.pipeline_editor, 0, 0)

        self.file_picker = FilePicker()
        grid_layout.addWidget(self.file_picker, 0, 1)

        self.transformation_configuration = TransformationConfiguration()
        grid_layout.addWidget(self.transformation_configuration, 1, 1)

        self.transformation_library = TransformationLibrary(
            self.transformation_configuration.config_form
        )
        grid_layout.addWidget(self.transformation_library, 1, 0)

        central_widget = QWidget()
        central_widget.setLayout(grid_layout)
        self.setCentralWidget(central_widget)
