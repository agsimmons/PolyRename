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

    def __init__(self, match, replace):
        self.match = match
        self.replace = replace

    def resolve(self, file_sequence):
        return_sequence = []
        for file in file_sequence:

            file = file.parent / (file.stem.replace(self.match, self.replace) + file.suffix)

            return_sequence.append(file)

        return return_sequence

    def __repr__(self):
        return "ReplaceTransformation('{}'. '{}')".format(self.match, self.replace)
