class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def view_tasks(self):
        if self.tasks:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. [{'X' if task['completed'] else ' '}] {task['task']}")
        else:
            print("No tasks in the list.")

    def mark_completed(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task deleted.")
        else:
            print("Invalid task index.")


def main():
    todo_list = ToDoList()
    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_completed(index)
        elif choice == '4':
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
