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

Before using the Habit Tracker App make sure you have Python3 installed on your computer.
<h3>How to run it?</h3>
     <ul>
      <li>Clone the repository from GitHub: git clone https://github.com/gianniprocida/habit_tracking_app.git</li>
      <li>Navigate to the habit-tracker directory: cd habit-tracker</li>
      <li></li>
    <ul>
<h2>Features</h2>
<h3>Create new habits</h3>
asdaasda

```
tracker = HabitTracker("John")
tracker.addHabit("Brush your teeth","2023-04-01","2023-04-28","D")
tracker.addHabit("Study Python","2023-04-01","2023-04-28","D")
```

<h3>Deleting habits</h3>
To delete a habit, use the delete method:

```
tracker.delete_habit("Study Python")
```

<h3>Get habit by name</h3>
To search for a habit, use the get_habit_by_name method:

```
myhabit = tracker.get_habit_by_name("Brush your teeth")
```

<h3>Get habit by id</h3>

```
myhabit = tracker.get_habit_by_id(1)
```

<h3>Checking off by name</h3>

```
tracker.checkoff_by_name("Brush your teeth","y")
tracker.checkoff_by_name("Brush your teeth","y")
```

<h2>Thought Process and Development of the Habit Tracking App</h2>
Formally, a habit is a clearly defined task that must be completed periodically 
(e.g., brush your teeth every day or go to the dentist once every year). 
The obvious object, therefore, is the <span style="color: red;">Habit</span> object; less obvious one is 
a <span style="color: red;">Habit Tracking</span> container object. The relationship between the 
two classes of objects in our tracking app can be described using a UML class diagram. Here is our 
first class diagram:
This UML diagram provides a visual representation of the one-to-many relationship between 
the Habit and HabitTracker classes, with one HabitTracker having zero or more Habit objects associated 
with it. 

</body>
