import pandas as pd
import datetime
import sys
from typing import Union
# import matplotlib.pyplot as plt


class Habit:
    """
    Represents a Habit with a name,start,end, and freq

    Attributes:
        name (str): The name of the habit you wish to create.
        start (str): The date when the habit is planned to start.
        end (str): The date when the habit is planned to end.
        freq (str): The frequency with which the habit is planned to occur.

     Additional Attributes:
        completed (bool):default False, True if the habit is completed within the given period .
        checkoffList (lst): A list that contains "y" or "n" to indicate whether the habit was completed or not for a day.
        longest_habit_streak (int): The maximum number of times the habit was completed in a row.
        count_of_yes (int): The number of 'y' in the checkoffList 

     Methods:
    __init__(self, name: str,start:str,end:str,freq:str) -> None
        Initializes a Habit object with the given name, starting date,end date and frequency.
    """

    def __init__(self, habit, start, end, freq: Union["D", "W"]):

        self.time_period_string = f"{start}/{end}"
        self.habit = habit
        self.start = start
        self.end = end
        self.freq = freq
        self.creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.checkoffList = []
        self.completed = False
        self.longest_streak = 0
        self.y_count = 0
        self.n_count = 0
        self.days_until_start = len(pd.date_range(start=datetime.datetime.now().date(), end=datetime.datetime.strptime(self.start, '%Y-%m-%d').date(),
                                                  freq="D"))
        self.next = None

    def checkoff(self, check):
        """Perform operations on the attributes of the habit class.

        1)Adds "y" or "n" to the checkoffList attribute of the class.
        2)Keeps track of the number of times the habit was completed in a row (longest_habit_streak).
        3)Keeps track of the number of 'y' in the checkoffList (count_of_yes). 'y' means that the habit was completed in one of 
        the days of the listed day.
        4)Sets completed to True If the checkoffList property of the class has reached a length equal to the number of days in
        the given period.

        Args:
        check (Union["y", "n"]): The 'check' argument should be either "y" (yes) or "n" (no)
        indicating whether the habit has been completed or not.

        Returns:
        This function does not return anything

        Raises:
          Values error: If the 'check' argument is not "y" or "n".

        """
        start_date_object = datetime.datetime.strptime(
            self.start, '%Y-%m-%d').date()
        end_date_object = datetime.datetime.strptime(
            self.end, '%Y-%m-%d').date()
        length_of_period = len(pd.date_range(start=start_date_object, end=end_date_object, freq=self.freq)) if self.freq == "D" \
            else len(pd.date_range(start=start_date_object, end=end_date_object, freq=f"{self.freq}-" + start_date_object.strftime('%a').upper()))
        # length_of_period = len(pd.date_range(start=self.start, end=self.end, freq=self.freq))

        if self.completed:
            print("You've already completed this habit")
            return

        self.checkoffList.append(check)

        # Track the current streak of consecutive completions and update longest_streak accordingly.
        current_streak = 0
        self.y_count = 0
        self.n_count = 0
        for i in range(len(self.checkoffList)):
            if self.checkoffList[i] == "y":
                current_streak += 1
                self.longest_streak = max(self.longest_streak, current_streak)
                self.y_count += 1
            else:
                current_streak = 0
                self.n_count += 1

        # Set completed to True if the checkoffList property of the class has reached a
        # length equal to the number of days in the given period.
        if len(self.checkoffList) == length_of_period:
            self.completed = True

        remaining_checks = length_of_period - len(self.checkoffList)

        print(f"{remaining_checks} check marks left.")

        # If the habit is completed, print a congratulatory message and the longest streak achieved.
        if self.completed:
            print("Congratulations! You have completed this habit.")
            print(f"Longest streak: {self.longest_streak}")

    def to_dict(self):
        """

        Returns a dictionary representation of the Habit object.

        Returns:
        A dictionary containing the Habits object's data.
        """

        return {'name': self.name, 'time_period_string': self.time_period_string, 'checkoffList': self.checkoffList, 'completed': self.completed, 'count_of_yes': self.count_of_yes}

    def print_dates(self):
        """
        Prints the dates on which a habit needs to be completed. 

        Returns:
        This function does not return anything.

        """

        start_date_object = datetime.datetime.strptime(
            self.start, '%Y-%m-%d').date()
        end_date_object = datetime.datetime.strptime(
            self.end, '%Y-%m-%d').date()
        date_list = pd.date_range(start=start_date_object, end=end_date_object, freq=self.freq) if self.freq == "D" \
            else pd.date_range(start=start_date_object, end=end_date_object, freq=f"{self.freq}-" + start_date_object.strftime('%a').upper())
        df = pd.DataFrame(date_list, columns=["Date"])
        print(df)


