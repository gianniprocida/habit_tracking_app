from habit_tracking_app import Habit,HabitTracker

# Function for testing purposes
def create_checkofflist_one_item(obj,n,check,name=[]):
    """ Add n items ("y" or "n") to the checkoffList of the habit object.

    Args:
        obj : object
        An object representing  either a habit object or habitTracker

        n (int) : The number of items you wish to add to the checkoffList.

        check (str): The type of check ("y" or "n") you want to add to the checkoffList

        name (str): This argument is only relevant if the obj is a habit tracker.


    Example:
        >>> myhabit = Habit("Study SQL","2023-03-01","2023-03-28","D")
        >>> create_checkofflist_one_item(myhabit,10,"y")
        >>> myhabit.checkoffList
        ['y','y','y','y','y','y','y','y','y','y']

    """

    for i in range(n):
        if isinstance(obj,HabitTracker):
            obj.checkoff_by_name(name,check)
        else:
            obj.checkoff(check)


def create_checkofflist_alternated_items(obj,n,name=[]):
      """Add n items ("y" and "n") to the checkoffList of the given object.
    
      Args:
        obj : object
        An object representing  either a habit object or habitTracker

        n (int) : The number of items you wish to add to the checkofflist.

        name (str): This argument is only relevant if the obj is a habit tracker.


    Example:
        >>> myhabit = Habit("Study Python","2023-03-01","2023-03-28","D")
        >>> create_checkofflist_alternated_items(myhabit,7)
        >>> myhabit.checkoffList
        ['y','n','y','n','y','n','y']

    """
      for i in range(n):
        if isinstance(obj,HabitTracker):
            if i % 2 == 0:
                  obj.checkoff_by_name(name,"y")
            else:
                  obj.checkoff_by_name(name,"n")
        else:
            if i % 2 == 0:
                  obj.checkoff("y")
            else:
                  obj.checkoff("n")
             

if __name__=='__main__':
      myhabit = Habit("Study Python","2023-03-01","2023-03-28","D")
      create_checkofflist_alternated_items(myhabit,7)
      print(myhabit.checkoffList)
      assert len(myhabit.checkoffList) == 7
      assert myhabit.checkoffList == ["y","n","y","n","y","n","y"]

      myhabit = Habit("Study SQL","2023-03-01","2023-03-28","D")
      create_checkofflist_one_item(myhabit,10,"y")
      print(myhabit.checkoffList)
      assert len(myhabit.checkoffList) == 10
      assert myhabit.checkoffList == ["y","y","y","y","y","y","y","y","y","y"]

      

