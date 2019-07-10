#import taglib
import pytag

from polyrename.transformation.transformation import Transformation
from polyrename.transformation.utils.path_utils import insert_text_before_extension


class MusicTagsTransformation(Transformation):
    schema = {
        'metadata': {
            'name': 'Music Tags',
            'description': 'Append a formatted string that pulls data from music metadata'
        },
        'options': [
            {
                'name': 'Format String',
                'description': 'Format string for text to append',
                'datatype': str,
                'required': True
            }
        ]
    }

    format_map = {
        '%t': 'title',
        '%n': 'tracknumber',
        '%a': 'artist',
    }

    forbidden_characters = [
        r'<',
        r'>',
        r':',
        r'"',
        r'/',
        r'\\',
        r'|',
        r'?',
        r'*',
    ]

    def __init__(self, format_string):
        self.format_string = format_string

    def sanitize_tag(self, tag):
        for character in self.forbidden_characters:
            tag = tag.replace(character, '')

        tag = tag.replace('\x00', '')

        return tag

    def resolve(self, file_sequence):
        return_sequence = []

        for file in file_sequence:

            # Skip if not a supported music file
            try:
                music_file = pytag.Audio(str(file))
            except:
                return_sequence.append(file)
                continue

            formatted_string = self.format_string
            for formatter, replacement in self.format_map.items():

                try:
                    tag_value = music_file.get_tags()[replacement]
                except KeyError as e:
                    print(e)
                    formatted_string = formatted_string.replace(formatter, '')
                    continue

                tag_value = self.sanitize_tag(tag_value)

                formatted_string = formatted_string.replace(formatter, tag_value)

            return_sequence.append(insert_text_before_extension(file, formatted_string))

        return return_sequence
