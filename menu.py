from habit_tracking_app import Habit,HabitTracker
import sys,json
import datetime

class Menu:
    """Display a menu and respond to choices when run."""
    def __init__(self,user_name):
        self.tracker = HabitTracker(user_name)
        self.choices = {
            "1":self.add,
            "2":self.show_all_habits_and_details,
            "3":self.show_by_name,
            "4":self.show_by_id,
            "5":self.checkoff,
            "6":self.show_habit_with_longest_run_streak_of_all,
            "7":self.show_habits_with_same_property,
            "8":self.show_barchart,
            "9":self.quit
            }
        
    def display_menu(self):
        print(""""
        Notebook Menu

    1. Add habit
    2. Show all habits and details
    3. Show habit by name
    4. Show habit by id
    5. Check off
    6. Show habit with longest run streak of all
    7. Show habits with the same property
    8. Show bar chart
    9. Quit
    
    """)
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            print(" ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")
    def show(self,habit):
        """
        Show habits
         
        Args:
        habit (obj) or (dict): If the habit parameter is a dictionary, it suggests that either
        the 'get_habit_with_longest_run_streak_of_all' or 'get_habits_with_same_property'
        function has been called. If 'habit' is not a dictionary, it suggests that 
        either 'get_habit_by_name' or 'get_habit_by_id' or 'data_visualization' has been invoked.
        
        """
        if not habit:
            print("Habit not found")
        # If "/" exisits in the keys of habit dictionary, it means that data_visualization was invoked
        elif isinstance(habit,dict) and "/" in "".join(habit.keys()):
            for key in habit:
                print("{0}: {1}".format(key,habit[key]))
                print(" ")
        elif isinstance(habit,dict) and isinstance(list(habit.values())[0],int):
            print("Longest run streak of all: {0}\nHabit:{1}".format(list(habit.values())[0],list(habit.keys())[0]))
            print(" ")
        elif isinstance(habit,dict) and isinstance(list(habit.values())[0],list):
            for key in habit:
                print("{0}: {1}".format(key,habit[key]))
                print(" ")
        else:
            print("{0}: {1}\n{2}\n{3}".format(habit.name, habit.start,habit.end,habit.completed))
            print(" ")
    def show_all_habits_and_details(self):
        """
        List all habits that are currently being tracked.
         
        
        """
        for habit in self.tracker.habits:
            print(" ")
            print("Habit:{0}\nStart:{1}\nEnd:{2}\nFreq:{3}\nCheckoffList:{4}\nCompleted:{5}\nLongest_streak:{6}\ncount_of_y:{7}".format(habit.name, habit.start,habit.end,habit.freq,\
                                                                                                                              habit.checkoffList,habit.completed,habit.longest_habit_streak,habit.count_of_yes))
            print(" ")
    def add(self):
        val1 = input("Enter the name of the habit you wish to add: ")
        
        #Check input data using a while loop until user enters correct data
        val2,val3,val4= input("Enter starting date, end date (in the format YYYY-MM-DD) and frequency (W or D) separated by spaces:").split()
        while True:
            try:
                datetime.datetime.strptime(val2,"%Y-%m-%d")
                break
            except ValueError:
                print("Starting date is not in the correct format")
                val2 = input("Enter starting date in the format YYYY-MM-DD.")
        print(f"You entered the date {val2}")
        while True:
            try:
                datetime.datetime.strptime(val3,"%Y-%m-%d")
                break
            except ValueError:
                print("End date is not in the correct format")
                val3 = input("Enter starting date in the format YYYY-MM-DD.")
        print(f"You entered the date {val3}")

        while True:
            try:
                if val4 in ["D","W"]:
                    break
                else:
                    raise ValueError
            except ValueError:
                 print(f"{val4} is neither D nor W") 
                 val4 = input("Enter a starting date")
        print(f"You entered {val4} frequency")   

        if val3 > val2: 
           self.tracker.add_habit(val1,val2,val3,val4)
           print("Your habit has been added")
        else:
            print("end date cannot be older than starting date")
        print(" ")
    def show_by_name(self):
        val = input("Enter a habit: ")
        habit = self.tracker.get_habit_by_name(val)
        self.show(habit)
    def show_by_id(self):
        val = int(input("Enter a habit id: "))
        habit = self.tracker.get_habit_by_id(val)
        self.show(habit)
    def checkoff(self):
        val1 = input("Enter the habit you completed:")
        
        #Check input data using a while loop until user enters correct data
        while True:
            habit = self.tracker.get_habit_by_name(val1)
            try:
                if habit:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Cannot checkoff a habit that does not exist")
                val1 = input("Enter the habit you completed: ")
        print(f"You entered {val1}")

        val2 = input("Enter 'y' or 'n' to indicate whether the task was completed today: ")
        
        while True:
            try:
                if val2 in ["y","n"]:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("f{val2} is neither y nor n}")
                val2 = input("Enter 'y' or 'n': ")
        print(f"You entered {val2}")
        print(" ")
        self.tracker.checkoff_by_name(val1,val2)
    def show_habit_with_longest_run_streak_of_all(self):
        habit = self.tracker.get_habit_with_longest_run_streak_of_all()
        self.show(habit)
    def delete(self):
        val = input("Enter the habit you wish to delete")
        self.tracker.delete_habit(val)
    def show_barchart(self):
        habit = self.tracker.data_visualization()
        self.show(habit)
    def show_habits_with_same_property(self):
        val = input("Enter the property (time_period_string or freq) by you wish to group your habits: ")
        while True:
            try:
                if val in ["time_period_string","freq"]:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("f{val} is neither time_period_string nor freq}")
                val = input("Enter 'y' or 'n': ")
        print(f"You entered {val}")
        habit = self.tracker.get_habits_with_same_property(val)
        self.show(habit)
    def quit(self):
        """

        Quits the execution an writes the instance of the class HabitTracker to a 
        JSON file.
        
        """

        print("Thank your for using our App today")
        d = self.tracker.to_dict()
        with open("mydata.json","w") as out:
            json.dump(d,out)
        sys.exit(0)
if __name__=="__main__":
    user_name = input("Enter your name: ")
    while not user_name.isalpha():
        print("Invalid input. Your name should only contain letters")
        user_name = input("Enter your name")
    Menu(user_name).run()


#Brush 2023-03-01 2023-03-03 D