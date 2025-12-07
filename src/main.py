import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.services.task_service import TaskService
from src.strategies.sorting import SortByPriority, SortByTitle
from src.utils.logger import setup_logger

logger = setup_logger()

def print_menu():
    print("\n=== SPRINT 2: TASK MANAGER ===")
    print("1. Create Task")
    print("2. Create SubTask")
    print("3. View Tasks (Unsorted)")
    print("4. View Tasks (Sorted by Strategy)")
    print("5. Update Task Status")
    print("6. Delete Task")
    print("7. Exit")
    print("==============================")

def main():
    service = TaskService()
    
    while True:
        print_menu()
        choice = input("Select option: ").strip()

        try:
            if choice == "1":
                # --- STRICT INPUT VALIDATION ---
                title = ""
                while not title:
                    title = input("Title: ").strip()
                    if not title: print("Title cannot be empty.")

                priority = ""
                while True:
                    p_input = input("Priority (High/Medium/Low): ").strip().capitalize()
                    if p_input in ["High", "Medium", "Low"]:
                        priority = p_input
                        break
                    print("Invalid! Please type High, Medium, or Low.")

                uid = input("Custom ID (Optional): ").strip() or None
                
                # Call Service
                service.create_task(title, priority, uid)
                print("Task Created.")

            elif choice == "2":
                parent = input("Parent ID: ")
                title = input("Title: ")
                service.create_subtask(title, parent)
                print("SubTask Created.")

            elif choice == "3":
                tasks = service.get_tasks()
                for t in tasks:
                    print(f"[{t['type']}] {t['title']} (ID: {t['id']}) - {t.get('priority', '')}")

            elif choice == "4":
                print("Sort Strategy: (P)riority or (T)itle?")
                s_choice = input("> ").lower()
                
                strategy = None
                if s_choice == 'p':
                    strategy = SortByPriority()
                elif s_choice == 't':
                    strategy = SortByTitle()
                
                if strategy:
                    tasks = service.get_tasks(sort_strategy=strategy)
                    print("\n--- Sorted List ---")
                    for t in tasks:
                        print(f"[{t['type']}] {t['title']} - {t.get('priority', 'N/A')}")
                else:
                    print("Invalid strategy selected.")

            elif choice == "5":
                tid = input("Task ID to Update: ")
                status = input("New Status (Todo/Done): ")
                service.update_task_status(tid, status)
                print("Task Updated.")

            elif choice == "6":
                tid = input("Task ID to Delete: ")
                service.delete_task(tid)
                print("Task Deleted.")

            elif choice == "7":
                print("Goodbye!")
                break
        
        except ValueError as e:
            logger.error(f"Validation Error: {e}")
            print(f"Error: {e}")
        except Exception as e:
            logger.critical(f"System Error: {e}")
            print("An unexpected error occurred.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting safely...")