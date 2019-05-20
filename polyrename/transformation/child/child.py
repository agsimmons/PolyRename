class ChildTransformation:
    def __init__(self, file_sequence):
        self.file_sequence = file_sequence

    def resolve(self):
        raise NotImplementedError
