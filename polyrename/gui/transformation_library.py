from PySide2.QtWidgets import (
    QGroupBox,
    QVBoxLayout,
    QListView,
    QAbstractItemView,
    QLabel,
    QTextEdit,
)
from PySide2.QtGui import QStandardItemModel, QStandardItem

from polyrename.transformation import TRANSFORMATIONS, TRANSFORMATIONS_BY_NAME


class TransformationLibrary(QGroupBox):
    def __init__(self, config_form):
        super().__init__("Transformation Library")

        self.config_form = config_form

        self.setLayout(QVBoxLayout())

        self._initialize_library()

    def _initialize_library(self):
        self.transformation_list = QListView()
        self.transformation_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.layout().addWidget(self.transformation_list)

        self.transformation_list.setModel(QStandardItemModel())

        self.transformation_list.clicked.connect(self.configure_transformation)

        # Populate transformations list
        for transformation in TRANSFORMATIONS:
            transformation_name = transformation.schema["metadata"]["name"]
            transformation_description = transformation.schema["metadata"][
                "description"
            ]

            transformation_element = QStandardItem()
            transformation_element.setText(transformation_name)
            transformation_element.setToolTip(transformation_description)

            self.transformation_list.model().appendRow(transformation_element)

    def configure_transformation(self, x):
        """Upon selection of a Transformation in the Transformation Library, initialize the Transformation Configuration
        interface
        """

        model = self.transformation_list.model()

        selected_transformation = TRANSFORMATIONS_BY_NAME[model.data(x)]
        print("Selected transformation: {}".format(selected_transformation))

        # Destroy existing form rows
        for i in reversed(range(self.config_form.count())):
            self.config_form.itemAt(i).widget().setParent(None)

        # Generate configuration for selected Transformation
        for option in selected_transformation.schema["options"]:

            label = QLabel(option["name"])
            label.setToolTip(option["description"])
            field = QTextEdit("Testing")

            self.config_form.addRow(label, field)
