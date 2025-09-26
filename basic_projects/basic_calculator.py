# Basic Calculator Program

tasks = []

def show_tasks():
    print("\nYour Tasks")
    if not tasks:
        print("No task yet ")

        for i , t in enumerate(tasks, 1):
            print(f"{i}, {t}")

while True:
    print("\nOptions: [1] Add [2] Complete [3] Show [4] Exit")
    choice = input()
    if choice == "1":
        task = input("New Task: ")
        tasks.append(task)
        print("Task Added")

    elif choice == "2":
        show_tasks()
        num = int(input("Task number to complete"))
        if 0 < num <=len(tasks):
            tasks.pop(num-1)

            print("Task Completed")
        else:
            print("Invalid number")

    elif choice == "3":
        show_tasks()

    elif choice == "4":
        print("Good Bye! ")
        break
    
    
    else:
        print("Invalid Choice.")