from polyrename.transformation.transformation import Transformation
from polyrename.transformation.utils.path_utils import insert_text_before_extension


class SuffixTransformation(Transformation):
    schema = {
        'metadata': {
            'name': 'Suffix',
            'description': 'Append text to filename'
        },
        'options': [
            {
                'name': 'Text',
                'description': 'Text to append',
                'datatype': str,
                'required': True
            }
        ]
    }

    def __init__(self, text):
        self.text = text

    def resolve(self, file_sequence):
        return_sequence = []
        for file in file_sequence:
            file_path = insert_text_before_extension(file, self.text)
            return_sequence.append(file_path)

        return return_sequence

    def __repr__(self):
        return "SuffixTransformation({})".format(self.text)
