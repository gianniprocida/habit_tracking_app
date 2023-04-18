import unittest
import pandas as pd
from habit_tracking_app import Habit,HabitTracker
from other_fun import *


# Tests for daily habits

class Test_Habit(unittest.TestCase):
    def setUp(self):
        self.obj1 = Habit("Brush teeth","2023-03-01","2023-03-28","D")
        self.obj2 = Habit("Study Python","2023-03-01","2023-03-28","D")
        self.obj3 = Habit("Study SQL","2023-04-01","2023-04-28","D")
        self.obj4 = Habit("Study JS","2023-04-01","2023-04-28","D")
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
      
        # Create this checkoffList ['y', 'n', 'y', 'n', 'y', 'n', 'y', 'n']
        create_checkofflist_alternated_items(self.obj1,8)

        # Create this checkoffList ['y','y','y','y','y','y','y','y','y','y']
        create_checkofflist_one_item(self.obj1,10,"y")
        
        # Create this checkoffList ['n','n','n','n','n','n','n','n','n','n']
        create_checkofflist_one_item(self.obj1,10,"n")
        
        # Final checkofflist
        excepted = ['y', 'n', 'y', 'n', 'y', 'n', 'y', 'n','y','y','y','y',\
               'y','y','y','y','y','y','n','n','n','n','n','n','n','n',\
               'n','n']
        
        self.assertEqual(self.obj1.checkoffList,excepted)
        self.assertEqual(self.obj1.longest_habit_streak,10)


        create_checkofflist_alternated_items(self.obj2,8)

        create_checkofflist_one_item(self.obj2,10,"n")
   
        create_checkofflist_one_item(self.obj2,10,"y")

        excepted = ['y', 'n', 'y', 'n', 'y', 'n', 'y', 'n','n','n','n','n',\
               'n','n','n','n','n','n','y','y','y','y','y','y','y','y',\
               'y','y']

        self.assertEqual(self.obj2.checkoffList,excepted)
        self.assertEqual(self.obj2.longest_habit_streak,10)

        # ["y","y","y","y","y","y","y","y"]
        create_checkofflist_one_item(self.obj3,8,"y")

        # ["y","n","y","n","y","n","y","n","y","n"]   
        create_checkofflist_alternated_items(self.obj3,10)
   
        # ["n","n","n","n","n","n","n","n","n","n"]
        create_checkofflist_one_item(self.obj3,10,"n")
        
        # Final checkoffList
        excepted = ["y","y","y","y","y","y","y","y","y","n","y","n","y","n","y","n","y","n",\
        "n","n","n","n","n","n","n","n","n","n"]
        
      
        self.assertEqual(self.obj3.checkoffList,excepted)
        self.assertEqual(self.obj3.longest_habit_streak,9)



        create_checkofflist_one_item(self.obj4,8,"y")

       
        create_checkofflist_one_item(self.obj4,10,"n")
   
       
        create_checkofflist_alternated_items(self.obj4,10)

        excepted = ["y","y","y","y","y","y","y","y","n","n","n","n","n","n","n",\
                    "n","n","n","y","n","y","n","y","n","y","n","y","n"]
        
        self.assertEqual(self.obj4.checkoffList,excepted)
        self.assertEqual(self.obj4.longest_habit_streak,8)


