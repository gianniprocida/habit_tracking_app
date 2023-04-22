import unittest
import pandas as pd
from habit_tracking_app import Habit,HabitTracker


# Tests for weekly habits

class Test_Habit(unittest.TestCase):
    def setUp(self):
        self.obj1 = Habit("Study SQL","2023-04-01","2023-04-22","W")
        self.obj2 = Habit("Study Python","2023-04-01","2023-04-22","W")
        self.obj3 = Habit("Study OOP","2023-05-01","2023-05-22","W")
        self.obj4 = Habit("Study git","2023-05-01","2023-05-22","W")
        self.obj5 = Habit("Study Data modeling","2023-05-01","2023-05-22","W")

    def tearDown(self):
        self.obj1 = None
        self.obj2 = None
        self.obj3 = None
    
    def test_checkoff(self):
        """
        This test case verifies that the checkoff method correctly updates a task's completion status for the current day.
        To do this,the test case creates four checkoff_lists for each habit defined in the setUp method. It then checks whether that
        the resulting lists match the expected outcome. Additionally, the test case checks whether the checkoff method 
        correctly identifies the longest run streak within the habit.
        """

        # Checking off Study SQL 
        self.obj1.checkoff("y")
        self.obj1.checkoff("y")
        self.obj1.checkoff("n")
        self.obj1.checkoff("n")

        excepted = ['y', 'y', 'n', 'n']
        
        self.assertEqual(self.obj1.checkoffList,excepted)
        self.assertEqual(self.obj1.longest_habit_streak,2)


        # Checking off Study Python 
        self.obj2.checkoff("y")
        self.obj2.checkoff("n")
        self.obj2.checkoff("y")
        self.obj2.checkoff("n")

        excepted = ['y', 'n', 'y', 'n']

        self.assertEqual(self.obj2.checkoffList,excepted)
        self.assertEqual(self.obj2.longest_habit_streak,1)
        

        # Checking off Study OOP
        self.obj3.checkoff("y")
        self.obj3.checkoff("y")
        self.obj3.checkoff("y")
        self.obj3.checkoff("y")

        excepted = ['y', 'y', 'y', 'y']

        self.assertEqual(self.obj3.checkoffList,excepted)
        self.assertEqual(self.obj3.longest_habit_streak,4)

   
        # Checking off Study git
        self.obj4.checkoff("y")
        self.obj4.checkoff("y")
        self.obj4.checkoff("y")
        self.obj4.checkoff("n")

        excepted = ['y', 'y', 'y', 'n']

        self.assertEqual(self.obj4.checkoffList,excepted)
        self.assertEqual(self.obj4.longest_habit_streak,3)

        
        # Checking off Study Data modeling
        self.obj5.checkoff("n")
        self.obj5.checkoff("n")
        self.obj5.checkoff("n")
        self.obj5.checkoff("n")

        excepted = ['n', 'n', 'n', 'n']

        self.assertEqual(self.obj5.checkoffList,excepted)
        self.assertEqual(self.obj5.longest_habit_streak,0)
    

