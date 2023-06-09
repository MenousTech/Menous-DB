![](../assets/logo-full.png)

# Introduction
Menous DB is a simple and elegant key value database. It uses a structured file system to store key values. The database is written in python and can be used directly in python using the menousdb pip package.

# Installation
You can install the menousdb module by using the pip package manager. You can install the package manager on all platforms by using the following commands:
```
For Linux use the following commands

$ sudo apt update
$ sudo apt upgrade
$ sudo apt-get install python3-pip
```
```
For Mac OS use homebrew to install pip

$ brew install python3-pip
```

Next we will use the pip package manager to install the library. Make sure you have pip set up properly and you can access it through your terminal window.

```
(Windows)

$ pip install menousdb 

(Mac OS and Linux)

$ pip3 install menousdb
```

# Documentation
### Importing the module
To import the menousdb import simply use

```python
from menousdb import *
```

### Initializing the database
To create a database from scratch use:

```python
# Using the imported class from the import statement

db = MenousDB(
    url="http://localhost:5555/",
    key="YOUR API KEY",
    database="DATABASE"
)

# Checking if the database exists
if not db.checkDbExists():
    # If not create the database
    db.createDb()
```
### Checking if the database exists
```python
# isCreated is either True or False
isCreated = db.checkDbExists()
```
### Reading the entire database
To read the entire database we will use the readDb method. The readDb method returns a dictionary that can be converted to a dataframe. 

```python
data = db.readDb()
```

### Deleting the entire database
To delete the entire database we will use the deleteDb method.
```python
if db.checkDbExists():
    db.deleteDb()
else:
    print("Database not found")
```

### Creating a new table
To create a new table, the parameters are the name of the table and the attributes of the new table. The attributes parameter must be a list of strings.
```python
# Defining the table name and attributes
table_name = "test"
attributes = ["name", "age", "gender"]

# Creating a new table using the defined variable
db.createTable(table_name, attributes)
```

### Checking if a table exists
To check if a table exists you can use the following which will return  a boolean value of True or False.

```python
# Defining the table name
table_name = "test"
# Cheking the table exists
isCreate = db.checkTableExists(table_name)
```

### Inserting values into the database
To insert new values into the table you can use the following code. The parameter values must be a dictionary whose order of keys must exactly match the order of the attributes passed in the creation of the table.

```python
# Defining table name and values
table_name = test
values = {
    "name":"John Doe",
    "age":"15",
    "gender":"male"
}

db.insertIntoTable(
    table=table_name,
    values=values
)
```
### Selecting the entire table
To get the complete data of a table use the following code:
```python
table_name = "test"
# Getting all the data in the table
data = db.getTable(table_name)
```
### Selecting Values with conditions
To search for values with conditions you can use the following code. The parameters required are the table name and the conditions which will be a dictionary.

```python
table_name = "test"
conditions = {
    "name":"John Doe"
}

# Contains all the values where the name is John Doe
data = db.selectWhere(
    table= table_name,
    conditions=conditions
)
```

### Selecting columns
To select only specefic columns from the table you can use the following code. The parameters include the table name and a list of names of columns you want to select. 

```python
table_name = "test"
columns=["name","age"]

# contains all the column values
selectedData = db.selectColumns(table_name, columns)
```

### Selecting columns with conditions
To select columns with conditions you can use the following code. The parameters include the table name, the target columns and the conditions. conditions will be a dictionary and columns will be an array. 

```python
table_name="test"
columns=["name","age"]
conditions={"name":"John Doe"}

data = db.selectColumnsWhere(
    table_name,
    columns,
    conditions
)
```

### Updating values
To update the values in the table we need the conditions and the replacement values. The parameters are the table name, the conditions and the replacement values.

```python
table_name = "test"
conditions = {
    "name":"John Doe"
}
values = {
    "name":"William Smith"
}

# This will replace the value of every row where the 
# name is John Doe to William Smith
db.updateWhere(
    table=table_name,
    conditions=conditions,
    values=values
)
```

### Deleting values
To delete values from a table with conditions use the following code. The parameters are the table name and the conditions.

```python
table_name = "test"
conditions = {
    "name":"John Doe",
}
db.deleteWhere(
    table=table_name,
    conditions=conditions
)
```

### Deleting the entire table
To delete the entire table just use the deleteTable functions. Its only parameter is the table name.
```python
table_name="test"
db.deleteTable(table_name)
```

### Getting all the databases
To get a list of all the databases use the following code.
```python
databases = db.getDatabases()
```


