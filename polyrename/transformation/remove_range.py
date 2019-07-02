from polyrename.transformation.transformation import Transformation


class RemoveRangeTransformation(Transformation):
    schema = {
        'metadata': {
            'name': 'Remove Range',
            'description': 'Removes range of text in file name'
        },
        'options': [
            {
                'name': 'Start',
                'description': 'Start position (inclusive)',
                'datatype': int,
                'required': True
            },
            {
                'name': 'Stop',
                'description': 'Stop position (exclusive)',
                'datatype': int,
                'required': True
            }
        ]
    }

    def __init__(self, file_sequence, start, stop):
        super().__init__(file_sequence)
        self.start = start if start >= 0 else 0
        self.stop = stop

    def resolve(self):
        return_sequence = []
        for file in self.file_sequence:

            # TODO: Make this clearer
            file_name_characters = [x for x in file.stem]
            for _ in range(self.stop - self.start):
                try:
                    del file_name_characters[self.start]
                except IndexError:
                    break

            file = file.parent / (''.join(file_name_characters) + file.suffix)

            return_sequence.append(file)

        return return_sequence
