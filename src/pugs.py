import pickle
from user import *
from team import *
from game import *


class Pugs:
    def __init__(self) -> None:
        with open("users.rkb","rb") as opf:
            self.userdict = pickle.load(opf)
        with open("teams.rkb","rb") as teams:
            self.teamdict = pickle.load(teams)
        self.gameinstance = None

    def newUser(self, name, team):
        if name not in self.userdict:
            newUser = User(name, team)
            self.userdict[name] = newUser
            return 1
        else:
            return 0 #return 0 if unsuccessful
        
    def newTeam(self, teamname):
        if teamname not in self.teamdict:
            newTeam = Team(teamname)
            self.userdict[teamname] = newTeam
            return 1
        else:
            return 0 #return 0 if unsuccessful
        
    def addUsertoTeam(self,user:User,team:Team):
        if user.username in self.userdict and team.teamname in self.teamdict:
            team.addmember(user)
            user.setTeam(team)
    
    def newGame(self, name, map, team1, team2):
        self.gameinstance = Game(name,map, team1, team2)
    