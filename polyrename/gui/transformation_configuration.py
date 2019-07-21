from PySide2.QtWidgets import (
    QGroupBox,
    QVBoxLayout,
    QScrollArea,
    QWidget,
    QFormLayout,
    QLabel,
    QTextEdit,
    QPushButton,
)
from PySide2.QtGui import QFontMetrics


class TransformationConfiguration(QGroupBox):
    def __init__(self, pipeline_editor):
        super().__init__("Transformation Config")

        self.pipeline_editor = pipeline_editor

        self.selected_transformation = None

        self.setLayout(QVBoxLayout())

        self._initialize_text()
        self._initialize_scroll_area()
        self._initialize_add_button()

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

    def _initialize_add_button(self):
        add_button = QPushButton("Add to Pipeline")
        add_button.clicked.connect(self.add_configured_transformation_to_pipeline)

        self.layout().addWidget(add_button)

    def swap_configuration(self, selected_transformation):
        """Swap config form with that of selected_transformation"""

        self.selected_transformation = selected_transformation

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

    def add_configured_transformation_to_pipeline(self):
        # Get form options
        form_options = []
        for i in range(self.config_form.count()):

            # Skip labels in the form
            if i % 2 == 0:
                continue

            configurated_field = self.config_form.itemAt(i).widget()
            form_options.append(configurated_field.toPlainText())

        print("Selected options: {}".format(form_options))

        option_types = [
            option["datatype"]
            for option in self.selected_transformation.schema["options"]
        ]
        print("Option types: {}".format(option_types))

        # Convert form options to correct datatype
        for i in range(len(form_options)):
            form_options[i] = option_types[i](form_options[i])

        print("Casted options: {}".format(form_options))

        configured_transformation = self.selected_transformation(*form_options)

        print("Configured Transformation: {}".format(configured_transformation))

        self.pipeline_editor.pipeline.add_transformation(configured_transformation)
        self.pipeline_editor.update_pipeline_view()
