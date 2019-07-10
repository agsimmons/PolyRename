class Pipeline:
    def __init__(self, transformations):
        self.transformations = transformations

    def resolve(self, file_sequence):
        for transformation in self.transformations:
            file_sequence = transformation.resolve(file_sequence)

        return file_sequence