class HabitTracker:
    """
    Represents a HabitTracker with a user name and list of habits.

    Attributes:
        user (str): The name of the user.
        head (Habit): The first habit in the linked list.
        tail (Habit): The last habit in the linked list.
        length (int): The number of habits in the tracker.


    Methods:
    __init__(self, user: str) -> None
        Initializes a HabitTracker object with the given user.
    """

    def __init__(self, user):
        self.user = user
        self.head = None
        self.tail = None
        self.length = 0

    def make_empty(self):
        """
        Empties the HabitTracker by setting head, tail, and length to None or 0.

        """
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, name, start, end, freq):
        """
        Adds a new habit to the end of the tracker.

        Args:
           name (str): The name of the habit.
           start (str): The start date of the habit.
           end (str): The end date of the habit.
           freq (str): The frequency of the habit.

        """
        new_habit = Habit(name, start, end, freq)
        if self.length == 0:
            self.head = new_habit
            self.tail = new_habit
            self.length += 1
        else:
            self.tail.next = new_habit
            self.tail = self.tail.next
            self.length += 1

    def print_habits(self):
        """
        Prints the details of each habit in the tracker, including the habit name and the number 
        of days until it starts.

        """
        tmp = self.head
        while tmp:
            print(tmp.habit)
            print(tmp.days_until_start)
            tmp = tmp.next

    def prepend_habit(self, name, start, end, freq):
        """Adds a habit to the Tracker object.

        Args:
        name (str): The name of the habit you wish to add.
        start (str): The date when the habit is planned to start.
        end (str): The date when the habit is planned to start.
        freq (str): The frequency with which the habit is planned to occur.

        Returns:
        This function does not return anything.    

        """
        new_habit = Habit(name, start, end, freq)
        if self.length == 0:
            self.head = new_habit
            self.tail = new_habit
        else:
            new_habit.next = self.head
            self.head = new_habit
        self.length += 1

    def add_habit(self, name, start, end, freq):
        """
        Adds a new habit to the tracker, ensuring it is inserted in chronological order.

        If the tracker is empty, the habit is prepended to the list.
        If the start date of the new habit is earlier than the start date of the first habit in the tracker and there is no conflict,
        the habit is prepended.
        If the start date of the new habit is later than the start date of the last habit in the tracker and there is no conflict,
        the habit is appended.
        Otherwise, the habit is inserted at the appropriate position to maintain chronological order..

        Args:
           name (str): The name of the habit.
           start (str): The start date of the habit.
           end (str): The end date of the habit.
           freq (str): The frequency of the habit.

        Returns:
           None 
        """
        new_habit = Habit(name, start, end, freq)
        if self.length == 0:
            self.prepend_habit(name, start, end, freq)
            return
        elif new_habit.days_until_start < self.head.days_until_start and no_conflict(self.head, new_habit):
            self.prepend_habit(name, start, end, freq)
            return
        elif new_habit.days_until_start > self.tail.days_until_start and no_conflict(self.head, new_habit):
            self.append(name, start, end, freq)
            return

        fast = self.head
        slow = self.head
        while fast.days_until_start < new_habit.days_until_start:
            slow = fast
            fast = fast.next
        slow.next = new_habit
        new_habit.next = fast
        self.length += 1
        return

    def get_habit_by_id(self, index):
        """
        Retrieves a habit from the tracker by its index.

        Args:
           index (int): The index of the habit to retrieve.

        Returns:
           Node: The habit node at the specified index, or None if index is out of range.
        """
        if index < 0 or index >= self.length:
            return None
        tmp = self.head
        for _ in range(index):
            tmp = tmp.next
        return tmp

    def get_habit_by_name(self, habit):

        tmp = self.head
        while tmp:
            if habit.lower() in tmp.habit.lower():
                return tmp
            tmp = tmp.next
        return None

    def pop_habit(self):
        """
        Removes the last habit from the tracker.

        Returns:
          The Habit object that was removed from the tracker.
          If the tracker is empty, returns None.
        """
        if self.length == 0:
            return None

        slow = None
        fast = self.head
        if self.length == 1:
            fast = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return fast

        while fast.next:
            slow = fast
            fast = fast.next
        self.tail = slow
        self.tail.next = None
        self.length -= 1
        return fast

    def pop_first(self):
        """
        Removes the first habit from the tracker.

        Returns:
          The Habit object that was removed from the tracker.
          If the tracker is empty, returns None.
        """
        if self.length == 0:
            return None
        tmp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            tmp.next = None
        self.length -= 1
        return tmp

    def insert_habit(self, index, name, start, end, freq):
        """
        Inserts a new habit into the tracker at the specified index while maintaining chronological order.

        Args:
           index (int): The index at which to insert the habit.
           name (str): The name of the habit.
           start (str): The start date of the habit.
           end (str): The end date of the habit.
           freq (str): The frequency of the habit.

        Returns:
           None 
        """
        new_habit = Habit(name, start, end, freq)
        if index < 0 or index > self.length:
            return None
        if index == 0:
            if new_habit.days_until_start < self.head.days_until_start:
                return self.prepend_habit(name, start, end, freq)
        if index == self.length:
            if new_habit.days_until_start < self.tail.days_until_start:
                return self.append(name, start, end, freq)

        tmp = self.get_habit_by_id(index - 1)

        if new_habit.days_until_start < tmp.next.days_until_start:
            new_habit.next = tmp.next
            tmp.next = new_habit
            self.length += 1
        else:
            print("Unable to insert habit. The habit's start date conflicts with the ordering of the existing habits")

    def checkoff_by_name(self, name, check: Union["y", "n"]):
        """

        Checks off a habit in the habit list with the given name

        Args:
        name (str): The name of the habit to check off.
        check  (Union["foo", "bar"]): The 'check' argument should be either "y" (yes) or "n" (no)
        indicating whether the habit has been completed or not.

        Returns:
        This function does not return anything.

        Raises:
          ValueError: If the 'check' argument is not "y" or "n". 

        Raises:
          ValueError: If the habit is not found.   
        """

        habit = self.get_habit_by_name(name)
        if not habit:
            raise TypeError("Cannot checkoff a habit that does not exist")
        if check not in {"y", "n"}:
            raise TypeError(f"Invalid argument {check}. Expected 'y' or 'n'")
        habit.checkoff(check)

    def reverse(self):
        pass

    def longest_run_streak_of_all(self):
        """
        Calculates the longest run streak of all habits in the tracker.

        Returns:
          A dictionary containing the name of the habit with the longest run streak and its corresponding streak length.
        """
        longest_run_streak_of_all = 0
        cur = 0
        tmp = self.head
        while tmp:
            cur = tmp.longest_streak
            longest_run_streak_of_all = max(longest_run_streak_of_all, cur)
            habit = tmp.habit
            tmp = tmp.next
        return {habit: longest_run_streak_of_all}


