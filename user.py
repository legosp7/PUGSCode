import pickle

class User:
    '''
    class for users
    '''
    def __init__(self,username) -> None:
        self.username = username
        self.wins = 0
        self.losses = 0
        self.kills = 0
        self.deaths = 0
        self.assists = 0
    def calcKDA(self):
        return (self.kills + self.assists)/self.deaths
    def WLRatio(self):
        return (self.wins/self.losses)
    
