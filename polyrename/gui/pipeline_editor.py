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
        self.moveUpButton.clicked.connect(self._move_up_listener)
        self.moveDownButton = QPushButton("Move Down")
        self.moveDownButton.clicked.connect(self._move_down_listener)
        self.modifyButton = QPushButton("Modify")
        self.modifyButton.clicked.connect(self._modify_transformation_listener)
        self.applyButton = QPushButton("Apply")
        self.applyButton.clicked.connect(self._apply_pipeline_listener)

        #TODO remove
        self.refreshButton = QPushButton("refresh")
        self.refreshButton.clicked.connect(self._update_pipeline_view)

        self.layout().addWidget(self.moveUpButton)
        self.layout().addWidget(self.moveDownButton)
        self.layout().addWidget(self.applyButton)
        self.layout().addWidget(self.refreshButton)

        self._update_pipeline_view()


    def _update_pipeline_view(self):
        self.pipelineView.setModel(self.pipeline)

    def _modify_transformation_listener(self):
        #TODO
        pass

    def _apply_pipeline_listener(self):
        #TODO
        #self.pipeline.resolve()
        pass

    def _move_up_listener(self):
        self.pipeline.move_transformation_up(1)
        self._update_pipeline_view()

    def _move_down_listener(self):
        self.pipeline.move_transformation_down(0)
        self._update_pipeline_view()
