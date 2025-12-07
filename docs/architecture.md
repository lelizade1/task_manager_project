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
services/
  task_service.py
strategies/
  sorting.py
utils/
  logger.py
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

**Services:**
The business logic layer. `TaskService` orchestrates validation, object creation, and repository interactions. It enforces rules like unique IDs and valid priorities.

**Strategies:**
Implement sorting algorithms (by Title or Priority) to keep logic decoupled from the service.

**Utils:**
Helpers like `logger.py` for centralized logging and error tracking.

**main.py (Application Layer):**  
This is where user inputs are handled. The menu, validation and creation of objects happen here, delegating actual work to the **Service** layer.

### Flow Example (Creating a Task)

1. User picks “Create Task” in `main.py`
2. Input is gathered (Title, Priority)
3. `TaskService` validates input (e.g., checks priority enum)
4. `WorkItemFactory` creates the object
5. `TaskRepository` saves it into `data/tasks.json`
6. `Logger` records the action

The system is simple but easy to extend if necessary.
