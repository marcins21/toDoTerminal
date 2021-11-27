# Terminal To-Do List

#Showing Current Tasks
def showTasks(toDo):
        for i in range(len(toDo)):
                for j in range(5):
                        print(10*"",toDo[i][j], end=" ")
                print()

#Checking if user input is '1' or '2'
def validation(userInput):
        if userInput == '1' or userInput == '2':
                return 1
        else:
                return 0

#List of Tasks
toDo = []

#Welcome Message***
print("Welcome It's My To-Do Planner")
print("Your Tasks")
print("\n")
showTasks(toDo)


#Adding Task
end_of_Task = False
while True:
        # UserInput VALIDATION
        is_user_input_valid = False
        while is_user_input_valid == False:
                print("\n(1) Add new Task\n(2)Change Done Status")
                user_main_menu_choice = input("What You Wanna Do: ")
                if validation(user_main_menu_choice):
                        is_user_input_valid = True
                else:
                        print("\nWRONG ACTION\n")
                        is_user_input_valid = False

        #Adding Task
        if user_main_menu_choice == '1':
                task_user_input = input("Task: ")
                #FIRST TASK
                if toDo == []:
                        toDo.append([1 , "|", task_user_input, "|", False])
                #NEXT TASKS
                else:
                        toDo.append([toDo[len(toDo)-1][0]+1,"|",task_user_input,"|",False])
                showTasks(toDo)


        #Changing Done Status
        if user_main_menu_choice == '2':
                changingStatus_user_input = int(input("Which Task You wanna change To Done :"))
                if len(toDo) > 0:
                        #Changing False -> True
                        toDo[changingStatus_user_input-1][4] = True
                        print("\n")
                        showTasks(toDo)
                #Handling empty list of tasks
                else:
                        print("There is no tasks to change")











