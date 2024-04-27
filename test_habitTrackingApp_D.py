import unittest
import pandas as pd
from habit_tracking_app import Habit,HabitTracker
from generateUserData import *


class Test_Habit(unittest.TestCase):
    def setUp(self):
        self.obj1 = Habit("Study Docker","2025-05-01","2025-05-07","D")
        self.obj2 = Habit("Study Python","2025-05-06","2025-05-12","D")
        self.obj3 = Habit("Study SQL","2025-05-14","2025-05-20","D")
        self.obj4 = Habit("Study JS","2025-06-01","2025-06-7","D")
       
    def tearDown(self):
        self.obj1 = None
        self.obj2 = None
        self.obj3 = None
        self.obj4 = None
      
    
    def test_checkoff(self):
        """
        This test case verifies that the checkoff method correctly updates a task's completion status for a day.
        To do this,the test case creates four checkoff_lists for each habit defined in the setUp method. It then checks whether that
        the resulting lists match the expected outcome. Additionally, the test case checks whether the checkoff method 
        correctly identifies the longest run streak within the habit.
        """
        ##Obj1
        # Create this list: ['y', 'n', 'y', 'n']
        create_checkofflist_alternated_items(self.obj1,4)

        # Append this list ['y','y','y'] to ['y', 'n', 'y', 'n']
        create_checkofflist_one_item(self.obj1,3,"y")
         
        # Final checkofflist
        expected = ['y', 'n', 'y', 'n', 'y', 'y', 'y']
        
        self.assertEqual(self.obj1.checkoffList,expected)
        self.assertEqual(self.obj1.longest_streak,3)

        ##Obj2
        create_checkofflist_alternated_items(self.obj2,3)

        create_checkofflist_one_item(self.obj2,3,"n")
   
        expected = ['y', 'n', 'y', 'n', 'n', 'n']

        self.assertEqual(self.obj2.checkoffList,expected)
        self.assertEqual(self.obj2.longest_streak,1)
        
        ##Obj3
        create_checkofflist_one_item(self.obj3,6,"y")
        
        expected = ['y', 'y', 'y', 'y', 'y', 'y']
        
        self.assertEqual(self.obj3.checkoffList,expected)
        self.assertEqual(self.obj3.longest_streak,6)
        
        ##Obj4
        create_checkofflist_one_item(self.obj4,6,"n")
        
        expected = ['n', 'n', 'n', 'n', 'n', 'n']
        
        self.assertEqual(self.obj4.checkoffList,expected)
        self.assertEqual(self.obj4.longest_streak,0)

      
      
class TestHabitTracker(unittest.TestCase):
    def setUp(self):
        self.objTracker = HabitTracker("John")
        self.objTracker.add_habit("Study git","2025-07-22","2025-07-25","D")
        self.objTracker.add_habit("Study nosql","2025-07-14","2025-07-21","D")
        self.objTracker.add_habit("Study java","2025-08-14","2025-08-20","D")
        self.objTracker.add_habit("Study mongodb","2025-08-01","2025-08-07","D")
        
    def test_add_habit(self):
        msg = "Habits are not in chronological order."
        self.assertTrue(is_linked_list_sorted(self.objTracker),msg=msg)
        
        self.objTracker.add_habit("Study kubernetes","2025-07-01","2025-07-07","D")
        
        self.objTracker.add_habit("Study fluxcd","2025-05-02","2025-05-06","D")
        
        self.assertTrue(is_linked_list_sorted(self.objTracker),msg=msg)
        
        self.objTracker.print_habits()
        
        
    
    

    def test_get_habit_by_name(self):
        h = self.objTracker.get_habit_by_name("Study git")
        self.assertEqual(h.habit,"Study git")

        h = self.objTracker.get_habit_by_name("Study java")
        self.assertEqual(h.habit,"Study java")

        h = self.objTracker.get_habit_by_name("Study mongodb")
        self.assertEqual(h.habit,"Study mongodb")





    def test_longest_run_streak_of_all(self):
        """This test case checks whether the checkoff method correctly updates a task's completion status for the 
        a day in the context of a HabitTracker object. It then checks whether the 
        get_longest_run_streak_of_all function correctly calculates the longest run streak for a set of habits 
        defined in the setUp method
        """

        create_checkofflist_alternated_items(self.objTracker,3,"Study java")

        create_checkofflist_one_item(self.objTracker,3,"y","Study java")

        expected = ['y','n','y','y', 'y', 'y']

        java = self.objTracker.get_habit_by_name("Study java")

        self.assertEqual(java.checkoffList,expected)
        self.assertEqual(java.longest_streak,4)
        
        print(java.longest_streak,java.habit)


        create_checkofflist_alternated_items(self.objTracker,4,"Study mongodb")

        create_checkofflist_one_item(self.objTracker,2,"n","Study mongodb")
   

        expected = ['y', 'n', 'y', 'n', 'n', 'n']
        
        mongodb = self.objTracker.get_habit_by_name("Study mongodb")

        self.assertEqual(mongodb.checkoffList,expected)

        self.assertEqual(mongodb.longest_streak,1)


        print("hello,there ")
        
        print(mongodb.longest_streak,java.longest_streak)
        create_checkofflist_one_item(self.objTracker,4,"y","Study nosql")

       
        create_checkofflist_alternated_items(self.objTracker,3,"Study nosql")
   

        expected = ["y","y","y","y","y","n","y"]
        
        nosql = self.objTracker.get_habit_by_name("Study nosql")
      
        self.assertEqual(nosql.checkoffList,expected)
        self.assertEqual(nosql.longest_streak,5)

        print("hello")
        print(nosql.longest_streak,java.longest_streak,mongodb.longest_streak)

        myhabit = self.objTracker.get_habit_with_longest_run_streak_of_all()
        
      
    
        
        self.assertEqual({"Study nosql":5},myhabit)

