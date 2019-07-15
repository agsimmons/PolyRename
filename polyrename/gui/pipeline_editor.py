from PySide2.QtWidgets import QGroupBox, QVBoxLayout, QPushButton, QListView

from polyrename.transformation.pipeline import Pipeline


class PipelineEditor(QGroupBox):
    def __init__(self):
        super().__init__("Pipeline Editor")

        self.setLayout(QVBoxLayout())

        self.pipeline = Pipeline()
        self.pipelineView = QListView()

        self.layout().addWidget(self.pipelineView)

        self.moveUpButton = QPushButton("Move Up")
        self.moveDownButton = QPushButton("Move Down")
        self.applyButton = QPushButton("Apply")

        self.layout().addWidget(self.moveUpButton)
        self.layout().addWidget(self.moveDownButton)
        self.layout().addWidget(self.applyButton)

        model = self.pipelineView.model()
