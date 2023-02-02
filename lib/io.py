def write(path, data):
    with open(path, mode="w+", encoding="utf-8") as f:
        f.write(data)


def read(path):
    with open(path, mode="r", encoding="utf-8") as f:
        return f.read()
