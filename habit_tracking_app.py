import pandas as pd
import datetime
import sys
# So that the index will start from 1
last_id = 0
class Habit:
    def __init__(self,name,start,end,freq):
        # check arguments passed in the constructor
        if not isinstance(start,str):
            raise TypeError("start must be a string")
            # convert the date string to a date object
        date_object = datetime.datetime.strptime(start, '%Y-%m-%d').date()
        start = date_object.strftime('%Y-%m-%d')
        if not isinstance(end,str):
            raise TypeError("end must be a string")
        date_object = datetime.datetime.strptime(end, '%Y-%m-%d').date()
        end = date_object.strftime('%Y-%m-%d')
        self.time_period_string = f"{start}-{end}"
        self.name = name
        self.start = start
        self.end = end
        self.freq = freq
     #   self.period = len(pd.date_range(start=self.start, end=self.end, freq=self.freq))
        self.checkoffList = []
        global last_id
        last_id+=1
        self.id = last_id
        self.creation_date = datetime.date.today()
      
        self.completed = False
        self.longest_habit_streak = None
        self.count_of_completed_habit = None

    def checkoff(self,check):
        length_of_period = len(pd.date_range(start=self.start, end=self.end, freq=self.freq))
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
          print(f"Other {length_of_period - len(self.checkoffList)} check marks left")
        else:
              print("No need to checkoff no more...")
              print("Exit...")
              return 
        if len(self.checkoffList) == length_of_period:# and datetime.date.today() == self.end
            self.completed = True
            self.count_of_completed_habit = self.checkoffList.count("y")
            self.longest_habit_streak = ans
            print(f"The daily habit of {self.name} was completed within the period of {self.start} to {self.end}")

                 
    
class HabitTracker:
    def __init__(self,user):
        self.user = user
        self.habits = []

    def add_habit(self,name,start,end,freq):
        """Adds a habit to the Tracker object.

        Parameters:
        name (str): The name of the habit you wish to add.
        start (str): The date when the habit is planned to start.
        end (str): The date when the habit is planned to start.
        freq (str): The frequency with which the habit is planned to occur.
        
        Returns:
        None

        """
        if self.get_habit_by_name(name):
            raise Exception("Habit already added!")
        print(f"Adding {name}...")
        self.habits.append(Habit(name,start,end,freq))
        return 
    
    def get_habit_by_id(self,habit_id):
        """

        Returns the Habit object and its name with the given ID.

        Parameters:
        habit_id (int): The unique identifier of the habit to retrieve.
        
        Returns:
        Habit: The Habit object with the given ID.
        """
        l,r = 0,len(self.habits) - 1
        while l <= r:
            mid = (r+l)//2
            if habit_id > self.habits[mid].id:
                l = mid + 1
            elif habit_id < self.habits[mid].id:
                r = mid - 1
            else:
                return self.habits[mid] 
    def get_habit_by_name(self,name):
        """

        Returns the Habit object with the given name.

        Parameters:
        name (int): The name of the Habit you wish to retrieve.
        
        Returns:
        Habit: The Habit object with the given name.
        """
        res = None
        for index,habit in enumerate(self.habits):
            if name == habit.name:
                res = habit
        return res
   
    def delete_habit(self,name):
        """

        Returns the Habit object with the given name.

        Parameters:
        name (int): The name of the Habit you wish to retrieve.
        
        Returns:
        Habit: The Habit object with the given name.
        """
        if self.get_habit_by_name(name):
            self.habits = [item for item in self.habits if item.name != name] +\
            [item for item in self.habits if item.name == name]
            self.habits.pop()
    def checkoff_by_name(self,name,check):
        habit = self.get_habit_by_name(name) 
        if not self.get_habit_by_name(name):
            raise Exception("Habit not found")
        habit.checkoff(check)
    def get_habits_with_same_periodicity(self):
        res = {}
        for habit in self.habits:
            mykey = getattr(habit,"time_period_string")
            if mykey not in res:
                res[mykey] = [habit]
            else:
                res[mykey].append(habit)
        return res
    def longest_run_streak_of_all(self):
        longest_run_streak_of_all = float('-inf')
        for habit in self.habits:
            if habit.completed:
                if habit.longest_habit_streak > longest_run_streak_of_all:
                    longest_run_streak_of_all = habit.longest_habit_streak
                    name = habit.name
        return {name:longest_run_streak_of_all}
    def show_all_habits(self):
        for habit in self.habits:
            print(habit.name)


if __name__=='__main__':
 
   tracker = HabitTracker("John")
   tracker.add_habit("Brush your teeth","2023-03-01","2023-03-4","D")
   tracker.add_habit("Go to school","2023-03-02","2023-03-05","D")
   
   tracker.habits[0].checkoff("y")
   tracker.habits[0].checkoff("y")
   tracker.habits[0].checkoff("n")
   tracker.habits[0].checkoff("y")
   print(tracker.habits[0].checkoffList)

   tracker.habits[1].checkoff("n")
   tracker.habits[1].checkoff("y")
   tracker.habits[1].checkoff("n")
   tracker.habits[1].checkoff("y")

   print(tracker.habits[1].checkoffList)
   print(tracker.habits[0].longest_habit_streak)
   print(tracker.habits[1].longest_habit_streak)
   print(tracker.get_habit_by_id(1).name)
   print(tracker.get_habit_by_id(2).name)
   r = tracker.get_habit_by_name("Brush your tth")

   tracker.add_habit("Study Python","2023-03-04","2023-03-10","D")

   tracker.add_habit("Study JavaScript","2023-03-04","2023-03-10","D")
   o = tracker.get_habits_with_same_periodicity()
   print(o)
#    d = {}
#    for i in tracker.habits:
#        mykey = getattr(i,"time_period_string")
#        if mykey in d:
#            d[mykey].append(i)
#        else:
#            d[mykey] = [i]

#    print(d)
#    a = tracker.longest_run_streak_of_all()
#    print(a)
     
   out = getattr(tracker,"user") 
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