def no_conflict(habit1, habit2):
    if habit1.start <= habit2.end and habit2.start <= habit1.end:
        return False
    return True


if __name__ == '__main__':

    tracker = HabitTracker("John")

    tracker.add_habit("Study java", "2024-06-23", "2024-06-29", "D")

    tracker.add_habit("Study math", "2024-05-08", "2024-05-12", "D")

    tracker.add_habit("Study python", "2024-05-01", "2024-05-06", "D")
    tracker.add_habit("Study SQL", "2024-04-25", "2024-04-30", "D")

    tracker.add_habit("Study csharp", "2024-05-02", "2024-04-03", "D")

    tracker.print_habits()
    print(" ")
    tracker.checkoff_by_name("sql", "y")

   # tracker.checkoff_by_name("sql", "y")

    sql = tracker.get_habit_by_id(0)

    # print(tracker.length)

    # a1 = tracker.get_habit(0)
    # a2 = tracker.get_habit(1)

    # a3 = tracker.get_habit(2)

    # a4 = tracker.get_habit(3)

    # new = Habit("Study c","2024-06-23","2024-07-01","D")

    # tracker.add_habit("Study c", "2024-06-10", "2024-06-15", "D")

    # tracker.insert(1, "Study kafka", "2024-05-05", "2024-04-07", "D")

    # tracker.print_habits()

    # tracker.prepend_habit("Study SQL","2024-04-18","2024-04-22","D")
    # tracker.prepend_habit("Study Python","2024-04-23","2024-04-29","D")
    # tracker.prepend_habit("Study OOP","2024-05-01","2024-05-22","D")

    # # tracker.print_habits()

    # a = tracker.get_habit(0)

    # tracker.reverse()

    # myhabit = tracker.get_habit_by_name("Study Python")

    # print(myhabit.name)

    # tracker.checkoff_by_name("Study Python","n")
    # tracker.checkoff_by_name("Study Python","y")
    # tracker.checkoff_by_name("Study Python","y")
    # tracker.checkoff_by_name("Study Python","y")

    # tracker.checkoff_by_name("Study SQL","n")
    # tracker.checkoff_by_name("Study SQL","n")
    # tracker.checkoff_by_name("Study SQL","y")
    # tracker.checkoff_by_name("Study SQL","y")

    # tracker.checkoff_by_name("Study OOP","n")
    # tracker.checkoff_by_name("Study OOP","n")
    # tracker.checkoff_by_name("Study OOP","y")
    # tracker.checkoff_by_name("Study OOP","n")

    # # Prints out {'Study Python':3}
    # print(tracker.get_habit_with_longest_run_streak_of_all())

    # # Prints out {'W':['Study SQL','Study Python','Study OOP']}
    # print(tracker.get_habits_with_same_property("freq"))

    # #{'2023-04-01-2023-04-22': ['Study SQL', 'Study Python'], '2023-05-01-2023-05-22': ['Study OOP']}
    # print(tracker.get_habits_with_same_property("time_period_string"))
