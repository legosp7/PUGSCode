import pickle
from user import *
from team import *

userdict = {}
teamdict = {}

legosp7 = User("legosp7")
userdict[legosp7.username] = legosp7

TestTeam = Team("TestTeam")
TestTeam.addmember(legosp7)
TestTeam2 = Team("TestTeam2")
teamdict[TestTeam2.teamname] = TestTeam2

teamdict[TestTeam.teamname] = TestTeam

with open("users.rkb","wb") as opf:
            pickle.dump(userdict, opf)
with open("teams.rkb","wb") as ppf:
            pickle.dump(teamdict, ppf)
