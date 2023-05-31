from user import *;

class Team:
    def __init__(self,name) -> None:
        self.teamname = name
        self.teamroster = {}
        self.teamWins = 0
        self.teamLosses = 0
    
    def addmember(self, member):
        '''member should be of the user class'''
        if member.username not in self.teamroster:
            self.teamroster[member.username] = member
            return 1 #return 1 if success
        else:
            return 0 #failure
        
    def removemember(self, member):
        if member.username in self.teamroster:
            try:
                self.teamroster.pop(member.username)
                print("SUCCESS!")
            except:
                print("FAILURE")
        else:
            return 1 #for key not found
        
    def getmember(self,member):
        #member should be a string
        if member.username in self.teamroster:
            try:
                return self.teamroster[member]
            except:
                print("FAILURE")
        else:
            return 1 #for key not found
        
    def setname(self,name):
        self.teamname = name    
        
    def teamoutcome(self,outcome):
        #1 for win, 0 for loss
        if outcome == 1:
            for membername, member in self.teamroster.items():
                member.addWin(1)
                self.teamWins += 1
        elif outcome == 0:
            for membername, member in self.teamroster.items():
                member.addLoss(1)
                self.teamLosses += 1
        else:
            return 2 #error code
        
         
    def __str__(self) -> str:
        return (f'{self.teamname}:{self.teamroster.keys()}')
    
    def __contains__(self, string):
        if string in self.teamroster:
            return True
        else:
            return False
    