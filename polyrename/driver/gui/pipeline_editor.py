import logging
import shutil

from PySide2.QtWidgets import (
    QGroupBox,
    QVBoxLayout,
    QPushButton,
    QListView,
    QMessageBox,
    QHBoxLayout,
    QAbstractItemView,
    QWidget,
)
from PySide2.QtGui import QStandardItem, QStandardItemModel

from polyrename.transformation.pipeline import Pipeline


class PipelineEditor(QGroupBox):
    def __init__(self, file_picker):
        super().__init__("Pipeline Editor")

        self.setLayout(QVBoxLayout())

        self.file_picker = file_picker

        self.pipeline = Pipeline()
        self.pipelineView = QListView()
        self.pipelineView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.pipelineView.setModel(QStandardItemModel())

        self.layout().addWidget(self.pipelineView)

        # === BUTTON CONTAINER ===
        button_rows = QWidget()
        self.layout().addWidget(button_rows)
        button_rows_layout = QVBoxLayout(button_rows)
        button_rows_layout.setContentsMargins(0, 0, 0, 0)

        # === ROW 1 ===
        row_1 = QWidget()
        button_rows_layout.addWidget(row_1)
        row_1_layout = QHBoxLayout(row_1)
        row_1_layout.setContentsMargins(0, 0, 0, 0)

        self.moveUpButton = QPushButton("Move Up")
        row_1_layout.addWidget(self.moveUpButton)
        self.moveUpButton.clicked.connect(self._move_up_listener)

        self.moveDownButton = QPushButton("Move Down")
        row_1_layout.addWidget(self.moveDownButton)
        self.moveDownButton.clicked.connect(self._move_down_listener)

        self.deleteButton = QPushButton("Delete")
        row_1_layout.addWidget(self.deleteButton)
        self.deleteButton.clicked.connect(self._delete_listener)

        # === ROW 2 ===
        row_2 = QWidget()
        button_rows_layout.addWidget(row_2)
        row_2_layout = QHBoxLayout(row_2)
        row_2_layout.setContentsMargins(0, 0, 0, 0)

        self.applyButton = QPushButton("Apply Pipeline")
        row_2_layout.addWidget(self.applyButton)
        self.applyButton.clicked.connect(self._apply_pipeline_listener)

        self.update_pipeline_view()

    def update_pipeline_view(self):
        logging.debug(self.pipeline)
        model = self.pipelineView.model()
        model.clear()

        for t in range(self.pipeline.rowCount()):
            item = QStandardItem()
            item.setText(repr(self.pipeline.data(t)))
            model.appendRow(item)

    def _modify_transformation_listener(self):
        # TODO
        raise NotImplementedError

    def _move_up_listener(self):
        try:
            to_move = self.pipelineView.selectionModel().selectedIndexes()[0].row()
            if to_move < 1:
                return
            self.pipeline.move_transformation_up(to_move)
            self.update_pipeline_view()
            self.pipelineView.setCurrentIndex(
                self.pipelineView.model().index(to_move - 1, 0)
            )
        except IndexError:
            return

    def _move_down_listener(self):
        try:
            to_move = self.pipelineView.selectionModel().selectedIndexes()[0].row()
            if to_move > self.pipelineView.model().rowCount() - 2:
                return
            self.pipeline.move_transformation_down(to_move)
            self.update_pipeline_view()
            self.pipelineView.setCurrentIndex(
                self.pipelineView.model().index(to_move + 1, 0)
            )
        except IndexError:
            return

    def _delete_listener(self):
        try:
            to_delete = self.pipelineView.selectionModel().selectedIndexes()[0].row()
            self.pipeline.remove_transformation(to_delete)
            self.update_pipeline_view()
            if to_delete > self.pipelineView.model().rowCount() - 1:
                self.pipelineView.setCurrentIndex(
                    self.pipelineView.model().index(to_delete - 1, 0)
                )
            else:
                self.pipelineView.setCurrentIndex(
                    self.pipelineView.model().index(to_delete, 0)
                )
        except IndexError:
            return

    def _apply_pipeline_listener(self):
        # Check that at least one transformation has been added to the pipeline
        if self.pipeline.rowCount() == 0:
            no_transformations_messagebox = QMessageBox(self)
            no_transformations_messagebox.setText("ERROR: No transformations selected")
            no_transformations_messagebox.exec_()
            return

        file_sequence = self.file_picker.file_sequence.files

        # Check that at least one file has been added to the file sequence
        if len(file_sequence) == 0:
            no_files_messagebox = QMessageBox(self)
            no_files_messagebox.setText("ERROR: No files selected")
            no_files_messagebox.exec_()
            return

        transformed_sequence = self.pipeline.resolve(file_sequence)

        before_after = list(zip(file_sequence, transformed_sequence))

        preview_text_lines = []
        for rename in before_after:
            preview_text_lines.append(f"{rename[0].name} -> {rename[1].name}")
        preview_text = "\n".join(preview_text_lines)

        confirmation = QMessageBox(self)
        confirmation.setText("Are you sure you want to apply the pipeline?")
        confirmation.setDetailedText(preview_text)
        confirmation.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirmation.setDefaultButton(QMessageBox.No)
        ret = confirmation.exec_()

        if ret == int(QMessageBox.Yes):
            for rename in before_after:
                from_path = rename[0]
                to_path = rename[1]
                
                shutil.move(str(from_path), str(to_path))
            self.file_picker.clear_file_list()
