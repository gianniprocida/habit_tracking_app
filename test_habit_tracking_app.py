import unittest
import pandas as pd
from habit_tracking_app import Habit,HabitTracker

class Test_Habit(unittest.TestCase):
    def setUp(self):
        self.obj1 = Habit("Brush your teeth","2023-03-01","2023-03-4","D")
        self.obj2 = Habit("Go to work","2023-03-10","2023-03-14","D")
        self.obj3 = Habit("Go to the gym","2023-03-10","2023-03-13","D")
    def tearDown(self):
        self.obj1 = None
        self.obj2 = None
    
    def test_checkoff(self):
        self.obj1.checkoff('y')
        self.obj1.checkoff('y')
        self.obj1.checkoff('n')
        self.obj1.checkoff('y')

        streak = self.obj1.longest_habit_streak
        self.assertEqual(streak,2)

        self.obj2.checkoff('y')
        self.obj2.checkoff('n')
        self.obj2.checkoff('y')
        self.obj2.checkoff('n')
        self.obj2.checkoff('y')
        streak = self.obj2.longest_habit_streak
        self.assertEqual(streak,1)

        self.obj3.checkoff('y')
        self.obj3.checkoff('y')
        self.obj3.checkoff('y')
        self.obj3.checkoff('y')
        streak = self.obj3.longest_habit_streak
        self.assertEqual(streak,4)

class TestHabitTracker(unittest.TestCase):
    def setUp(self):
        self.obj1 = HabitTracker("John")
        self.obj1.addHabit("Brush your teeth","2023-03-01","2023-03-4","D") 

    def test_search_by_name(self):
        (h,_,_) = self.obj1.search_by_name("Brush your teeth")
        self.assertEqual(h,"Brush your teeth")
        self.obj1.addHabit("Go to the gym","2023-03-01","2023-03-4","D") 
        (h,_,_) = self.obj1.search_by_name("Go to the gym")
        self.assertEqual(h,"Go to the gym")

    def test_search_by_id(self):
        self.obj1.addHabit("Go to the gym","2023-03-01","2023-03-4","D") 
        h = self.obj1.search_by_id(2)
        self.assertEqual(h,"Go to the gym")



if __name__ == '__main__':
    unittest.main()



    
    

