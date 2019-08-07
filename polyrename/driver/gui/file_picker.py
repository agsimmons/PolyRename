import logging

from PySide2.QtWidgets import (
    QGroupBox,
    QVBoxLayout,
    QListView,
    QAbstractItemView,
    QPushButton,
    QFileDialog,
)
from PySide2.QtGui import QStandardItem, QStandardItemModel

from polyrename.file_sequence import FileSequence


class FilePicker(QGroupBox):
    def __init__(self, files):
        super().__init__("File Picker")

        self.setLayout(QVBoxLayout())

        self.file_sequence = FileSequence([])

        self._initialize_file_list()

        self.file_sequence = FileSequence(files)
        self._update_file_picker_list([str(file) for file in files])

    def log_file_sequence_status(self):
        logging.debug(f"Current file sequence: {self.file_sequence}")

    def clear_file_list(self):
        self.file_sequence = FileSequence([])
        self.file_list.model().clear()
        self.log_file_sequence_status()

    def _initialize_file_list(self):
        self.file_list = QListView()
        self.file_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.layout().addWidget(self.file_list)

        self.file_list.setModel(QStandardItemModel())

        select_files = QPushButton("Select Files")
        select_files.clicked.connect(self._select_files_listener)
        self.layout().addWidget(select_files)

    def _update_file_picker_list(self, file_names):
        model = self.file_list.model()

        # Update File Picker list from files[]
        model.clear()
        for f in range(self.file_sequence.rowCount()):
            item = QStandardItem()
            item.setText(file_names[f])
            model.appendRow(item)

        self.log_file_sequence_status()

    def _select_files_listener(self):
        """Handles selection of files to rename"""

        files = QFileDialog.getOpenFileNames(self, "Select Files", ".")
        self.file_sequence = FileSequence(files[0])

        self._update_file_picker_list(files[0])
