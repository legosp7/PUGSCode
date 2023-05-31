from team import *
from user import *

class Game:
    def __init__(self, name, map, team1 = None, team2 = None) -> None:
        self.gamename = name
        self.team1players = []
        self.team2players = []
        if team1 is not None:
            self.loadteam1players(team1)
        if team2 is not None:
            self.loadteam2players(team2)
        self.map = map
    
    def loadteam1players(self,team1:Team):
        for member in team1.teamroster:
            if len(self.team1players) < 5:
                self.team1players.append(member)

    def loadteam2players(self,team2:Team):
        for member in team2.teamroster:
            if len(self.team2players) < 5:
                self.team2players.append(member)
    
    def addteam1member(self,user:User):
        if len(self.team1players) < 5:
            self.team1players.append(user)
        else:
            return 1 #error
    
    def addteam2member(self,user:User):
        if len(self.team2players) < 5:
            self.team2players.append(user)
        else:
            return 1 #error
    
    def changeT1Player(self,pos:int,user:User):
        try:
            self.team1players[pos] = user
        except:
            return 1
    
    def changeT2Player(self,pos:int,user:User):
        try:
            self.team1players[pos] = user
        except:
            return 1
    
    def t1Win(self):
        for user in self.team1players:
            user.addWin(1)
        for luser in self.team2players:
            luser.addLoss(1)
    
    def t1Win(self):
        for user in self.team2players:
            user.addWin(1)
        for luser in self.team1players:
            luser.addLoss(1)
        
        
        
            
    
