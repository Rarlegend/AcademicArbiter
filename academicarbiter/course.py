class course:
    #scores are either 1 or -1, its just thumbs up or down
    #difficulty, teaching, subject matter
    dScore = 0
    tScore = 0
    sScore = 0
    name = ""
    
    
    def __init__ (self, name, dscore, 
                  tscore, sscore):
        self.name = name
        self.dScore = dscore
        self.tScore = tscore
        self.sScore = sscore
    
    def getName (self):
        return self.name
    def getT(self):
        return self.tScore
    def getD(self):
        return self.dScore
    def getS(self):
<<<<<<< HEAD
        return self.sScore

    
    
    
    
=======
        return self.sScore
>>>>>>> 801fc4a0213ac14bc11c04d12550341ad9a38a31
