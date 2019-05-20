from .child import ChildTransformation


class TextTransformation(ChildTransformation):
    def configure(self, text):
        self.text = text

    def resolve(self):
        return self.text
