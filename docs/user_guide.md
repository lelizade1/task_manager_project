# User Guide

## Running the Program
Make sure you have Python installed.  
Go to the project folder and run:

python src/main.py

If the data/ folder doesn’t exist, create it and add an empty tasks.json file.

## Menu Options

1. Create New Task  
2. Create SubTask  
3. Read All Tasks  
4. Exit  

### Creating a Task
You can enter an ID yourself or leave it empty to auto-generate.
Then you must write a title.
Priority must be one of: High, Medium, Low.

### Creating a SubTask
You must enter a valid existing Task ID.
You can also give your own SubTask ID or leave it empty.
A title is also required.

### Reading Tasks
This shows everything stored in tasks.json.

### Validation
- Title cannot be empty
- ID cannot be repeated
- SubTask must have an existing parent ID
- Priority only accepts 3 values

The program prints errors clearly if something is wrong.
