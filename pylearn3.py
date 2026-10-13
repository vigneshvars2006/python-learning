todos = []

while True:
    user_action = input("choose your action(add,show,exit): ")

    match user_action:
        case "add":
            todo = input("Enter your new to-do: ")
            todos.append(todo)

        case "show":
            print(todos)

        case "exit":
            print("bye!")
            break
            



