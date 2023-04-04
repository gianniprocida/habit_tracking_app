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
      <li>hello</li>
      <li>hello</li>
    <li>jo</li>
    <ul>
  <h2>Features</h2>
  <h3>Creating habits</h3>

```
tracker = HabitTracker("John")
tracker.addHabit("Brush your teeth","2023-03-01","2023-03-4","D")
tracker.addHabit("Go to school","2023-03-02","2023-04-30","D")
```

<h3>Deleting habits</h3>
To delete a habit, use the delete method:

```
tracker.deleteHabit("Go to school")
```

<h3>Searching by name</h3>
To search for a habit, use the search_by_name method:

```
(myhabit,index) = tracker.search_by_name("Brush your teeth")
```

<h3>Searching by id</h3>

```
output = tracker.search_by_id(1)
```

<h3>Checking off by name</h3>

```
tracker.checkoff_by_name("Brush your teeth","y")
tracker.checkoff_by_name("Brush your teeth","y")
```

</body>
