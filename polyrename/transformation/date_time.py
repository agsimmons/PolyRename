from .transformation import Transformation

import datetime


class DateTimeTransformation(Transformation):
    schema = {
        'metadata': {
            'name': 'Datetime',
            'description': 'Appends a formatted datetime object'
        },
        'options': [
            {
                'name': 'Year',
                'description': 'Date year',
                'datatype': int,
                'required': False,
                'default_value': 2000
            },
            {
                'name': 'Month',
                'description': 'Date month',
                'datatype': int,
                'required': False,
                'default_value': 1
            },
            {
                'name': 'Day',
                'description': 'Date day',
                'datatype': int,
                'required': False,
                'default_value': 1
            },
            {
                'name': 'Hour',
                'description': 'Time hour',
                'datatype': int,
                'required': False,
                'default_value': 0
            },
            {
                'name': 'Minute',
                'description': 'Time minute',
                'datatype': int,
                'required': False,
                'default_value': 0
            },
            {
                'name': 'Second',
                'description': 'Time second',
                'datatype': int,
                'required': False,
                'default_value': 0
            },
            {
                'name': 'Microsecond',
                'description': 'Time microsecond',
                'datatype': int,
                'required': False,
                'default_value': 0
            },
            {
                'name': 'Format String',
                'description': 'Format string for date (see https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior)',
                'datatype': str,
                'required': True
            }
        ]
    }

    def __init__(self, file_sequence, year, month, day, hour, minute, second, microsecond, format_string):
        super(DateTimeTransformation, self).__init__(file_sequence)
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond
        self.format_string = format_string

    def resolve(self):

        date_object = datetime.datetime(*(self.year, self.month, self.day, self.hour, self.minute, self.second, self.microsecond))

        return_sequence = []
        for file in self.file_sequence:
            file_name = file.stem + date_object.strftime(self.format_string) + file.suffix
            file_path = file.parent / file_name
            return_sequence.append(file_path)

        return return_sequence
