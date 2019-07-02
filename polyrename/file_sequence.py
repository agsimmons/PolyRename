from pathlib import Path

from PyQt5.QtCore import QAbstractListModel


class FileSequence(QAbstractListModel):
    """A class used to represent a list of file objects"""

    def __init__(self, file_path_list):
        super().__init__()

        # self.files = [Path(file) for file in file_path_list if file.exists()]
        if file_path_list:
            self.files = [Path(file) for file in file_path_list]
        else:
            self.files = []

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.files)

    def data(self, QModelIndex, role=None):
        return self.files[QModelIndex.row()].name

    def __repr__(self):
        return str([str(file) for file in self.files])
