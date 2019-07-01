from polyrename.transformation.transformation import Transformation
from polyrename.transformation.utils.path_utils import insert_text_before_extension

import datetime


class ReplaceExtensionTransformation(Transformation):
    schema = {
        'metadata': {
            'name': 'Replace Extension',
            'description': 'Replaces file extension with specified extension'
        },
        'options': [
            {
                'name': 'Extension',
                'description': 'Extension to use in replacement',
                'datatype': str,
                'required': False,
                'default_value': ''
            }
        ]
    }

    def __init__(self, file_sequence, extension):
        super().__init__(file_sequence)
        self.extension = extension

    def resolve(self):
        return_sequence = []
        for file in self.file_sequence:
            file_path = file.parent / (file.stem + self.extension)
            return_sequence.append(file_path)

        return return_sequence
