import argparse
from pathlib import Path
import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QListView, QWidget, QTextEdit, QListWidget


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+')
    return parser.parse_args()


class Window(QMainWindow):
    def __init__(self, file_sequence):
        super().__init__()

        self.title = 'PolyRename'
        self.top = 100
        self.left = 100
        self.width = 640
        self.height = 480

        self.file_sequence = file_sequence

        self.init_window()
        self.populate_file_selection()

        self.show()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Left pane - Pipeline creator and transformation library
        left_pane = QVBoxLayout()
        self.pipeline_creator = QListView()
        left_pane.addWidget(self.pipeline_creator)

        self.transformation_library = QListView()
        left_pane.addWidget(self.transformation_library)

        # Right pane - File selection and transformation configuration
        right_pane = QVBoxLayout()
        self.file_selection = QListWidget()
        right_pane.addWidget(self.file_selection)
        self.transformation_config = QTextEdit()
        right_pane.addWidget(self.transformation_config)

        hbox_layout = QHBoxLayout()
        hbox_layout.addItem(left_pane)
        hbox_layout.addItem(right_pane)

        content = QWidget()
        content.setLayout(hbox_layout)

        self.setCentralWidget(content)

    def populate_file_selection(self):
        for file in self.file_sequence:
            self.file_selection.addItem(file.name)


def main():
    args = parse_args()
    file_sequence = [Path(file) for file in args.files]
    print(args.files)
    print(file_sequence)

    app = QApplication(sys.argv)
    window = Window(file_sequence)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
