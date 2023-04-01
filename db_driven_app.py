import pandas as pd
import datetime
import sys
import mysql.connector

# one user at once
last_id = 0
class Habit:
    def __init__(self,name,start,end,freq):
        # check arguments passed in the constructor
        if not isinstance(start,str):
            raise TypeError("start must be a string")
        else:
            # convert the date string to a date object
            date_object = datetime.datetime.strptime(start, '%Y-%m-%d').date()
            start = date_object.strftime('%Y-%m-%d')
        if not isinstance(end,str):
            raise TypeError("end must be a string")
        else:
            date_object = datetime.datetime.strptime(end, '%Y-%m-%d').date()
            end = date_object.strftime('%Y-%m-%d')
        self.name = name
        self.start = start
        self.end = end
        self.freq = freq
        self.period = len(pd.date_range(start=self.start, end=self.end, freq=self.freq))
        self.checkoffList = []
        global last_id
        last_id+=1
        self.id = last_id
        self.creation_date = datetime.date.today()
        self.completed = False
        self.longest_habit_streak = None
        self.count_of_completed_habit = None
    def checkoff(self,check):
        ans = 0
        if not self.completed:
          if check == "y":
             self.checkoffList.append("y")
          elif check =="n":
             self.checkoffList.append("n")
          else:
             raise TypeError("Invalid input")
          if len(self.checkoffList) > 1 and "y" in self.checkoffList:
              ans = 1
              for i in range(len(self.checkoffList)):
                  j = i + 1
                  while j < len(self.checkoffList) and self.checkoffList[j] == self.checkoffList[i]=="y":
                    j+=1
                  ans = max(ans,j-i)
        else:
            print("No need to checkoff no more...")
            print("Exit...")  
            return 
        if len(self.checkoffList) == self.period:# and datetime.date.today() == self.end
            self.completed = True
            self.count_of_completed_habit = self.checkoffList.count("y")

            self.longest_habit_streak = ans
    
class HabitTracker:
    def __init__(self):
        self.habits = []
    def getConn(self):
        cnx = mysql.connector.connect(host="localhost",user="root",password="Chimica90$",database="HabitTrackerdb")
        cur = cnx.cursor()
        return cnx, cur
    def createTables(self):
        (cnx,cur) = self.getConn()
    #    createdb = """create database if not exists HabitTrackerdb"""
  #      usedb = """use HabitTrackerdb"""

        try:
            create_HabitTracker = """create table if not exists HabitTracker (id int not null auto_increment,name varchar(50),
        start date, end date,freq varchar(50), primary key(id))"""
    #    alter_query = """alter table HabitTracker add unique (habit)"""
            create_ScoreTracker = """create table if not exists ScoreTracker (id int not null auto_increment,name varchar(50),longest_habit_streak int default null,
         count_of_completed_habit int default null, primary key(id))"""
            cur.execute(create_HabitTracker)
            cur.execute(create_ScoreTracker)
            cnx.close()
        except mysql.connector.Error as error:
            print(f"Error creating tables: {error}")
        finally:
            cur.close()

    def search_by_id(self,id):
        (cnx,cur) = self.getConn()
        try:
           select_query = """select habit,start,end,freq from HabitTracker where id = (%s)"""
           data = (id,)
           cur.execute(select_query,data)
           return cur.fetchall()
        except mysql.connector.Error as error:
            print(f"Error querying data : {error}")
        finally:
            cur.close()
        
    def search_by_name(self,name):
        (cnx,cur) = self.getConn()
        try:

           select_query = """select id,start,end,freq from HabitTracker where name = (%s)"""
           data = (name,)
           cur.execute(select_query,data)
           return cur.fetchall()
        except mysql.connector.Error as error:
            print(f"Error querying data : {error}")
        finally:
            cur.close()
    
    def addHabit(self,name,start,end,freq):
        if self.search_by_name(name):
            print("Already added! ")
        else:
            print("Adding your habit..")
            self.habits.append(Habit(name,start,end,freq))

        # db    
        (cnx,cur) = self.getConn()
        try:
           add_query = """insert into HabitTracker (name,start,end,freq) values (%s,%s,%s,%s)"""
           data = (name,start,end,freq)
           cur.execute(add_query,data)
           add_query = """insert into ScoreTracker (name) values (%s)"""
           data = (name,)
           cur.execute(add_query,data)
           cnx.commit()
           print("Habit successfully added...")
        except mysql.connector.Error as error:
            print(f"Error adding habit: {error}") 
        finally:
            cur.close()
    def add_score(self,name):
        # db    
        (cnx,cur) = self.getConn()
        for item in self.habits:
            if item.name == name and not item.completed:
                print(f"Error : {item.name} not completed")
            elif item.name == name and item.completed:
                data = (item.longest_habit_streak,item.count_of_completed_habit,name)
                update_query = """update ScoreTracker set longest_habit_streak = (%s),count_of_completed_habit = (%s)
                where name = (%s)"""
                cur.execute(update_query,data)
                cnx.commit()

    def modifyHabit(self,name,start=None,end=None,freq=None):
        if not bool(start) and not bool(end) and bool(freq):
            print("Arguments all empty!")
            pass
        elif bool(start) and bool(end):
            pass
        elif bool(freq):
            pass
        return 



tracker = HabitTracker()
tracker.createTables()
tracker.addHabit("Go to work","2023-03-01","2023-03-4","D")
tracker.habits[0].checkoff("y")
tracker.habits[0].checkoff("y")
tracker.habits[0].checkoff("y")
tracker.habits[0].checkoff("y")
tracker.habits[0].checkoff("y")
print(tracker.habits[0].completed)
tracker.add_score("Go to work")

# tracker.addHabit("Go to school","2023-03-02","2023-03-25","D")
# a = tracker.search_by_name("Go to school")
# a = tracker.search_by_name("Go to work")
# tracker.createTable()
# print(tracker.habits)

# for i in range(6):
#  a = tracker.habits[0].checkoff("n")
#  print(a)