class TestHabitTracker(unittest.TestCase):
    def setUp(self):
        self.objTracker  = HabitTracker("John")
        self.objTracker.add_habit("Study SQL","2023-04-01","2023-04-22","W")
        self.objTracker.add_habit("Study Python","2023-04-01","2023-04-22","W")
        self.objTracker.add_habit("Study OOP","2023-05-01","2023-05-22","W")
        self.objTracker.add_habit("Study git","2023-05-01","2023-05-22","W")
        self.objTracker.add_habit("Study Data modeling","2023-05-01","2023-05-22","W")

      

    def test_get_habit_by_name(self):
        h = self.objTracker.get_habit_by_name("Study SQL")
        self.assertEqual(h.name,"Study SQL")

        h = self.objTracker.get_habit_by_name("Study Python")
        self.assertEqual(h.name,"Study Python")

        h = self.objTracker.get_habit_by_name("Study OOP")
        self.assertEqual(h.name,"Study OOP")

        h = self.objTracker.get_habit_by_name("Study git")
        self.assertEqual(h.name,"Study git")




    def test_longest_run_streak_of_all(self):
        """This test case checks whether the checkoff method correctly updates a task's completion status for the 
        current day in the context of a HabitTracker object. It then checks whether the 
        get_longest_run_streak_of_all function correctly calculates the longest run streak for a set of habits 
        defined in the setUp method
        """

        #Checking off Study SQL
        self.objTracker.checkoff_by_name("Study SQL","y")
        self.objTracker.checkoff_by_name("Study SQL","y")
        self.objTracker.checkoff_by_name("Study SQL","n")
        self.objTracker.checkoff_by_name("Study SQL","n")

        excepted = ['y', 'y', 'n', 'n']

        h = self.objTracker.get_habit_by_name("Study SQL")

        self.assertEqual(h.checkoffList,excepted)
        self.assertEqual(h.longest_habit_streak,2)


        # Checking off Study Python
        self.objTracker.checkoff_by_name("Study Python","y")
        self.objTracker.checkoff_by_name("Study Python","n")
        self.objTracker.checkoff_by_name("Study Python","y")
        self.objTracker.checkoff_by_name("Study Python","n")

        excepted = ['y', 'n', 'y', 'n']

        h = self.objTracker.get_habit_by_name("Study Python")

        self.assertEqual(h.checkoffList,excepted)
        self.assertEqual(h.longest_habit_streak,1)

   
         # Checking off Study OOP
        self.objTracker.checkoff_by_name("Study OOP","y")
        self.objTracker.checkoff_by_name("Study OOP","y")
        self.objTracker.checkoff_by_name("Study OOP","y")
        self.objTracker.checkoff_by_name("Study OOP","y")

        excepted = ['y', 'y', 'y', 'y']

        h = self.objTracker.get_habit_by_name("Study OOP")

        self.assertEqual(h.checkoffList,excepted)
        self.assertEqual(h.longest_habit_streak,4)


         # Checking off git 
        self.objTracker.checkoff_by_name("Study git","y")
        self.objTracker.checkoff_by_name("Study git","y")
        self.objTracker.checkoff_by_name("Study git","y")
        self.objTracker.checkoff_by_name("Study git","n")

        excepted = ['y', 'y', 'y', 'n']

        h = self.objTracker.get_habit_by_name("Study git")

        self.assertEqual(h.checkoffList,excepted)
        self.assertEqual(h.longest_habit_streak,3)


        # Checking off Data modeling
        self.objTracker.checkoff_by_name("Study Data modeling","n")
        self.objTracker.checkoff_by_name("Study Data modeling","n")
        self.objTracker.checkoff_by_name("Study Data modeling","n")
        self.objTracker.checkoff_by_name("Study Data modeling","n")

        excepted = ['n', 'n', 'n', 'n']

        h = self.objTracker.get_habit_by_name("Study Data modeling")

        self.assertEqual(h.checkoffList,excepted)
        self.assertEqual(h.longest_habit_streak,0)




        h = self.objTracker.get_habit_with_longest_run_streak_of_all()
    
       
        self.assertEqual({"Study OOP":4},h)

    def test_delete_habit(self):
        """This test case checks whether the delete_habit method correctly deletes a habit in the context of a
          Tracking object
        """

        self.objTracker.delete_habit("Study Data modeling")
        self.objTracker.delete_habit("Study Python")
        self.objTracker.delete_habit("Study SQL")
        self.objTracker.delete_habit("Study git")
        self.objTracker.delete_habit("Study OOP")
        self.assertEqual(self.objTracker.habits,[])

    def test_get_habits_with_same_property(self):
        """This test case checks whether the get_habit_with_same_property method correctly 
        groups habits by property
        """

        key_to_compare = ["2023-04-01/2023-04-22","2023-05-01/2023-05-22"]
        
        self.objTracker.add_habit("Study Flask","2023-05-01","2023-05-22","D")

        myres = self.objTracker.get_habits_with_same_property("time_period_string")


        self.assertEqual(len(myres),2)

        
        for key in myres:
            assert key in key_to_compare,f"The key {key} is not in the expected keys."

        max_key = max(myres,key = lambda x : len(myres[x]))

        self.assertEqual(max_key,"2023-05-01/2023-05-22")

        self.assertEqual(set(myres[max_key]),set(["Study OOP","Study Data modeling","Study git","Study Flask"]))



if __name__ == '__main__':
    unittest.main()



    
    

