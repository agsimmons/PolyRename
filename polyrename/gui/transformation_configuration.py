from PySide2.QtWidgets import (
    QGroupBox,
    QVBoxLayout,
    QScrollArea,
    QWidget,
    QFormLayout,
    QLabel,
    QTextEdit,
)
from PySide2.QtGui import QFontMetrics


class TransformationConfiguration(QGroupBox):
    def __init__(self):
        super().__init__("Transformation Config")

        self.setLayout(QVBoxLayout())

        self._initialize_text()
        self._initialize_scroll_area()

    def _initialize_text(self):
        metrics = QFontMetrics(QTextEdit().font())
        self.text_line_height = metrics.lineSpacing() * 2

    def _initialize_scroll_area(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        self.config_form = QFormLayout()

        form_widget = QWidget()
        form_widget.setLayout(self.config_form)

        scroll_area.setWidget(form_widget)

        self.layout().addWidget(scroll_area)

    def swap_configuration(self, selected_transformation):
        """Swap config form with that of selected_transformation"""

        # Destroy existing form rows
        for i in reversed(range(self.config_form.count())):
            self.config_form.itemAt(i).widget().setParent(None)

        # Generate configuration for selected Transformation
        for option in selected_transformation.schema["options"]:

            label = QLabel(option["name"])
            label.setToolTip(option["description"])

            field = QTextEdit("Testing")
            field.setFixedHeight(self.text_line_height)

            self.config_form.addRow(label, field)
