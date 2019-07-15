from polyrename.transformation.transformation import Transformation
from polyrename.transformation.utils.path_utils import insert_text_before_extension


class InsertTransformation(Transformation):
    schema = {
        'metadata': {
            'name': 'Insert',
            'description': 'Inserts text at specified location'
        },
        'options': [
            {
                'name': 'Text',
                'description': 'Text to insert',
                'datatype': str,
                'required': True
            },
            {
                'name': 'Position',
                'description': 'Position to insert text at',
                'datatype': int,
                'required': True
            }
        ]
    }

    def __init__(self, text, position):
        self.text = text
        self.position = position

    def resolve(self, file_sequence):
        return_sequence = []
        for file in file_sequence:

            if len(file.stem) < self.position:
                file = insert_text_before_extension(file, self.text)
            else:
                before = file.stem[0:self.position]
                after = file.stem[self.position:]
                file = file.parent / (before + self.text + after + file.suffix)

            return_sequence.append(file)

        return return_sequence

    def __repr__(self):
        return "InsertTransformation('{}', {})".format(self.text, self.position)
