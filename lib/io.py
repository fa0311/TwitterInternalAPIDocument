def write(path, data):
    with open(path, mode="w+") as f:
        f.write(data)


def read(path):
    with open(path, mode="r") as f:
        return f.read()
