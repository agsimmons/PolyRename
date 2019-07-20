import shutil

from PySide2.QtWidgets import QGroupBox, QVBoxLayout, QPushButton, QListView
from PySide2.QtGui import QStandardItem, QStandardItemModel
from PySide2.QtCore import QItemSelectionModel, QModelIndex

from polyrename.file_sequence import FileSequence
from polyrename.transformation.pipeline import Pipeline


class PipelineEditor(QGroupBox):
    def __init__(self, file_picker):
        super().__init__("Pipeline Editor")

        self.setLayout(QVBoxLayout())

        self.file_picker = file_picker

        self.pipeline = Pipeline()
        self.pipelineView = QListView()

        self.pipelineView.setModel(QStandardItemModel())

        self.layout().addWidget(self.pipelineView)

        self.moveUpButton = QPushButton("Move Up")
        self.moveUpButton.clicked.connect(self._move_up_listener)
        self.moveDownButton = QPushButton("Move Down")
        self.moveDownButton.clicked.connect(self._move_down_listener)
        self.modifyButton = QPushButton("Modify")
        self.modifyButton.clicked.connect(self._modify_transformation_listener)
        self.applyButton = QPushButton("Apply")
        self.applyButton.clicked.connect(self._apply_pipeline_listener)

        self.layout().addWidget(self.moveUpButton)
        self.layout().addWidget(self.moveDownButton)
        self.layout().addWidget(self.applyButton)
        self.layout().addWidget(self.modifyButton)

        self._update_pipeline_view()

    def _update_pipeline_view(self):
        print(self.pipeline)
        model = self.pipelineView.model()
        model.clear()

        for t in range(self.pipeline.rowCount()):
            item = QStandardItem()
            item.setText(repr(self.pipeline.data(t)))
            model.appendRow(item)

    def _modify_transformation_listener(self):
        # TODO
        pass

    def _apply_pipeline_listener(self):
        file_sequence = self.file_picker.file_sequence.files
        transformed_sequence = self.pipeline.resolve(file_sequence)

        before_after = zip(file_sequence, transformed_sequence)

        for rename in before_after:
            shutil.move(rename[0], rename[1])

        # TODO: Either clear file sequence or reflect changes in file picker

    def _move_up_listener(self):
        to_move = self.pipelineView.selectionModel().selectedIndexes()[0].row()
        self.pipeline.move_transformation_up(to_move)
        self._update_pipeline_view()

    def _move_down_listener(self):
        to_move = self.pipelineView.selectionModel().selectedIndexes()[0].row()
        self.pipeline.move_transformation_down(to_move)
        self._update_pipeline_view()
