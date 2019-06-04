from .transformation import Transformation

import datetime


class DateTransformation(Transformation):
    schema = {
        'metadata': {
            'name': 'Date',
            'description': 'TODO'
        },
        'options': [
            {
                'name': 'Year',
                'description': 'Date year',
                'datatype': int,
                'required': False
            },
            {
                'name': 'Month',
                'description': 'Date month',
                'datatype': int,
                'required': False
            },
            {
                'name': 'Day',
                'description': 'Date day',
                'datatype': int,
                'required': False
            },
            {
                'name': 'Format String',
                'description': 'Format string for date (see https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior)',
                'datatype': str,
                'required': True
            }
        ]
    }

    def __init__(self, file_sequence, year, month, day, format_string):
        super(DateTransformation, self).__init__(file_sequence)
        self.year = year
        self.month = month
        self.day = day
        self.format_string = format_string

    def resolve(self):

        date_object = datetime.datetime(*(self.year, self.month, self.day))

        return_sequence = []
        for file in self.file_sequence:
            file_name = file.stem + date_object.strftime(self.format_string) + file.suffix
            file_path = file.parent / file_name
            return_sequence.append(file_path)

        return return_sequence
