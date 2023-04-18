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
<h2>Thought Process and Development of the Habit Tracking App</h2>
Formally, a habit is a clearly defined task that must be completed periodically 
(e.g., brush your teeth every day or go to the dentist once every year). 
The obvious object, therefore, is the <span style="color: red;">Habit</span> object; less obvious one is 
a <span style="color: red;">Habit Tracker</span> container object. The relationship between the 
two classes of objects in our tracking app can be described using a UML class diagram. Here is our 
first class diagram:
<img src="uml_diagr.png" alt="Description of the image">
This UML diagram provides a visual representation of the one-to-many relationship between 
the Habit and HabitTracker classes, with one HabitTracker having zero or more Habit objects associated 
with it. The folder structure for this project looks like this:
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
