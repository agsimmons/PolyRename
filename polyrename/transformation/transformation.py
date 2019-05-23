class Transformation:
    def __init__(self, file_sequence):
        self.file_sequence = file_sequence

    @property
    def schema(self):
        raise NotImplementedError

    def configure(self):
        raise NotImplementedError

    def resolve(self):
        raise NotImplementedError
