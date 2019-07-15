from polyrename.transformation.transformation import Transformation
from polyrename.transformation.utils.path_utils import insert_text_before_extension

import datetime


class CurrentDateTimeTransformation(Transformation):
    schema = {
        'metadata': {
            'name': 'Current Datetime',
            'description': 'Appends the current datetime accourding to a format string'
        },
        'options': [
            {
                'name': 'Format String',
                'description': 'Format string for datetime (see https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior)',
                'datatype': str,
                'required': True
            }
        ]
    }

    def __init__(self, format_string):
        self.format_string = format_string

    def resolve(self, file_sequence):
        datetime_object = datetime.datetime.now()
        resolved_datetime_string = datetime_object.strftime(self.format_string)

        return_sequence = []
        for file in file_sequence:
            file_path = insert_text_before_extension(file, resolved_datetime_string)
            return_sequence.append(file_path)

        return return_sequence

    def __repr__(self):
        return "CurrentDateTimeTransformation('{}')".format(self.format_string)
