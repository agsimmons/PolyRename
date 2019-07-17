from PySide2.QtWidgets import QGroupBox, QVBoxLayout, QPushButton, QListView
from PySide2.QtGui import QStandardItem, QStandardItemModel

from polyrename.transformation.pipeline import Pipeline


class PipelineEditor(QGroupBox):
    def __init__(self):
        super().__init__("Pipeline Editor")

        self.setLayout(QVBoxLayout())

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
        #TODO
        pass

    def _apply_pipeline_listener(self):
        #TODO
        #self.pipeline.resolve()
        pass

    def _move_up_listener(self):
        self.pipeline.move_transformation_up(self.pipelineView.selectedIndexes()[0].row())
        self._update_pipeline_view()

    def _move_down_listener(self):
        self.pipeline.move_transformation_down(self.pipelineView.selectedIndexes()[0].row())
        self._update_pipeline_view()
