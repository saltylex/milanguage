class ParserOutput:
    def __init__(self, configuration):
        self.configuration = configuration
        self.representation = self.build_string_of_productions()

    def save_to_file(self, file_path="representation.out"):
        with open(file_path, 'w') as f:
            f.write(self.representation)

    def build_string_of_productions(self):
        return ' '.join(symbol[0] for symbol in self.configuration.stack)
