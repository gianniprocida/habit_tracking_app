import unittest
import pandas as pd
from habit_tracking_app import Habit,HabitTracker

class TestHabitTracker(unittest.TestCase):
    def setUp(self):

        self.objTracker = HabitTracker("John")
        self.objTracker.add_habit("Study SQL","2023-04-01","2023-04-22","W")
        self.objTracker.add_habit("Study Python","2023-04-01","2023-04-22","W")
        self.objTracker.add_habit("Study OOP","2023-05-01","2023-05-22","W")

    def test_get_habit_by_id(self):
        self.objTracker.add_habit("Study ML","2023-03-01","2023-03-4","D")

        self.assertEqual(self.objTracker.get_habit_by_id(1).name,"Study SQL")

        self.assertEqual(self.objTracker.get_habit_by_id(2).name,"Study Python")


        self.assertEqual(self.objTracker.get_habit_by_id(3).name,"Study OOP")

        self.assertEqual(self.objTracker.get_habit_by_id(4).name,"Study ML")

      
