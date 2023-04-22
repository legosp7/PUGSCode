import pickle


def main():
    with open("users.rkb","rb") as opf:
        userdict = pickle.load(opf)
