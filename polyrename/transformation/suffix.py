from polyrename.transformation.transformation import Transformation


class SuffixTransformation(Transformation):
    def get_schema(self):
        return {
            'metadata': {
                'name': 'Suffix',
                'description': 'Append text to filename'
            },
            'options': [{
                'name': 'text',
                'description': 'Text to append',
                'datatype': str,
                'required': True
            }]
        }

    def configure(self, text):
        self.text = text

    def resolve(self):
        for file in self.file_sequence:
            file = file + self.text

        return self.file_sequence
