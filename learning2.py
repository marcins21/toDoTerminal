# Terminal To-Do List
import os


#Showing Current Tasks
def showTasks(toDo):
        os.system('cls')
        print("Welcome It's My To-Do Planner")
        print("\nTASKS:")
        for i in range(len(toDo)):
                for j in range(5):
                        print(10*"",toDo[i][j], end=" ")
                print()

#Refreshing Tasks Index'es After deleting Task
def refrsh_Tasks_index(toDo):
        for i in range(len(toDo)):
                for j in range(1):
                        toDo[i][j] = i+1

#MAIN MENU VALIDATION (Checking if user input is Valid)
def validation(userInput):
        if userInput == '1' or userInput == '2' or userInput == '3' or userInput == '4':
                return 1
        else:
                return 0

#List of Tasks
toDo = []

#Welcome Message***
print("Welcome It's My To-Do Planner")

showTasks(toDo)
space_index = 40
main_menu = "\n"+space_index*" "+"|(1) Add new Task"+"\n"+space_index*" "+"|(2)Delete Task BETA"+"\n"+space_index*" "+"|(3)Change Done Status"\
            +"\n"+space_index*" "+"|(4)Edit Task BETA\n"

#Adding Task
end_of_Task = False
while True:

        # UserInput VALIDATION
        is_user_input_valid = False
        while is_user_input_valid == False:

                print(" "*10,main_menu)
                user_main_menu_choice = input("What You Wanna Do: ")
                if validation(user_main_menu_choice):
                        is_user_input_valid = True
                else:
                        showTasks(toDo)
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


        #Deleting Task
        if user_main_menu_choice == '2':
                try:
                        delete_task_input = int(input("Which Task You Wanna Delete: "))
                        toDo.pop(delete_task_input-1)
                        refrsh_Tasks_index(toDo)
                        showTasks(toDo)
                #Handling Wrong Input
                except ValueError:
                        showTasks(toDo)
                        print("You Didn't Enter Integer")

                except IndexError:
                        showTasks(toDo)
                        print("Wrong Index")


        #Changing Done Status
        if user_main_menu_choice == '3':
                try:
                        changingStatus_user_input = int(input("Which Task You wanna change To Done :"))
                        if len(toDo) > 0:
                                #Changing False -> True
                                toDo[changingStatus_user_input-1][4] = True
                                print("\n")

                                showTasks(toDo)
                        #Handling empty list of tasks
                        else:
                                showTasks(toDo)
                                print("\nThere is no tasks to change".capitalize())

                #Handling Wrong Input
                except ValueError:
                        showTasks(toDo)
                        print("You Didn't Enter Integer")

                except IndexError:
                        showTasks(toDo)
                        print("Wrong Index")


        #Edit Feature
        if user_main_menu_choice == '4':
                try:
                        edit_task_user_input = int(input("\nWhich Task You Wanna Edit: "))
                        print("\nYour Current Task: \n",toDo[edit_task_user_input-1][2])
                        edited_input = input("\nEdit your Task: ")

                        #Editing Task
                        toDo[edit_task_user_input- 1][2] = edited_input

                        showTasks(toDo)

                #Handling Wrong Input
                except ValueError:
                        showTasks(toDo)
                        print("You Didn't Enter Integer")
                except IndexError:
                        showTasks(toDo)
                        print("Wrong Index")

















