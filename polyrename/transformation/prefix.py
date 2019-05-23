from polyrename.transformation.transformation import Transformation


class PrefixTransformation(Transformation):
    def get_schema(self):
        return {
            'metadata': {
                'name': 'Prefix',
                'description': 'Prepend text to filename'
            },
            'options': [{
                'name': 'text',
                'description': 'Text to prepend',
                'datatype': str,
                'required': True
            }]
        }

    def configure(self, text):
        self.text = text

    def resolve(self):
        for file in self.file_sequence:
            file = self.text + file

        return self.file_sequence
