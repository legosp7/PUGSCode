import pickle

with open("users.rkb","rb") as opf:
    userdict = pickle.load(opf)

class Game:
    def __init__(self, num, map) -> None:
        self.gamenum = num
        self.team1players = []
        self.team2players = []
        self.map = map
        
