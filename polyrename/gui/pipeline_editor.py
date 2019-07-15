from PySide2.QtWidgets import QGroupBox, QVBoxLayout


class PipelineEditor(QGroupBox):
    def __init__(self):
        super().__init__("Pipeline Editor")

        self.setLayout(QVBoxLayout())
