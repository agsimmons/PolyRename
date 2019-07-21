class Transformation:

    schema = {}

    def __init__(self):
        raise NotImplementedError

    def resolve(self, file_sequence):
        raise NotImplementedError
