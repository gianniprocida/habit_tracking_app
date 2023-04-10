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
        self.assertEqual(self.obj1.checkoffList,["y","y","n","y"])
        streak = self.obj1.longest_habit_streak
        self.assertEqual(streak,2)

        self.obj2.checkoff('y')
        self.obj2.checkoff('n')
        self.obj2.checkoff('y')
        self.obj2.checkoff('n')
        self.obj2.checkoff('y')
        self.assertEqual(self.obj2.checkoffList,["y","n","y","n","y"])
        streak = self.obj2.longest_habit_streak
        self.assertEqual(streak,1)

        self.obj3.checkoff('y')
        self.obj3.checkoff('y')
        self.obj3.checkoff('y')
        self.obj3.checkoff('y')
        self.assertEqual(self.obj3.checkoffList,["y","y","y","y"])
        streak = self.obj3.longest_habit_streak
        self.assertEqual(streak,4)

class TestHabitTracker(unittest.TestCase):
    def setUp(self):
        self.objTracker = HabitTracker("John")
        self.objTracker.add_habit("Brush your teeth","2023-03-01","2023-03-04","D") 
        

    def test_get_habit_by_name(self):
        h = self.objTracker.get_habit_by_name("Brush your teeth")
        self.assertEqual(h.name,"Brush your teeth")
        self.objTracker.add_habit("Go to the gym","2023-03-01","2023-03-04","D") 
        h = self.objTracker.get_habit_by_name("Go to the gym")
        self.assertEqual(h.name,"Go to the gym")

    # def test_checkoff_by_name(self):
    #     self.objTracker.add_habit("Study Python","2023-03-02","2023-03-05","D")
    #     self.objTracker.checkoff_by_name("Study Python","y")

    #     self.objTracker.
    #     self.objTracker.checkoff_by_name("Study Python","n")
    #     self.objTracker.checkoff_by_name("Study Python","y")
    #     self.assertEqual()

    def test_longest_run_streak_of_all(self):
        self.objTracker.add_habit("Go to school","2023-03-02","2023-03-05","D")
        self.objTracker.checkoff_by_name("Brush your teeth","y")
        self.objTracker.checkoff_by_name("Brush your teeth","y")
        self.objTracker.checkoff_by_name("Brush your teeth","y")
        self.objTracker.checkoff_by_name("Brush your teeth","n")

        self.objTracker.checkoff_by_name("Go to school","y")
        self.objTracker.checkoff_by_name("Go to school","n")
        self.objTracker.checkoff_by_name("Go to school","y")
        self.objTracker.checkoff_by_name("Go to school","n")
        self.assertEqual({"Brush your teeth":3},self.objTracker.get_longest_run_streak_of_all())

    def test_delete_habit(self):
        self.objTracker.add_habit("Go to school","2023-03-02","2023-03-05","D")
        self.objTracker.add_habit("Study SQL","2023-03-02","2023-03-05","D")
        self.objTracker.delete_habit("Brush your teeth")
        self.objTracker.delete_habit("Go to school")
        self.objTracker.delete_habit("Study SQL")
        self.assertEqual(self.objTracker.habits,[])
    
    def test_get_habits_with_same_property(self):
        self.objTracker.add_habit("Go to school","2023-03-02","2023-03-25","D")

        self.objTracker.add_habit("Study SQL","2023-03-01","2023-03-05","D")

        self.objTracker.add_habit("Study JavaScript","2023-03-02","2023-03-05","D")

        self.objTracker.add_habit("Study Python","2023-03-02","2023-03-05","D")

        key_to_compare = ["2023-03-01-2023-03-04","2023-03-02-2023-03-25","2023-03-01-2023-03-05","2023-03-02-2023-03-05"]

        myres = self.objTracker.get_habits_with_same_property("time_period_string")

        self.assertEqual(len(myres),4)

        
        for key in myres:
            assert key in key_to_compare,f"The key {key} is not in the expected keys."

        max_key = max(myres,key = lambda x : len(myres[x]))

        self.assertEqual(max_key,"2023-03-02-2023-03-05")

        self.assertEqual(set(myres[max_key]),set(["Study JavaScript","Study Python"]))



if __name__ == '__main__':
    unittest.main()



    
    

