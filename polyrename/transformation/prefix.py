from polyrename.transformation.transformation import Transformation


class PrefixTransformation(Transformation):
    schema = {
        'metadata': {
            'name': 'Prefix',
            'description': 'Prepend text to filename'
        },
        'options': [
            {
                'name': 'Text',
                'description': 'Text to prepend',
                'datatype': str,
                'required': True
            }
        ]
    }

    def __init__(self, file_sequence, text):
        super().__init__(file_sequence)
        self.text = text

    def resolve(self):
        return_sequence = []
        for file in self.file_sequence:
            file_name = self.text + file.name
            file_path = file.parent / file_name
            return_sequence.append(file_path)

        return return_sequence
