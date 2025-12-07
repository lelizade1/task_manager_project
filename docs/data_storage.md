# Data Storage Description

The project uses a simple JSON file called `tasks.json` which is inside 
the data/ folder. All tasks and subtasks are stored as dictionaries.

### What gets saved for each item

Common fields:
- id
- title
- status
- type (Task or SubTask)

Extra fields:
- priority (only for Task)
- parent_id (only for SubTask)

### Example of the JSON content

 {
        "id": "23",
        "title": "python",
        "status": "Todo",
        "type": "Task",
        "priority": "High"
}




