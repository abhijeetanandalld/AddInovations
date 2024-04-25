class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task number!")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
        else:
            print("Invalid task number!")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks yet!")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task['completed'] else "Not Completed"
                print(f"{i + 1}. {task['task']} - {status}")

def main():
    todo_list = TodoList()

    while True:
        print("\n==== TO-DO LIST ====")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added successfully!")
        elif choice == '2':
            if todo_list.tasks:
                index = int(input("Enter the task number to delete: ")) - 1
                todo_list.delete_task(index)
            else:
                print("No tasks to delete!")
        elif choice == '3':
            if todo_list.tasks:
                index = int(input("Enter the task number to mark as completed: ")) - 1
                todo_list.mark_completed(index)
            else:
                print("No tasks to mark as completed!")
        elif choice == '4':
            print("\n==== TASKS ====")
            todo_list.display_tasks()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()