from .child import ChildTransformation


class SequenceTransformation(ChildTransformation):
    def configure(self, initial=1, step=1, pad_character='0', pad_length=1):
        self.initial = initial
        self.step = step
        self.pad_character = pad_character
        self.pad_length = pad_length

    def resolve(self):
        sequence_length = len(self.file_sequence)

        sequence = []
        counter = self.initial
        for _ in range(sequence_length):
            sequence.append(str(counter).rjust(self.pad_length, self.pad_character))
            counter += self.step

        return sequence
