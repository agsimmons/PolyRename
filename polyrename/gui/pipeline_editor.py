import shutil

from PySide2.QtWidgets import QGroupBox, QVBoxLayout, QPushButton, QListView, QMessageBox
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
        self.applyButton = QPushButton("Apply Pipeline")
        self.applyButton.clicked.connect(self._apply_pipeline_listener)
        # self.modifyButton = QPushButton("Modify")
        # self.modifyButton.clicked.connect(self._modify_transformation_listener)

        self.layout().addWidget(self.moveUpButton)
        self.layout().addWidget(self.moveDownButton)
        self.layout().addWidget(self.applyButton)
        # self.layout().addWidget(self.modifyButton)

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

        before_after = list(zip(file_sequence, transformed_sequence))

        preview_text_lines = []
        for rename in before_after:
            preview_text_lines.append(f"{rename[0].name} -> {rename[1].name}")
        preview_text = '\n'.join(preview_text_lines)

        confirmation = QMessageBox(self)
        confirmation.setText("Are you sure you want to apply the pipeline?")
        confirmation.setDetailedText(preview_text)
        confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirmation.setDefaultButton(QMessageBox.No)
        ret = confirmation.exec_()

        if ret == int(QMessageBox.Yes):
            for rename in before_after:
                shutil.move(*rename)

        # TODO: Either clear file sequence or reflect changes in file picker

    def _move_up_listener(self):
        to_move = self.pipelineView.selectionModel().selectedIndexes()[0].row()
        self.pipeline.move_transformation_up(to_move)
        self._update_pipeline_view()

    def _move_down_listener(self):
        to_move = self.pipelineView.selectionModel().selectedIndexes()[0].row()
        self.pipeline.move_transformation_down(to_move)
        self._update_pipeline_view()
