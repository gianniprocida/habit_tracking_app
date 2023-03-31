import pandas as pd
import datetime
import sys
import mysql.connector

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
            print("Conversion..")
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
        self.completed = None
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
        if len(self.checkoffList) == self.period:# and datetime.date.today() == self.end
            self.completed = True
            self.count_of_completed_activities = self.checkoffList.count("y")
            self.longest_habit_streak = ans
    
class HabitTracker:
    def __init__(self,user):
        self.user = user
        self.habits = []
    def getConn(self):
        cnx = mysql.connector.connect(host="localhost",user="root",password="Chimica90$",database="HabitTrackerdb")
        cur = cnx.cursor()
        return cnx, cur
    def createTable(self):
        (cnx,cur) = self.getConn()
    #    createdb = """create database if not exists HabitTrackerdb"""
  #      usedb = """use HabitTrackerdb"""
        create_query = """create table if not exists HabitTracker (id int not null auto_increment,user varchar(50),habit varchar(50),
        start date, end date,freq varchar(50), primary key(id))"""
        alter_query = """alter table HabitTracker add unique (user,habit)"""

       
 
#        cur.execute(usedb)
        cur.execute(create_query)
        cur.execute(alter_query)
        cnx.commit()
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

           select_query = """select id,start,end,freq from HabitTracker where habit = (%s)"""
           data = (name,)
           cur.execute(select_query,data)
           return cur.fetchall()
        except mysql.connector.Error as error:
            print(f"Error querying data : {error}")
        finally:
            cur.close()
    
    def addHabit(self,name,start,end,freq):
        (cnx,cur) = self.getConn()
   #     usedb = """use HabitTrackerdb"""
   #     cur.execute(usedb)
        try:
           add_query = """insert into HabitTracker (user,habit,start,end,freq) values (%s,%s,%s,%s,%s)"""
           data = (self.user,name,start,end,freq)
           cur.execute(add_query,data)
           cnx.commit()
           print("Habit successfully added...")
        except mysql.connector.Error as error:
            print(f"Error adding habit: {error}") 
        finally:
            cur.close()
    def log_habit(self):
        pass

    def modifyHabit(self,name,start=None,end=None,freq=None):
        if not bool(start) and not bool(end) and bool(freq):
            print("Arguments all empty!")
            pass
        elif bool(start) and bool(end):
            pass
        elif bool(freq):
            pass
        return 



tracker = HabitTracker("John")
tracker.addHabit("Brush your teeth","2023-03-01","2023-03-5","D")
tracker.habits[0].check_off()
tracker.habits[0].check_off()
print(tracker.habits[0].checkoffList)
# tracker.addHabit("Go to school","2023-03-02","2023-03-25","D")
# a = tracker.search_by_name("Go to school")
# a = tracker.search_by_name("Go to work")
# tracker.createTable()
# print(tracker.habits)

# for i in range(6):
#  a = tracker.habits[0].checkoff("n")
#  print(a)