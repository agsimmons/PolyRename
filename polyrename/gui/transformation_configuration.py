from PySide2.QtWidgets import QGroupBox, QVBoxLayout, QScrollArea, QWidget, QFormLayout


class TransformationConfiguration(QGroupBox):
    def __init__(self):
        super().__init__("Transformation Config")

        self.setLayout(QVBoxLayout())

        self._initialize_scroll_area()

    def _initialize_scroll_area(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        self.config_form = QFormLayout()

        form_widget = QWidget()
        form_widget.setLayout(self.config_form)

        scroll_area.setWidget(form_widget)

        self.layout().addWidget(scroll_area)
