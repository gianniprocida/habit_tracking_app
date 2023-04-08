from habit_tracking_app import Habit,HabitTracker
import sys

class Menu:
    """Display a menu and respond to choices when run."""
    def __init__(self):
        self.tracker = HabitTracker("gianni")
        self.choices = {
            "1":self.add,
            "2":self.show_by_name,
            "3":self.show}
        
    def display_menu(self):
        print(""""
        Notebook Menu
    1.Add habit""")
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
    def show(self,habit):
        if not habit:
            print("Habit not found")
        else:
            print("{0}: {1}\n{2}".format(habit.name, habit.start,habit.end))
    def add(self):
        val1,val2,val3,val4= input("Enter three values separated by space: ").split() 
        self.tracker.addHabit(val1,val2,val3,val4)
        print("Your habit has been added")
    def show_by_name(self):
        val = input("Enter a habit: ")
        habit = self.tracker.get_habit_by_name(val)
        self.show(habit)
    def show_by_id(self):
        val = int(input("Enter a habit id: "))
        habit = self.tracker.get_habit_by_id(val)
        self.show(habit)
    def show_habit_with_longest_run_streak_of_all(self):
        habit = self.tracker.longest_run_streak_of_all()
        self.show(habit)
        

if __name__=="__main__":
    Menu().run()