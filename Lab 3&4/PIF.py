class PIF:
    def __init__(self) -> None:
        self.__content = []

    def add(self, token, index):
        self.__content.append((token, index))

    def __str__(self) -> str:
        result = ""
        for pair in self.__content:
            result += f"{pair[0]} -> {pair[1]}\n"
        if result == "":
            return "{}"
        return result