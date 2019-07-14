from PySide2.QtWidgets import QAbstractItemView


class Pipeline(QAbstractItemView):
    def __init__(self):
        super().__init__()

        self.transformations = []

    def add_transformation(self, transformation):
        self.transformations.append(transformation)

    def remove_transformation(self, index):
        del self.transformations[index]

    def move_transformation_up(self, index):
        if index > 0:
            temp = self.transformations[index]
            self.transformations[index] = self.transformations[index - 1]
            self.transformations[index - 1] = temp

    def move_transformation_down(self, index):
        if index < len(self.transformations) - 1:
            temp = self.transformations[index]
            self.transformations[index] = self.transformations[index + 1]
            self.transformations[index + 1] = temp

    def resolve(self, file_sequence):
        for transformation in self.transformations:
            file_sequence = transformation.resolve(file_sequence)

        return file_sequence

    def __str__(self):
        return 'Pipeline({})'.format(self.transformations)
