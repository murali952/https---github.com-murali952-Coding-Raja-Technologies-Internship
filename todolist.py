class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("Your to-do list is empty.")

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1] += " (Completed)"
            print("Task marked as completed!")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task deleted successfully!")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.complete_task(task_index)
        elif choice == "4":
            task_index = int(input("Enter the index of the task to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
