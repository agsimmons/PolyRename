from PySide2.QtWidgets import (
    QGroupBox,
    QVBoxLayout,
    QListView,
    QAbstractItemView,
)
from PySide2.QtGui import QStandardItemModel, QStandardItem

from polyrename.transformation import TRANSFORMATIONS, TRANSFORMATIONS_BY_NAME


class TransformationLibrary(QGroupBox):
    def __init__(self, transformation_confirmation):
        super().__init__("Transformation Library")

        self.transformation_configuration = transformation_confirmation

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
        """Resolve selected transformation and pass it to transformation_configuration to display config"""

        model = self.transformation_list.model()
        selected_transformation = TRANSFORMATIONS_BY_NAME[model.data(x)]
        print("Selected transformation: {}".format(selected_transformation))

        self.transformation_configuration.swap_configuration(selected_transformation)