class TestHabitTracker(unittest.TestCase):
    def setUp(self):
        self.objTracker = HabitTracker("John")
        self.objTracker.add_habit("Brush teeth","2023-03-01","2023-03-28","D")
        self.objTracker.add_habit("Study Python","2023-03-01","2023-03-28","D")
        self.objTracker.add_habit("Study SQL","2023-04-01","2023-04-28","D")
        self.objTracker.add_habit("Study JS","2023-04-01","2023-04-28","D")
      

    def test_get_habit_by_name(self):
        h = self.objTracker.get_habit_by_name("Brush teeth")
        self.assertEqual(h.name,"Brush teeth")

        h = self.objTracker.get_habit_by_name("Study Python")
        self.assertEqual(h.name,"Study Python")

        h = self.objTracker.get_habit_by_name("Study SQL")
        self.assertEqual(h.name,"Study SQL")

        h = self.objTracker.get_habit_by_name("Study JS")
        self.assertEqual(h.name,"Study JS")




    def test_longest_run_streak_of_all(self):
        """This test case checks whether the checkoff method correctly updates a task's completion status for the 
        current day in the context of a HabitTracker object. It then checks whether the 
        get_longest_run_streak_of_all function correctly calculates the longest run streak for a set of habits 
        defined in the setUp method
        """

        create_checkofflist_alternated_items(self.objTracker,8,"Brush teeth")

        create_checkofflist_one_item(self.objTracker,10,"y","Brush teeth")
   
        create_checkofflist_one_item(self.objTracker,10,"n","Brush teeth")

        excepted = ['y', 'n', 'y', 'n', 'y', 'n', 'y', 'n','y','y','y','y',\
               'y','y','y','y','y','y','n','n','n','n','n','n','n','n',\
               'n','n']

        h = self.objTracker.get_habit_by_name("Brush teeth")

        self.assertEqual(h.checkoffList,excepted)
        self.assertEqual(h.longest_habit_streak,10)




        create_checkofflist_alternated_items(self.objTracker,8,"Study Python")

        create_checkofflist_one_item(self.objTracker,10,"n","Study Python")
   
        create_checkofflist_one_item(self.objTracker,10,"y","Study Python")

        excepted = ['y', 'n', 'y', 'n', 'y', 'n', 'y', 'n','n','n','n','n',\
               'n','n','n','n','n','n','y','y','y','y','y','y','y','y',\
               'y','y']
        
        h = self.objTracker.get_habit_by_name("Study Python")

        self.assertEqual(h.checkoffList,excepted)

        self.assertEqual(h.longest_habit_streak,10)



        create_checkofflist_one_item(self.objTracker,8,"y","Study SQL")

       
        create_checkofflist_alternated_items(self.objTracker,10,"Study SQL")
   
    
        create_checkofflist_one_item(self.objTracker,10,"n","Study SQL")

        excepted = ["y","y","y","y","y","y","y","y","y","n","y","n","y","n","y","n","y","n",\
        "n","n","n","n","n","n","n","n","n","n"]
        
        h = self.objTracker.get_habit_by_name("Study SQL")
      
        self.assertEqual(h.checkoffList,excepted)
        self.assertEqual(h.longest_habit_streak,9)


        create_checkofflist_one_item(self.objTracker,8,"y","Study JS")

        
        create_checkofflist_one_item(self.objTracker,10,"n","Study JS")
   

        create_checkofflist_alternated_items(self.objTracker,10,"Study JS")

        excepted = ["y","y","y","y","y","y","y","y","n","n","n","n","n","n","n",\
                    "n","n","n","y","n","y","n","y","n","y","n","y","n"]
        
        h = self.objTracker.get_habit_by_name("Study JS")

        self.assertEqual(h.checkoffList,excepted)
        self.assertEqual(h.longest_habit_streak,8)

        h = self.objTracker.get_habit_with_longest_run_streak_of_all()
    
       
        self.assertEqual({"Brush teeth":10},h)

    def test_delete_habit(self):
        """This test case checks whether the delete_habit method correctly deletes a habit in the context of a
          Tracking object
        """

        self.objTracker.delete_habit("Brush teeth")
        self.objTracker.delete_habit("Study Python")
        self.objTracker.delete_habit("Study SQL")
        self.objTracker.delete_habit("Study JS")
        self.assertEqual(self.objTracker.habits,[])

    def test_get_habits_with_same_property(self):
        """This test case checks whether the get_habit_with_same_property method correctly 
        groups habits by property
        """

        key_to_compare = ["2023-03-01-2023-03-28","2023-04-01-2023-04-28"]
        
        self.objTracker.add_habit("Study Flask","2023-04-01","2023-04-28","D")

        myres = self.objTracker.get_habits_with_same_property("time_period_string")


        self.assertEqual(len(myres),2)

        
        for key in myres:
            assert key in key_to_compare,f"The key {key} is not in the expected keys."

        max_key = max(myres,key = lambda x : len(myres[x]))

        self.assertEqual(max_key,"2023-04-01-2023-04-28")

        self.assertEqual(set(myres[max_key]),set(["Study JS","Study Flask","Study SQL"]))



if __name__ == '__main__':
    unittest.main()



    
    

