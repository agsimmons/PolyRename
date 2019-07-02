from polyrename.transformation.transformation import Transformation


class ReplaceTransformation(Transformation):
    schema = {
        'metadata': {
            'name': 'Replace',
            'description': 'Replace text'
        },
        'options': [
            {
                'name': 'Match Text',
                'description': 'Text to match',
                'datatype': str,
                'required': True
            },
            {
                'name': 'Replace',
                'description': 'Text to replace match with',
                'datatype': str,
                'required': False,
                'default_value': ''
            }
        ]
    }

    def __init__(self, file_sequence, match, replace):
        super().__init__(file_sequence)
        self.match = match
        self.replace = replace

    def resolve(self):
        return_sequence = []
        for file in self.file_sequence:

            file = file.parent / (file.stem.replace(self.match, self.replace) + file.suffix)

            return_sequence.append(file)

        return return_sequence
