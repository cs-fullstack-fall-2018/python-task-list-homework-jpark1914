

class UserList():
    def __init__(self, task = ["Grcoeries"]):
        self.task = task

def main():
    person = UserList()
    print("Hola!")
    while True:
        taskList = input("What would you like to do? \n 'Add' \n 'Remove' \n 'Check' \n 'End'").lower()
        if taskList != "add" and taskList!= "remove" and taskList != "check" and taskList!= "end":
            print("Please enter 'Add', 'Remove', or 'Check'")
            continue
        elif taskList == 'add':
            person.task.append(input("What would you like to add?"))
            continue
        elif taskList == 'remove':
            person.task.remove(input("What would you like to remove?"))
            continue
        elif taskList == 'check':
            for x in person.task:
                print(x)
            continue
        elif taskList == 'end':
            break
        else:
            print("Error occurred, program will now quit out of frustration")
            break

    my_file = open("python_TaskList.txt","w+")

    for x in person.task:
        print(x)
        my_file.write(x)

if __name__ == '__main__':
    main()
