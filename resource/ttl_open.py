import os


def load():
    file_list = []
    for filename in os.listdir("./"):
        if filename.endswith(".ttl"):
            file_list.append(os.path.abspath(filename))
