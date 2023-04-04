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
          print(f"Other {self.period - len(self.checkoffList)} check marks left")
        else:
              print("No need to checkoff no more...")
              print("Exit...")
              return 
        if len(self.checkoffList) == self.period:# and datetime.date.today() == self.end
            self.completed = True
            self.count_of_completed_habit = self.checkoffList.count("y")
            self.longest_habit_streak = ans
            print(f"The daily habit of {self.name} was completed\
                  within the period of {self.start} to {self.end}")

                 
    
class HabitTracker:
    def __init__(self,user):
        self.user = user
        self.habits = []

    def search_by_id(self,target_id):
        l,r = 0,len(self.habits) - 1
        while l <= r:
            mid = (r+l)//2
            if target_id > self.habits[mid].id:
                l = mid + 1
            elif target_id < self.habits[mid].id:
                r = mid - 1
            else:
                return self.habits[mid].name 
    def search_by_name(self,name):
        res = None
        for index,habit in enumerate(self.habits):
            if name == habit.name:
                res = (habit.name,index,habit)
        if not bool(res):
            print("Habit not found")
        return res
    def addHabit(self,name,start,end,freq):
        if self.search_by_name(name):
            print("Already added! ")
        else:
            print(f"Adding {name}...")
            self.habits.append(Habit(name,start,end,freq))
        return 
    def modifyHabit(self,name,start=None,end=None,freq=None):
        """TO DO"""
        if not bool(start) and not bool(end) and bool(freq):
            print("Arguments all empty!")
            pass
        elif bool(start) and bool(end):
            pass
        elif bool(freq):
            pass
        return 
    def deleteHabit(self,name):
        if self.search_by_name(name):
            self.habits = [item for item in self.habits if item.name != name] +\
            [item for item in self.habits if item.name == name]
            self.habits.pop()
            return 
    def checkoff_by_name(self,name,check):
        (_,_,h) = self.search_by_name(name) 
        if h:
            h.checkoff(check)
            return 
        else:
            print("Not found...")



if __name__=='__main__':
 
   tracker = HabitTracker("John")
   tracker.addHabit("Brush your teeth","2023-03-01","2023-03-4","D")
   tracker.addHabit("Go to school","2023-03-02","2023-04-30","D")
   
   tracker.checkoff_by_name("Brush your teeth","y")
   help(tracker.modifyHabit)

  # tracker.habits[0].checkoff("y")
  # tracker.habits[0].checkoff("y")
  # tracker.habits[0].checkoff("y")

#    tracker.addHabit("Go to school","2023-03-02","2023-04-30","D")
#    tracker.addHabit("Study JavaScript","2023-03-02","2023-03-04","D")
#    tracker.addHabit("Study Python","2023-03-02","2023-03-04","D")
#    tracker.addHabit("Go to bed","2023-03-02","2023-03-04","D")
#    print("Before calling the delete method..")
#    for i in tracker.habits:
#        print(i.name)
   
   
#    tracker.deleteHabit("Go to school")
#    tracker.deleteHabit("Go to bed")
#    tracker.deleteHabit("Study JavaScript")
   
#    print("See what happened after calling the delete method..")
#    for i in tracker.habits:
#        print(i.name)
   
#    (a,b) = tracker.search_by_name("Brush your teeth")
#    tracker.addHabit("Go to the gym","2023-03-02","2023-03-04","D")
#    tracker.addHabit("Wash your clothes","2023-03-02","2023-03-04","D")
#    output = tracker.search_by_id(1)
 
#    tracker.deleteHabit("Brush your teeth")
#    tracker.deleteHabit("Study Python")
#    tracker.deleteHabit("Go to bed")

#    tracker.habits[0].checkoff('y')
#    tracker.habits[0].checkoff('y')
#    tracker.addHabit("Go to the gym","2023-03-02","2023-03-04","D")

#    print(tracker.search_by_id(32))