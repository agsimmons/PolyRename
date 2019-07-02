import re

from polyrename.transformation.transformation import Transformation


class RegexReplaceTransformation(Transformation):
    schema = {
        'metadata': {
            'name': 'Regex Replace',
            'description': 'Replace text using a regex match'
        },
        'options': [
            {
                'name': 'Match Pattern',
                'description': 'Regex pattern to match',
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

            file = file.parent / (re.sub(self.match, self.replace, file.stem) + file.suffix)

            return_sequence.append(file)

        return return_sequence
