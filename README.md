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
    csv files (pricing data ) are downloaded through web scraping, after which they are cleaned using 
    using pandas. Data are going to be distributed across several databases.
         For example, we create a database with only BTC pricing data, EOS pricing data, ETH pricing data, and LTC pricing data.
  <ul>  
      Input required:  </li>
      <li>BTCUSDT_Binance_futures_data_day.csv</li>
      <li>EOSUSDT_Binance_futures_data_day</li>
      <li>ETHUSDT_Binance_futures_data_day</li>
      <li>LTCUSDT_Binance_futures_data_day</li>
      <li>TO DO: Add Entity relationship model </li>

  </ul>
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


