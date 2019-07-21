from polyrename.transformation.transformation import Transformation


class RemoveRangeTransformation(Transformation):
    schema = {
        "metadata": {
            "name": "Remove Range",
            "description": "Removes range of text in file name",
        },
        "options": [
            {
                "name": "Start",
                "description": "Start position (inclusive)",
                "datatype": int,
                "required": True,
            },
            {
                "name": "Stop",
                "description": "Stop position (exclusive)",
                "datatype": int,
                "required": True,
            },
        ],
    }

    def __init__(self, start, stop):
        self.start = start if start >= 0 else 0
        self.stop = stop

    def resolve(self, file_sequence):
        return_sequence = []
        for file in file_sequence:

            # TODO: Make this clearer
            file_name_characters = [x for x in file.stem]
            for _ in range(self.stop - self.start):
                try:
                    del file_name_characters[self.start]
                except IndexError:
                    break

            file = file.parent / ("".join(file_name_characters) + file.suffix)

            return_sequence.append(file)

        return return_sequence

    def __repr__(self):
        return "RemoveRangeTransformation({}, {})".format(self.start, self.stop)
