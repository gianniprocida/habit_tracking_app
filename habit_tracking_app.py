import pandas as pd
import datetime
import sys
from typing import Union
# So that the index will start from 1
last_id = 0
class Habit:
    """
    Represents a Habit with a name,start,end,freq

    Attributes:
        name (str): The name of the habit you wish to create.
        start (str): The date when the habit is planned to start.
        end (str): The date when the habit is planned to start.
        freq (str): The frequency with which the habit is planned to occur.

     Methods:
    __init__(self, name: str,start:str,end:str,freq:str) -> None
        Initializes a Habit object with the given name, starting date,end date and frequency.
    """
     
    def __init__(self,name,start,end,freq:Union["D","W"]):
        if not isinstance(name,str):
            raise TypeError(f"{name} must be a string")
        if not isinstance(start,str):
            raise TypeError(f"{start} must be a string")
            # convert the date string to a date object
        date_object = datetime.datetime.strptime(start, '%Y-%m-%d').date()
        start = date_object.strftime('%Y-%m-%d')
        if not isinstance(end,str):
            raise TypeError("end must be a string")
        date_object = datetime.datetime.strptime(end, '%Y-%m-%d').date()
        end = date_object.strftime('%Y-%m-%d')

        if freq not in ["D","W"]:
            raise ValueError(f"Invalid argument {freq}. Expected 'D' or 'W'.")

        self.time_period_string = f"{start}-{end}"
        self.name = name
        self.start = start
        self.end = end
        self.freq = freq
        self.checkoffList = []
        global last_id
        last_id+=1
        self.id = last_id
        self.creation_date = datetime.date.today()   
        self.completed = False
        self.longest_habit_streak = None
        self.count_of_completed_habit = None

    def checkoff(self,check: Union["y","n"]):
        """Perform operations on the properties of the habit class.
        Adds "y" or "n" to the checkoffList property of the class, 
        Keeps track of the number of consecutive 'y' in the checkoffList (longest_habit_streak)
        Keeps track of the number of 'y' in the checkoffList (count_of_completed_habit)
        Sets completed to True If the checkoffList property of the class has reached a length equal to the given period.

        Args:
        check (Union["foo", "bar"]): The 'check' argument should be either "y" (yes) or "n" (no)
        indicating whether the habit has been completed or not.
        
        Returns:
        This function does not return anything

        Raises:
          Values error: If the 'check' argument is not "y" or "n".

        """


        length_of_period = len(pd.date_range(start=self.start, end=self.end, freq=self.freq))
        ans = 0
        if not self.completed:
          if check == "y":
             self.checkoffList.append("y")
          elif check =="n":
             self.checkoffList.append("n")
          else:
             raise ValueError(f"Invalid argument {check}. Expected 'y' or 'n'.")
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
    """
    Represents a HabitTracker with a user name and list of habits.

    Attributes:
        user (str): The name of the user
        habits (lst): List of habits to be processed 

    Methods:
    __init__(self, user: str) -> None
        Initializes a HabitTracker object with the given user.
    """
     
    def __init__(self,user):
        self.user = user
        self.habits = []

    def add_habit(self,name,start,end,freq):
        """Adds a habit to the Tracker object.

        Args:
        name (str): The name of the habit you wish to add.
        start (str): The date when the habit is planned to start.
        end (str): The date when the habit is planned to start.
        freq (str): The frequency with which the habit is planned to occur.
        
        Returns:
        This function does not return anything

        Raises:
          Habit already added: If the habit name was already added.

        """
        if self.get_habit_by_name(name):
            raise Exception("Habit already added!")
        print(f"Adding {name}...")
        self.habits.append(Habit(name,start,end,freq)) 
    
    def get_habit_by_id(self,habit_id):
        """

        Returns the Habit object and its name with th
         given ID.

        Args:
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

        Delete the Habit object with the given name.

        Args:
        name (int): The name of the Habit you wish to delete.
        
        Returns:
        This function does not return anything
        """
        if not self.get_habit_by_name(name):
            raise Exception(f"Error: the habit {name} is not in the HabitTracker!")
        self.habits = [item for item in self.habits if item.name != name] +\
        [item for item in self.habits if item.name == name]
        self.habits.pop()
    def checkoff_by_name(self,name,check: Union["y","n"]):
        """
        
        Checks off a habit in the habit list with the given name
        
        Args:
        name (str): The name of the habit to check off.
        check  (Union["foo", "bar"]): The 'check' argument should be either "y" (yes) or "n" (no)
        indicating whether the habit has been completed or not.
        
        Returns:
        This function does not return anything.

        Raises:
          Habit not found: If the habit name is not found in the habits list.
        
        Raises:
          ValueError: If the 'check' argument is not "y" or "n". 
        """

        habit = self.get_habit_by_name(name) 
        if not self.get_habit_by_name(name):
            raise Exception("Habit not found")
        if check not in ["y","n"]:
            raise ValueError(f"Invalid argument {check}. Expected 'y' or 'n'.")
        habit.checkoff(check)
    def get_habits_with_same_property(self,myprop:Union["time_period_string","freq"]):
        """Group habits by property
        
        Returns a dictionary with property key and lists of the name of the habit objects that share 
        the same property key.
         
        Args:
        myprop (str): The name of the property by which you wish to group 
        your habits.  The myprop argument should be either "time_period_string" or "freq". 
        
        Returns:
        Dict[str, List[name]]: A dictionary with subject keys and lists of the name habit objects.


        Raises:
          Habit not found: If the habit name is not found in the habits list.
        
        """
        
        if myprop not in ["time_period_string","freq"]:
            raise ValueError(f"Invalid argument {myprop}. Expected 'time_period_string' or 'freq'.")
        res = {}
        for habit in self.habits:
            mykey = getattr(habit,myprop)
            if mykey not in res:
                res[mykey] = [habit.name]
            else:
                res[mykey].append(habit.name)
        return res
    def get_habit_with_longest_run_streak_of_all(self):
        """
        
        Returns a dictionary with the key as the habit name and value as the longest run streak 
        of all habits.
         
    
        Returns:
        Dict[str, int]: A dictionary with the key as the habit name and value as the longest run streak 
        of all habits.

        """
        longest_run_streak_of_all = float('-inf')
        for habit in self.habits:
            if habit.completed:
                if habit.longest_habit_streak > longest_run_streak_of_all:
                    longest_run_streak_of_all = habit.longest_habit_streak
                    name = habit.name
        return {name:longest_run_streak_of_all}


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
   out = tracker.get_habit_with_longest_run_streak_of_all()
   o = tracker.get_habits_with_same_property("time_period_string")
#    d = {}
#    for i in tracker.habits:
#        mykey = getattr(i,"time_period_string")
#        if mykey in d:
#            d[mykey].append(i)
#        else:
#            d[mykey] = [i]
   print("Longest run: {0}\nHabit:{1}".format(list(out.keys())[0],list(out.values())[0]))
#    print(d)
#    a = tracker.longest_run_streak_of_all()
#    print(a)
     
#    tracker.deleteHabit("Go to school")
#    tracker.deleteHabit("Go to bed")
#    tracker.deleteHabit("Study JavaScript")