def read_tokens(file_path):
    operators = []
    separators = []
    keywords = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

    spaces = 0
    for line in lines:
        line = line.replace("\n", "").strip()
        if line == "":
            spaces += 1
            continue
        if spaces == 0:
            operators.append(line)
        if spaces == 1:
            separators.append(line)
        if spaces == 2:
            keywords.append(line)
    return operators, separators, keywords


def read_program(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines
