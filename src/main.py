import logging
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.factory import WorkItemFactory
from src.models.member import TeamMember
from src.repositories.task_repo import TaskRepository

logging.basicConfig(level=logging.INFO, format='%(message)s')

def get_valid_input(prompt, error_msg="Input cannot be empty."):
    """Helper function to ensure non-empty input."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print(f"❌ {error_msg}")

def main():
    repo = TaskRepository()
    print("\n=== STRICT TASK MANAGER ===")

    while True:
        print("\n1. Create New Task")
        print("2. Create SubTask")
        print("3. Read All Tasks")
        print("4. Exit")
        
        choice = input("Select option: ").strip()

        if choice == "1":
            # --- 1. ID VALIDATION ---
            task_id = input("Enter Manual ID (or press Enter for Auto-Gen): ").strip()
            if task_id:
                # Check if ID is unique
                if repo.task_exists(task_id):
                    print(f"❌ Error: ID '{task_id}' already exists! Try again.")
                    continue # Skip to start of loop
            else:
                task_id = None # Let the class auto-generate

            # --- 2. TITLE VALIDATION (Null Safety) ---
            title = get_valid_input("Enter Task Title: ")

            # --- 3. PRIORITY VALIDATION (Strict Enums) ---
            valid_priorities = ["High", "Medium", "Low"]
            priority = ""
            while True:
                p_input = input("Enter Priority (High, Medium, Low): ").strip().capitalize()
                if p_input in valid_priorities:
                    priority = p_input
                    break
                print("❌ Invalid Priority! Must be High, Medium, or Low.")

            # --- SAVE ---
            try:
                # Pass 'uid' if the user provided one
                task = WorkItemFactory.create_item("task", title=title, priority=priority, uid=task_id)
                repo.save(task)
                logging.info(f"✅ Task '{title}' saved with ID: {task.id}")
            except Exception as e:
                logging.error(f"Error: {e}")

        elif choice == "2":
            # --- 1. PARENT ID VALIDATION (Referential Integrity) ---
            while True:
                parent_id = input("Enter Parent Task ID: ").strip()
                if not parent_id:
                    print("❌ Parent ID cannot be empty.")
                    continue
                
                if repo.task_exists(parent_id):
                    break # Found it, proceed
                else:
                    print(f"❌ Error: Task with ID '{parent_id}' does not exist. You cannot add a SubTask to a ghost.")

            # --- 2. SUBTASK ID VALIDATION ---
            sub_id = input("Enter Manual SubTask ID (or press Enter for Auto-Gen): ").strip()
            if sub_id and repo.task_exists(sub_id):
                 print(f"❌ Error: ID '{sub_id}' already exists!")
                 continue

            title = get_valid_input("Enter SubTask Title: ")

            try:
                sub = WorkItemFactory.create_item("subtask", title=title, parent_id=parent_id, uid=sub_id if sub_id else None)
                repo.save(sub)
                logging.info(f"✅ SubTask saved linked to Parent {parent_id}")
            except Exception as e:
                logging.error(f"Error: {e}")

        elif choice == "3":
            items = repo.get_all_raw()
            if not items:
                print("No tasks found.")
            else:
                for i in items:
                    print(f"[{i['type']}] {i['title']} (ID: {i['id']})")
                    if "priority" in i:
                        print(f"   - Priority: {i['priority']}")
                    if "parent_id" in i:
                        print(f"   - Parent: {i['parent_id']}")

        elif choice == "4":
            break

if __name__ == "__main__":
    main()