from PySide2.QtWidgets import QMainWindow, QWidget, QDesktopWidget, QGridLayout, QAction

from polyrename.gui import (
    FilePicker,
    TransformationLibrary,
    TransformationConfiguration,
    PipelineEditor,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_window()
        self.init_layout()

        # Initialize each quadrant
        self.file_picker = FilePicker()
        self.grid_layout.addWidget(self.file_picker, 0, 1)

        self.pipeline_editor = PipelineEditor(self.file_picker)
        self.grid_layout.addWidget(self.pipeline_editor, 0, 0)

        self.transformation_configuration = TransformationConfiguration(
            self.pipeline_editor
        )
        self.grid_layout.addWidget(self.transformation_configuration, 1, 1)

        self.transformation_library = TransformationLibrary(
            self.transformation_configuration
        )
        self.grid_layout.addWidget(self.transformation_library, 1, 0)

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

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        edit_menu = menu_bar.addMenu("&Edit")
        help_menu = menu_bar.addMenu("&Help")

        select_file_action = QAction("S&elect Files", self)
        select_file_action.setShortcut("Ctrl+e")
        select_file_action.setStatusTip("Select Files")
        select_file_action.triggered.connect(self.file_picker._select_files_listener)
        file_menu.addAction(select_file_action)

        quit_action = QAction("&Quit", self)
        quit_action.setShortcut("Ctrl+q")
        quit_action.setStatusTip("Quit PolyRename")
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)

        undo_action = QAction("&Undo", self)
        undo_action.setShortcut("Ctrl+Z")
        undo_action.setStatusTip("Undo last action")
        edit_menu.addAction(undo_action)

        redo_action = QAction("&Redo", self)
        redo_action.setShortcut("Ctrl+Shift+Z")
        redo_action.setStatusTip("Redo last action")
        edit_menu.addAction(redo_action)

        about_action = QAction("&About", self)
        about_action.setShortcut("Ctrl+?")
        about_action.setStatusTip("About PolyRename")
        help_menu.addAction(about_action)

        # Initialize Status Bar
        status_bar = self.statusBar()
        status_bar.showMessage("Ready")

    def init_layout(self):
        """Initialize base layout of main windows"""

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(10)

        central_widget = QWidget()
        central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(central_widget)
