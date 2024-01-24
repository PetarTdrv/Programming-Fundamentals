tasks = []
lenght = 0

while True:
    print("\n===== To-Do List Menu =====")
    print("1. Add a new task")
    print("2. Mark a task as completed")
    print("3. View all tasks")
    print("4. Quit")

    enter_choice = int(input("\nEnter your choice (1-4): "))

    lenght = len(tasks)
    lenght -= 1

    if enter_choice == 1:
        enter_task = input("Enter a task description: ")
        tasks.append(enter_task)
        print(f'Task "{enter_task}" added successfully!')
    elif enter_choice == 2:
        completed_task = int(input("Enter the index of the task to mark as completed: "))
        if 0 <= completed_task <= lenght:
            tasks[completed_task] = f"[completed] {tasks[completed_task]}"
            print("Task marked as completed.")
    elif enter_choice == 3:
        print(tasks)
    elif enter_choice == 4:
        print("Exiting the program. Goodbye!")
        break
