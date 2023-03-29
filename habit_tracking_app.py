import pandas as pd
import datetime

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
        self.completed_date = None
    def check_off(self,completed):
        ans = 0
        if len(self.checkoffList) >= self.period:
            print("Done")
            self.last_completed = datetime.date.today()
            return 
        if completed == "y":
            self.checkoffList.append("y")
        elif completed =="n":
            self.checkoffList.append("n")
        else:
            print("Invalid input")

        if len(self.checkoffList) > 2:
         ans = 1
         for i in range(len(self.checkoffList)):
            j = i + 1
            while j < len(self.checkoffList) and self.checkoffList[j] == self.checkoffList[i]:
                j+=1
            ans = max(ans,j-i)         
        return ans

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



h1 = Habit("Brush your teeth","2023-03-01","2023-03-30","D")
tracker = HabitTracker("John")
tracker.addHabit("Brush your teeth","2023-03-01","2023-03-30","D")
tracker.addHabit("Go to school","2023-03-02","2023-03-25","D")
a = tracker.search_by_name("Go to school")
a = tracker.search_by_name("Go to work")
print(tracker.habits)
