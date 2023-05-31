import pickle
from team import *

class User:
    '''
    class for users
    '''
    def __init__(self,username:str, team = None) -> None:
        self.username = username
        self.wins = 0
        self.losses = 0
        self.kills = 0
        self.deaths = 0
        self.assists = 0
        self.team = team
        
    def calcKDA(self):
        return (self.kills + self.assists)/self.deaths
    
    def WLRatio(self):
        return (self.wins/self.losses)
    
    def setname(self, name):
        self.username = name
    
    def addKills(self,killamt):
        self.kills += killamt
    
    def addDeaths(self,Deathamt):
        self.deaths += Deathamt
        
    def addassists(self,astamt):
        self.assists += astamt
        
    def addWin(self,Winamount):
        self.wins += Winamount

    def addLoss(self,lossamount):
        self.losses += lossamount
    
    def setTeam(self,teamtoset):
        #team is a team obj
        self.team = teamtoset
    
    
