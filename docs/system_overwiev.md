# System Overview

This project is a small Task Management System that works from the terminal. 
The main idea is to let the user create tasks and subtasks and store them in 
a JSON file. It is a simple system, but it still uses OOP ideas like 
inheritance, abstract classes, encapsulation and so on.

The user can:
- Create a new Task
- Create a SubTask connected to a parent task
- View all tasks saved in the system

IDs can be written manually or automatically generated. SubTasks always require
a valid parent task ID. Everything is saved into `data/tasks.json`.

### Main Classes
- WorkItem (abstract)
- Task
- SubTask
- TeamMember
- WorkItemFactory (creates Task/SubTask)
- TaskRepository (saving, reading, validation)

The program is run through `main.py` which shows a simple menu in the terminal.
