from polyrename.transformation.transformation import Transformation


class StringTransformation(Transformation):
    def configure(self, string):
        self.string = string

    def resolve(self):
        return self.string
