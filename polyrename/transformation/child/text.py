from .child import ChildTransformation


class TextTransformation(ChildTransformation):
    def __init__(self, text):
        self.text = text

    def resolve(self):
        return self.text
