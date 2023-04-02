import pandas as pd
import datetime
import sys

last_id = 0
class Habit:
    def __init__(self,name,start,end,freq):
        # check arguments passed in the constructor
        self.name = name
        self.start = start
        self.end = end
        self.freq = freq
        self.period = len(pd.date_range(start=self.start, end=self.end, freq=self.freq))
        self.checkoffList = []
        global last_id
        last_id+=1
        self.id = last_id
        self.creation_date = datetime.date.today()
        self.completed = False
        self.longest_habit_streak = None
        self.count_of_completed_habit = None
    def checkoff(self,check):
        ans = 0
        if not self.completed:
          if check == "y":
             self.checkoffList.append("y")
          elif check =="n":
             self.checkoffList.append("n")
          else:
             raise TypeError("Invalid input")
          if len(self.checkoffList) > 1 and "y" in self.checkoffList:
              ans = 1
              for i in range(len(self.checkoffList)):
                  j = i + 1
                  while j < len(self.checkoffList) and self.checkoffList[j] == self.checkoffList[i]=="y":
                    j+=1
                  ans = max(ans,j-i)  
        else:
              print("No need to checkoff no more...")
              print("Exit...")
              return 
        if len(self.checkoffList) == self.period:# and datetime.date.today() == self.end
            self.completed = True
            self.count_of_completed_habit = self.checkoffList.count("y")
            self.longest_habit_streak = ans

                 
    
class HabitTracker:
    def __init__(self,user):
        self.user = user
        self.habits = []
    def search_by_id(self,id):
        # It'll be faster searching an habit by id
        pass
    def search_by_name(self,name):
        res = None
        for index,habit in enumerate(self.habits):
            if name == habit.name:
                res = (habit.name,index)
        if not bool(res):
            print("Habit not found")
        return res
    def addHabit(self,name,start,end,freq):
        if self.search_by_name(name):
            print("Already added! ")
        else:
            print("Adding your habit..")
            self.habits.append(Habit(name,start,end,freq))
        return 
    def modifyHabit(self,name,start=None,end=None,freq=None):
        if not bool(start) and not bool(end) and bool(freq):
            print("Arguments all empty!")
            pass
        elif bool(start) and bool(end):
            pass
        elif bool(freq):
            pass
        return 
    



tracker = HabitTracker("John")
tracker.addHabit("Brush your teeth","2023-03-01","2023-03-4","D")
tracker.addHabit("Go to school","2023-03-02","2023-03-06","D")
tracker.habits[0].checkoff('y')
tracker.habits[0].checkoff('y')
tracker.habits[0].checkoff('n')
tracker.habits[0].checkoff('y')
print(tracker.habits[0].longest_habit_streak)





