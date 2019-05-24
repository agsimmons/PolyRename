from .transformation import Transformation


class SuffixTransformation(Transformation):
    schema = {
        'metadata': {
            'name': 'Suffix',
            'description': 'Append text to filename'
        },
        'options': [{
            'name': 'Text',
            'description': 'Text to append',
            'datatype': str,
            'required': True
        }]
    }

    def __init__(self, file_sequence, text):
        super(SuffixTransformation, self).__init__(file_sequence)
        self.text = text

    # TODO: Don't put suffix after extension
    def resolve(self):
        return_sequence = []
        for file in self.file_sequence:
            file_name = file.name + self.text
            file_path = file.parent / file_name
            return_sequence.append(file_path)

        return return_sequence
