from mediafile import FileTypeError, MediaFile, UnreadableFileError

from polyrename.transformation.transformation import Transformation
from polyrename.transformation.utils.path_utils import insert_text_before_extension


class MusicTagsTransformation(Transformation):
    schema = {
        "metadata": {
            "name": "Music Tags",
            "description": "Append a formatted string that pulls data from music metadata",
        },
        "options": [
            {
                "name": "Format String",
                "description": "Format string for text to append",
                "datatype": str,
                "required": True,
            }
        ],
    }

    format_map = {"%t": "title", "%n": "track", "%a": "artist"}

    forbidden_characters = [r"<", r">", r":", r'"', r"/", r"\\", r"|", r"?", r"*"]

    def __init__(self, format_string):
        self.format_string = format_string

    def sanitize_tag(self, tag):
        for character in self.forbidden_characters:
            tag = tag.replace(character, "")

        return tag

    def resolve(self, file_sequence):
        return_sequence = []

        for file in file_sequence:

            # Skip if not a supported music file
            try:
                music_file = MediaFile(file)
            except (FileTypeError, UnreadableFileError) as e:
                return_sequence.append(file)
                continue

            # Resolve format string
            formatted_string = self.format_string
            for formatter, replacement in self.format_map.items():

                # Get required tag, and skip if not found
                try:
                    tag_value = getattr(music_file, replacement)
                except KeyError:
                    formatted_string = formatted_string.replace(formatter, "")
                    continue

                tag_value = self.sanitize_tag(str(tag_value))

                formatted_string = formatted_string.replace(formatter, tag_value)

            return_sequence.append(insert_text_before_extension(file, formatted_string))

        return return_sequence

    def __repr__(self):
        return f"MusicTagsTransformation('{self.format_string}')"
