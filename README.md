<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
<h1>Overview</h1>
<hr>
<p>Habit tracking app that allows users to track their daily habits and 
      monitor their progress over time. Users can create, modifiy, delete, and search habits, and check off each day
    they complete the habit</a></p>
<h2>Getting started</h2>

Before using the Habit Tracking App make sure you have Python3 installed on your computer.
<h3>How to run it?</h3>
     <ul>
      <li>Clone the repository from GitHub: git clone https://github.com/gianniprocida/habit_tracking_app.git</li>
      <li>Navigate to the habit-tracker directory: cd habit-tracking_app</li>
      <li>Install any dependencies required by the project:
        <ul>
          <li>pandas</li>
        </ul>
      </li>   
      <li>Run the project by executing the menu Python file: python menu.py</li>
      This should start the habit tracking program and allow you to interact with it via the user interface provided by the project.
    <ul>
<h2>Features</h2>
<h3>Create new habits</h3>
To start tracking habits, you need to create a HabitTracker instance by providing the name of the user. Then we pass in the name of the habit,"Study OOP", the start date of the habit period,`2023-04-01`, the end date of the habit period,"2023-04-28", and the frequency,'D'.

```
tracker = HabitTracker("John")
tracker.addHabit("Study OOP","2023-04-01","2023-04-28","D")
```

<h3>Delete a habit</h3>
We call the `delete_habit` method on the HabitTracking class and pass in the name of the habit we want to delete.
This will remove the habit from the tracker object.

```
tracker.delete_habit("Study Python")
```

<h3>Get habit by name</h3>
We call the `get_habit_by_name` method on the HabitTracker class and pass in the 
name of the habit we want to retrieve. This will return a `Habit' instance with the specified name.

```
myhabit = tracker.get_habit_by_name("Brush your teeth")
```

<h3>Get habit by id</h3>
We call the `get_habit_by_name` method on the HabitTracker class and pass in the id of
the habit we want to retrieve. This will return a `Habit' instance with the specified id.

```
myhabit = tracker.get_habit_by_id(1)
```

<h3>Check off by name</h3>
We call the `checkoff_by_name` method on the HabitTracker class and pass in the name of the habit we want to check off. This 
will add the string "y" to the checkoffList of the `Habit` instance with the specified name.

```
tracker.checkoff_by_name("Brush your teeth","y")
tracker.checkoff_by_name("Brush your teeth","y")
```
These are just a few examples of the functionality of this habit tracking app. 
For more information, please see the documentation or explore the source code.
<h2>Conception phase</h2>

In our habit tracking app, a Habit object can represent a task that needs to be performed 
regularly, such as studying a programming languages weekly or exercising daily. 
The <span style="color: red;">Habit</span> object can have attributes like name of the habit, 
start date, end date, frequency, checkofflist ( a list containing “y” or “n” to indicate 
whether the habit was completed or not for a day), ID, completed (whether the habit was 
completed within the given period), and longest habit streak (the maximum number of times 
the habit was completed in a row). To manage multiple habits in  the app, we can create a 
<span style="color: red;">HabitTracker</span>  container object that 
has attributes like user name and a list of habits. This will make it easier to add new
 habits, delete habits, retrieve habits by name, retrieve habits by id or group habits by 
 specific attribues, and find the habit with the longest run streak. Moreover, 
 the<span style="color: red;">Habit</span>object includes a<span style="color: red;">checkoff</span>method that 
 allows users to mark the habit as completed (“y” or “n”) at any point in time. However, the total number of marks cannot 
 exceed the number of days in that period. If the maximum number of marks is reached, the 
 method will stop adding additional marks to the checkofflist attribute.
 The relationship between the two classes of objects in our tracking app can be described 
 using a UML class diagram. 
 
 This UML diagram provides a visual representation of the 
 one-to-many relationship between the Habit and<span style="color: red;">HabitTracker</span>classes, with one HabitTracker
  having zero or more Habit objects associated with it. 

 The folder structure for this project looks like this:
 <ul>
  <li>parent directory/
    <ul>
      <li>menu.py</li>
      <li>habit_tracking_app.py</li>
    </ul>
  </li>
</ul>
The Habit and HabitTracker objects can live together in one module. The menu interface simply allows a user to navigate through a set of options and perform different actions based on their selections.
</body>
