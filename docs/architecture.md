# Project Architecture

The project is divided into folders to keep everything clean.

src/
models/
work_item.py
task.py
member.py
factory.py
repositories/
task_repo.py
main.py
data/
tasks.json
docs/




### Description of the Layers

**Models:**  
Contain all the classes that describe Task, SubTask, WorkItem and TeamMember.

**Factory:**  
Creates Task or SubTask depending on input.

**Repository:**  
Reads and writes items into a JSON file. Also checks if an ID exists.

**main.py (Application Layer):**  
This is where user inputs are handled. The menu, validation and creation
of objects happen here.

### Flow Example (Creating a Task)

1. User picks “Create Task”
2. main.py checks for ID, title and priority
3. Task is created using WorkItemFactory
4. TaskRepository saves it into JSON

The system is simple but easy to extend if necessary.
