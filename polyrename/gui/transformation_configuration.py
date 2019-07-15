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


CONFIG_FIELD_HEIGHT_SCALER = 2


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
        self.text_line_height = metrics.lineSpacing() * CONFIG_FIELD_HEIGHT_SCALER

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

    def _clear_form(self):
        for i in reversed(range(self.config_form.count())):
            self.config_form.itemAt(i).widget().setParent(None)

    def swap_configuration(self, selected_transformation):
        """Swap config form with that of selected_transformation"""

        self.selected_transformation = selected_transformation

        self._clear_form()

        # Generate configuration for selected Transformation
        for option in selected_transformation.schema["options"]:

            label = QLabel(option["name"])
            label.setToolTip(option["description"])

            # TODO: Determine value of field based on default value
            field = QTextEdit("Testing")
            field.setFixedHeight(self.text_line_height)

            self.config_form.addRow(label, field)

    def add_configured_transformation_to_pipeline(self):

        # Return if a transformation hasn't been selected yet
        if self.selected_transformation is None:
            return

        # Get form options
        form_options = []
        for i in range(self.config_form.count()):

            # Skip labels in the form
            if i % 2 == 0:
                continue

            configurated_field = self.config_form.itemAt(i).widget()
            form_options.append(configurated_field.toPlainText())

        print("Selected options: {}".format(form_options))

        option_types = []
        for option in self.selected_transformation.schema["options"]:
            option_types.append(option["datatype"])
        print("Option types: {}".format(option_types))

        # Convert form options to correct datatype
        for i in range(len(form_options)):
            form_options[i] = option_types[i](form_options[i])

        print("Casted options: {}".format(form_options))

        configured_transformation = self.selected_transformation(*form_options)

        print("Configured Transformation: {}".format(configured_transformation))

        self._clear_form()

        self.pipeline_editor.pipeline.add_transformation(configured_transformation)
