from polyrename.transformation.transformation import Transformation
from polyrename.transformation.utils.path_utils import insert_text_before_extension


class SequenceTransformation(Transformation):
    schema = {
        'metadata': {
            'name': 'Sequence',
            'description': 'Append numeric sequence'
        },
        'options': [
            {
                'name': 'Start',
                'description': 'Initial value of sequence',
                'datatype': int,
                'required': True,
                'default_value': 1
            },
            {
                'name': 'Step',
                'description': 'Value to increment sequence by',
                'datatype': int,
                'required': True,
                'default_value': 1
            },
            {
                'name': 'Pad Character',
                'description': 'Character to pad sequence number by',
                'datatype': str,
                'required': True,
                'default_value': '0'
            },
            {
                'name': 'Pad length',
                'description': 'Number of characters to pad sequence to',
                'datatype': int,
                'required': True,
                'default_value': 1
            },
        ]
    }

    def __init__(self, file_sequence, start, step, pad_char, pad_len):
        super().__init__(file_sequence)
        self.start = start
        self.step = step
        self.pad_char = pad_char
        self.pad_len = pad_len

    def resolve(self):
        return_sequence = []
        sequence_value = self.start
        for file in self.file_sequence:
            file_path = insert_text_before_extension(file, str(sequence_value).rjust(self.pad_len, self.pad_char))
            return_sequence.append(file_path)

            sequence_value += self.step

        return return_sequence
