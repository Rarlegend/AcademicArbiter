#defines the actual algorithm

import course
import student
import semester
import data

class algorithm:
    isemesters = []
    iconcentration = ""
    iyear = ""
    students = []
    courseRecs = dict()
    
    #initialize an instance of the class
    def __init__ (self, sem, conc, year, students):
        self.isemesters = sem
        self.iconcentration = conc
        self.iyear = year
        self.students = students
    
    #go through every student and assign values for each course
    def values(self):
        for x in self.students:
            curYear = x.year
            if curYear == self.year:
                curSemesters = x.semesters
                #curConc = x.concentration
                multiplier = 0
                semIndex = self.isemesters.length - 1
                
                #get all of the courses from you and from them
                mySem = self.isemesters[semIndex]
                theirSem = curSemesters[semIndex]
                myClasses = mySem.getCourses
                theirClasses = theirSem.getCourses
                
                #assign a weight for the other student's courses
                for i in myClasses:
                    for j in theirClasses:
                        if (i.getName == j.getName):
                            multiplier += 1
                theirClasses = curSemesters[semIndex + 1].getCourses
                
                #add their courses to a list of recs
                for course in theirClasses:
                    if course in self.courseRecs:
                        self.courseRecs[course] += multiplier
                    else:
                        self.courseRecs.update({course, multiplier})  
                
                #remove the courses if they have already taken
                for x in self.courseRecs:  
                    for y in myClasses:
                        if x == y:
                            del self.courseRecs[x]
                                          
                #create a new sorted dictionary based on weights
                allRecs = dict()
                for x in (self.courseRecs.iterkeys()):
                    key = self.courseRecs[x]
                    if key in allRecs.keys(): 
                        allRecs[key].append(x)
                    allRecs[key] = x
                 
        return allRecs
                        
                        
                    
                
            