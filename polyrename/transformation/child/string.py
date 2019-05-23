from polyrename.transformation.transformation import Transformation


class StringTransformation(Transformation):
    def configure(self, text):
        self.text = text

    def resolve(self):
        return self.text
