from polyrename.transformation.transformation import Transformation


class PrefixTransformation(Transformation):
    schema = {
        "metadata": {"name": "Prefix", "description": "Prepend text to filename"},
        "options": [
            {
                "name": "Text",
                "description": "Text to prepend",
                "datatype": str,
                "required": True,
            }
        ],
    }

    def __init__(self, text):
        self.text = text

    def resolve(self, file_sequence):
        return_sequence = []
        for file in file_sequence:
            file_name = self.text + file.name
            file_path = file.parent / file_name
            return_sequence.append(file_path)

        return return_sequence

    def __repr__(self):
        return f"PrefixTransformation('{self.text}')"