#     def test_delete_habit(self):
#         """This test case checks whether the delete_habit method correctly deletes a habit in the context of a
#           Tracking object
#         """

#         self.objTracker.delete_habit("Brush teeth")
#         self.objTracker.delete_habit("Study Python")
#         self.objTracker.delete_habit("Study SQL")
#         self.objTracker.delete_habit("Study JS")
#         self.assertEqual(self.objTracker.habits,[])

#     def test_get_habits_with_same_property(self):
#         """This test case checks whether the get_habit_with_same_property method correctly 
#         groups habits by property
#         """

#         key_to_compare = ["2023-03-01/2023-03-28","2023-04-01/2023-04-28"]
        
#         self.objTracker.add_habit("Study Flask","2023-04-01","2023-04-28","D")

#         myres = self.objTracker.get_habits_with_same_property("time_period_string")


#         self.assertEqual(len(myres),2)

        
#         for key in myres:
#             assert key in key_to_compare,f"The key {key} is not in the expected keys."

#         max_key = max(myres,key = lambda x : len(myres[x]))

#         self.assertEqual(max_key,"2023-04-01/2023-04-28")

#         self.assertEqual(set(myres[max_key]),set(["Study JS","Study Flask","Study SQL"]))
        
#     def test_data_visualization(self):

#         # Checkoff brush teeth
#         create_checkofflist_alternated_items(self.objTracker,8,"Brush teeth")

#         create_checkofflist_one_item(self.objTracker,10,"y","Brush teeth")
   
#         create_checkofflist_one_item(self.objTracker,10,"n","Brush teeth")

#         #Checkoff Study Python

#         create_checkofflist_alternated_items(self.objTracker,8,"Study Python")

#         create_checkofflist_one_item(self.objTracker,10,"n","Study Python")
   
#         create_checkofflist_one_item(self.objTracker,10,"y","Study Python")

       
       

#         # The checkoffList looks like : [y,n,y,n,y,n,y,n] so there four "y" 
#         create_checkofflist_one_item(self.objTracker,8,"y","Study SQL")

#         # The checkoffList looks like : [y,n,y,n,y,n,y,n,y,n] so there five "y" 
#         create_checkofflist_alternated_items(self.objTracker,10,"Study SQL")
   
#         create_checkofflist_one_item(self.objTracker,10,"n","Study SQL")

    
#         # Study JS

#         create_checkofflist_one_item(self.objTracker,8,"y","Study JS")
       
#         # The checkoffList looks like : [y,y,y,y,y,y,y,y,y,y] so there ten "y" 
#         create_checkofflist_one_item(self.objTracker,10,"n","Study JS")
   
#         # The checkoffList looks like : [y,n,y,n,y,n,y,n,y,n] so there five "y" 
#         create_checkofflist_alternated_items(self.objTracker,10,"Study JS")


#         # Expected output:
#         expected = {"2023-03-01/2023-03-28":28,"2023-04-01/2023-04-28":26}
       
#         res = self.objTracker.data_visualization()
         
#         self.assertEqual(res,expected)
def is_linked_list_sorted(ll):
    slow = ll.head
    fast = ll.head
            
    if ll.length == 1:
        return True 
            
    while fast.next:
        slow = fast 
        fast = slow.next
        if fast.days_until_start <= slow.days_until_start:
           
            return False
    return True





if __name__ == '__main__':
    unittest.main()



    
    

