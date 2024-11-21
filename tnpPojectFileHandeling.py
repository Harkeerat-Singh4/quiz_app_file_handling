import random
import os
import time
import getpass

from time import sleep

userNameGlobal = ""
passwordGlobal = ''
quizWorking = 0
listForOption = ['a','b','c','d']

def clearScreen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def printWithDelay(string, delay=0.05):
    for letter in string:
        print(letter, end='', flush=True)  # Print without newline
        time.sleep(delay)
    print()  # Newline after the loop finishes

clearScreen() #For clearing the screen!!!

def save_user_data(username, password):
    with open('users.txt', 'a') as file:
        file.write(f"{username}:{password}\n")

##########################################################################33

def register():
    clearScreen()
    global passwordGlobal
    global userNameGlobal
    def rulesForUsername():
        print("\t\t\t\tRULES FOR CREATING A USERNAME::\n")
        print('''1. Username must be at least 8 characters long and can go up to 20 characters.
    \r2. First character must be a letter only.
    \r3. Username can contain digits.
    \r4. Username must not have any spaces between the words.
    \r5. Username must not have any special characters except underscores.''',end='\n\n')
    
    rulesForUsername()
    userName = input("Enter your Username: ") 
    userNameGlobal= userName
    letterFound = False

    while (letterFound != True):
        if len(userName) != 0 and userName[0].isalpha() == True and len(userName) >= 8 and len(userName) <= 20 and ' ' not in userName:
            for i in userName[1:]:
                if not i.isalnum():                                                  
                    if '_' == i:
                        letterFound = True
                    else: 
                        clearScreen()                           #to clr the screen
                        rulesForUsername()
                        print("\nPlease create Username as per the rules!\n")
                        userName = input("Enter Another Username: ")  
                        userNameGlobal = userName
                        break
            else:
                letterFound = True
                clearScreen()
                print("\nUsername is Successfully Created!")
        else:
            clearScreen()
            rulesForUsername()
            print("\nPlease create Username as per the rules!\n")
            userName = input("Enter Username: ")  
            userNameGlobal = userName
            
    def rulesForPassword():
        print("\n\t\t\t\t RULES FOR CREATING A PASSWORD::")
        print("""\n1. Password must at least be 8 characters long and can go up to 15 characters.
        \r2. Password must contain at least 1 upper-case character, 1 lower-case character, 1 special character and 1 digit also.""",end= '\n\n')
    
    rulesForPassword()
    
    password = getpass.getpass("Enter your password: ")
    passwordGlobal = password
    
    correctPassword = False
    upperCaseCondition = False
    lowerCaseCondition = False
    specialCharacterCondition = False
    digitCondition = False
    
    while correctPassword != True:
        if len(password) >= 8 and len(password) <= 15:
            for i in password:
                if i.isupper() == True:
                    upperCaseCondition = True
                elif i.islower() == True:
                    lowerCaseCondition = True
                elif i.isalnum() != True:
                    specialCharacterCondition = True
                elif i.isnumeric() == True:
                    digitCondition = True
            else: 
                if not (upperCaseCondition == True and lowerCaseCondition == True and specialCharacterCondition == True and digitCondition == True):
                    clearScreen()
                    rulesForPassword()
                    print("\nPlease create password according to the rules!\n")
                    correctPassword = False
                    upperCaseCondition = False
                    lowerCaseCondition = False
                    specialCharacterCondition = False
                    digitCondition = False
                    password = getpass.getpass("Enter another password: ")
                    passwordGlobal = password
                else:
                    clearScreen()
                    confirmingPassword = getpass.getpass("\nEnter your password again to confirm it: ")
                    if confirmingPassword == password:
                        clearScreen()
                        printWithDelay("\nYour Account is successfully created!",0.05)
                        sleep(1.5)
                        correctPassword = True
                        save_user_data(userNameGlobal, passwordGlobal)
                    else: 
                        clearScreen()
                        rulesForPassword()
                        print("\nPlease create password according to the rules!\n")
                        correctPassword = False
                        upperCaseCondition = False
                        lowerCaseCondition = False
                        specialCharacterCondition = False
                        digitCondition = False                        
                        password = getpass.getpass("Enter another password: ")
                        passwordGlobal = password
        else:
            clearScreen()
            rulesForPassword()
            print("\nPlease create password according to the rules!\n")
            correctPassword = False
            upperCaseCondition = False
            lowerCaseCondition = False
            specialCharacterCondition = False
            digitCondition = False            
            password = getpass.getpass("Enter another password: ")
            passwordGlobal = password

######################################################################################3

def load_user_data():
    users = {}
    try:
        with open('users.txt', 'r') as file:
            for line in file:
                username, password = line.strip().split(':')
                users[username] = password
    except FileNotFoundError:
        pass
    return users

##############################################################################################333

def login():
    users = load_user_data()
    global userNameGlobal
    global passwordGlobal
    # count = 0
    clearScreen()
    print("\t\t\t\tLOGIN TO YOUR ACCOUNT:: ")
    loginUsername = input("\nEnter your Username: ")
    loginPassword = getpass.getpass("Enter your password: ")
    
    if loginUsername in users and users[loginUsername] == loginPassword:
        clearScreen()
        print("\n\nYOU HAVE SUCCESSFULLY LOGGED IN YOUR ACCOUNT!!!")
        #print('I am working121') # exp
        return loginUsername
    else:
# ##############################################################
#     print(userNameGlobal)
#     print(passwordGlobal)
#     sleep(2)
# ##############################################################
    # if count < 0:
        while not (loginUsername in users and users[loginUsername] == loginPassword):
            clearScreen()
            print("\nNo such account exist in the database!")
            while(1):
                choice= input('\n1. Want to register?\n2. Enter another Username and password\n\nEnter Your Choice: ')
                if choice == '1' or choice.lower() == 'a':
                    register()
        # ###############################################################                
        #             print(userNameGlobal)
        #             print(passwordGlobal)
        #             sleep(2)
        # #################################################################
                    login()
                    # count =+ 1
                    # break
                    return
                elif choice == '2' or choice.lower() == 'b':
                    clearScreen()
                    loginUsername = input("\nEnter your Username: ")
                    loginPassword = getpass.getpass("Enter your password: ")
                    break
                else:
                    clearScreen()
                    continue
                # break
        else: 
            clearScreen()
            print("\n\nYOU HAVE SUCCESSFULLY LOGGED IN YOUR ACCOUNT!!!")
            #############################
            #print('i am working')#exp
            return loginUsername

# def quiz():
#     clearScreen()
#     global quizWorking
#     quizWorking += 1
#     def python():
#         dic_py={'What is the correct way to define a variable in Python?\na) variable = value\nb) value = variable\nc) var: value\nd) define variable = value':'a',
#                         'Which data type is used to represent a sequence of characters in Python?\na) int\nb) float\nc) str\nd) bool':'c',
#                         'How do you comment a single line in Python?\na) // This is a comment\nb) # This is a comment\nc) /* This is a comment */\nd) ; This is a comment':'b',
#                         'Which operator is used for integer division in Python?\na) /\nb) //\nc) %\nd) **':'b',
#                         'How do you create an if-else statement in Python?\na) if condition: statement1\nb) if condition: statement1 else: statement2\nc) if condition then statement1\nd) if condition { statement1; }':'b',
#                         'What is the purpose of a while loop in Python?\na) To execute a block of code repeatedly until a condition becomes false.\nb) To execute a block of code a fixed number of times.\nc) To create functions.\nd) To define variables.':'a',
#                         'How do you define a function in Python?\na) function name(): statements\nb) def name(): statements\nc) create function name(): statements\nd) function name(arguments): statements':'b',
#                         'What is the purpose of the return statement in a Python function?\na) To define the function name.\nb) To end the function execution.\nc) To return a value from the function.\nd) To take input arguments for the function.':'c',
#                         'How do you import a module named mymodule in Python?\na) import mymodule\nb) include mymodule\nc) use mymodule\nd) load mymodule':'a',
#                         'How do you access the first element of a list named my_list in Python?\na) my_list[0]\nb) my_list.first()\nc) my_list(0)\nd) my_list[1]':'a',
#                         'How do you get input from the user in Python?\na) input()\nb) get_input()\nc) read_input()\nd) input_value()':'a',
#                         'How do you print a message to the console in Python?\na) print()\nb) display()\nc) show()\nd) output()':'a',
#                         'What is the purpose of a try-except block in Python?\na) To handle errors that may occur during program execution.\nb) To define functions.\nc) To create loops.\nd) To import modules.':'a',
#                         'What is the difference between a list and a tuple in Python?\na) Lists are mutable, while tuples are immutable.\nb) Lists are immutable, while tuples are mutable.\nc) Both lists and tuples are mutable.\nd) Both lists and tuples are immutable.':'a',
#                         'How do you create a set in Python?\na) using curly braces\nb) using square brackets []\nc) using parentheses ()\nd) using the set() function':'a',
#                         'What is the purpose of a dictionary in Python?\na) To store a sequence of elements.\nb) To store key-value pairs.\nc) To store a set of unique elements.\nd) To define functions.':'b',
#                         'What is a class in Python?\na) A blueprint for creating objects.\nb) A collection of functions.\nc) A data type.\nd) A variable.':'a',
#                         'What is a module in Python?\na) A collection of functions and classes.\nb) A data type.\nc) A variable.\nd) An object.':'a',
#                         'What is a package in Python?\na) A collection of modules.\nb) A data type.\nc) A variable.\nd) An object.':'a',
#                         'How do you import the math module in Python?\na) import math\nb) include math\nc) use math\nd) load math':'a'
#                         } 
#         count=0
#         i = 1
#         li=random.sample(list(dic_py.keys()),5)
#         for key in li:
#             while True: 
#                 forBreaking= 0
#                 print(f'{i}. {key}')
#                 i += 1
#                 res=input("Enter your answer: ")
#                 print()
#                 if dic_py[key]==res.lower():
#                     print("Correct\n")
#                     count+=1
#                     break
#                 else:
#                     for option in listForOption:
#                         if res.lower() in listForOption:
#                             print("Incorrect\n")
#                             forBreaking = 1
#                             break
#                     else:
#                         print("Invalid Input!\n")
#                         i -= 1
#                     if forBreaking == 1:
#                         break
#         else: 
#             # clearScreen() 
#             print(f'\nYou Got {count}/5')
#         if count>=3:
#             print(f"\n\nCongratulations {userNameGlobal}, You have PASSED the QUIZ!!!")
#         else:
#             print(f"\n\nSorry {userNameGlobal}, You have FAILED the QUIZ!!!\n")
            
#     def cpp():
#         dic_cpp={'What is the correct syntax to declare a variable in C++?\na) variable = value\nb) value = variable\nc) var: value\nd) datatype variable_name;':'d',
#                 'Which data type is used to represent whole numbers in C++?\na) int\nb) float\nc) char\nd) string':'a',
#                 'What is the difference between int and long in C++?\na) int is used for smaller integers, long is used for larger integers\nb) int is used for larger integers, long is used for smaller integers\nc) There is no difference between int and long\nd) int is used for floating-point numbers, long is used for integers':'a',
#                 'How do you declare a constant variable in C++?\na) const variable_name = value;\nb) variable_name const = value;\nc) constant variable_name = value;\nd) define variable_name = value;':'a',
#                 'Which operator is used for logical AND in C++?\na) &&\nb) ||\nc) !\nd) ^':'a',
#                 'How do you increment the value of a variable x by 1 in C++?\na) x++\nb) x--\nc) ++x\nd) All of the above':'d',
#                 'How do you create an if-else statement in C++?\na) if (condition) { statement1; } else { statement2; }\nb) if condition then statement1 else statement2\nc) if condition: statement1 else: statement2\nd) if (condition) statement1 else statement2':'a',
#                 'What is the purpose of the break statement in a loop?\na) Exits the loop\nb) Continues to the next iteration\nc) Declares a new variable\nd) Defines a function':'a',
#                 'What is the purpose of the continue statement in a loop?\na) Exits the loop\nb) Continues to the next iteration\nc) Declares a new variable\nd) Defines a function':'b',
#                 'How do you define a function in C++?\na) function name() { statements; }\nb) def name(): statements\nc) void name() { statements; }\nd) function name(arguments) { statements; }':'c',
#                 'What is the purpose of the return statement in a function?\na) Exits the function\nb) Returns a value from the function\nc) Declares a new variable\nd) Defines a function':'b',
#                 'What is a pointer in C++?\na) A variable that stores the address of another variable\nb) A constant value\nc) A data type\nd) A function':'a',
#                 'How do you dereference a pointer in C++?\na) Using the * operator\nb) Using the & operator\nc) Using the -> operator\nd) Using the [] operator':'a',
#                 'How do you declare an array in C++?\na) array name[size];\nb) name array[size];\nc) size array name;\nd) array[size] name;':'a',
#                 'What is the index of the first element in a C++ array?\na) 0\nb) 1\nc) -1\nd) The size of the array':'a',
#                 'How do you access the third element of an array named arr in C++?\na) arr[3]\nb) arr(3)\nc) arr.3\nd) *arr[3]':'a',
#                 'What is a string in C++?\na) An array of characters\nb) A data type\nc) A function\nd) A constant value':'a',
#                 'What is a class in C++?\na) A blueprint for creating objects\nb) A data type\nc) A function\nd) A constant value':'a',
#                 'How do you define a class in C++?\na) class name { };\nb) struct name { };\nc) define name { };\nd) class name() { };':'a',
#                 'What is an object in C++?\na) An instance of a class\nb) A data type\nc) A function\nd) A constant value':'a',
#                 }
#         count=0
#         i = 1
#         li=random.sample(list(dic_cpp.keys()),5)
#         for key in li:
#             while True: 
#                 forBreaking= 0
#                 print(f'{i}. {key}')
#                 i += 1
#                 res=input("Enter your answer: ")
#                 print()
#                 if dic_cpp[key]==res.lower():
#                     print("Correct\n")
#                     count+=1
#                     break
#                 else:
#                     for option in listForOption:
#                         if res.lower() in listForOption:
#                             print("Incorrect\n")
#                             forBreaking = 1
#                             break
#                     else:
#                         print("Invalid Input!\n")
#                         i -= 1
#                     if forBreaking == 1:
#                         break
#         else: 
#             # clearScreen() 
#             print(f'\nYou Got {count}/5')
#         if count>=3:
#             print(f"\n\nCongratulations {userNameGlobal}, You have PASSED the QUIZ!!!")
#         else:
#             print(f"\n\nSorry {userNameGlobal}, You have FAILED the QUIZ!!!\n")
            
#     def java():
#         dic_java={'What is the default data type for integer literals in Java?\na) int\nb) long\nc) short\nd) byte':'a',
#                 'Which data type is used to represent a single character in Java?\na) char\nb) string\nc) byte\nd) boolean':'a',
#                 'How do you declare a constant variable in Java?\na) final variable_name = value;\nb) constant variable_name = value;\nc) const variable_name = value;\nd) define variable_name = value;':'a',
#                 'Which operator is used for logical OR in Java?\na) &&\\nb) ||\nc) !\nd) ^':'b',
#                 'How do you increment the value of a variable x by 1 in Java?\na) x++\nb) x--\nc) ++x\nd) All of the above':'d',
#                 'How do you create an if-else statement in Java?\na) if (condition) { statement1; } else { statement2; }\nb) if condition then statement1 else statement2\nc) if condition: statement1 else: statement2\nd) if (condition) statement1 else statement2':'a',
#                 'What is the purpose of the break statement in a loop?\na) Exits the loop\nb) Continues to the next iteration\nc) Declares a new variable\nd) Defines a function':'a',
#                 'What is the purpose of the continue statement in a loop?\na) Exits the loop\nb) Continues to the next iteration\nc) Declares a new variable\nd) Defines a function':'b',
#                 'How do you define a function in Java?\na) function name() { statements; }\nb) def name(): statements\nc) void name() { statements; }\nd) function name(arguments) { statements; }':'c',
#                 'What is the purpose of the return statement in a function?\na) Exits the function\nb) Returns a value from the function\nc) Declares a new variable\nd) Defines a function':'b',
#                 'How do you declare an array in Java?\na) array name[size];\nb) name array[size];\nc) size array name;\nd) array[size] name;':'a',
#                 'What is the index of the first element in a Java array?\na) 0\nb) 1\nc) -1\nd) The size of the array':'a',
#                 'How do you access the third element of an array named arr in Java?\na) arr[3]\nb) arr(3)\nc) arr.3\nd) *arr[3]':'a',
#                 'What is a class in Java?\na) A blueprint for creating objects\nb) A data type\nc) A function\nd) A constant value':'a',
#                 'How do you define a class in Java?\na) class name { };\nb) struct name { };\nc) define name { };\nd) class name() { };':'a',
#                 'What is an object in Java?\na) An instance of a class\nb) A data type\nc) A function\nd) A constant value':'a',
#                 'How do you create an object of a class in Java?\na) class_name object_name;\nb) object_name = class_name;\nc) new class_name;\nd) create object_name':'a',
#                 'What is the purpose of the this keyword in Java?\na) Points to the current object\nb) Points to the base class\nc) Points to the derived class\nd) Points to the function':'a',
#                 'Which keyword is used to inherit properties from a base class in Java?\na) extends\nb) inherits\nc) public\nd) implements':'a',
#                 }
#         count=0
#         i = 1
#         li=random.sample(list(dic_java.keys()),5)
#         for key in li:
#             while True: 
#                 forBreaking= 0
#                 print(f'{i}. {key}')
#                 i += 1
#                 res=input("Enter your answer: ")
#                 print()
#                 if dic_java[key]==res.lower():
#                     print("Correct\n")
#                     count+=1
#                     break
#                 else:
#                     for option in listForOption:
#                         if res.lower() in listForOption:
#                             print("Incorrect\n")
#                             forBreaking = 1
#                             break
#                     else:
#                         print("Invalid Input!\n")
#                         i -= 1
#                     if forBreaking == 1:
#                         break
#         else: 
#             # clearScreen() 
#             print(f'\nYou Got {count}/5')
#         if count>=3:
#             print(f"\n\nCongratulations {userNameGlobal}, You have PASSED the QUIZ!!!")
#         else:
#             print(f"\n\nSorry {userNameGlobal}, You have FAILED the QUIZ!!!\n")
            
            
#     wantToContinue = True

#     while wantToContinue == True:
#         clearScreen()
#         print('\n\t\t\t\tAttempt the Quiz for::\n\n1. PYTHON\n2. C++\n3. JAVA')
#         choice = input("\nEnter your choice: ")

#         if choice == '1' or choice.lower() == 'python' or choice.lower() == 'a': 
#             clearScreen()
#             python()
#         elif choice == '2' or choice.lower() == 'c++' or choice.lower() == 'cpp' or choice.lower() == 'b':
#             clearScreen()
#             cpp()
#         elif choice == '3' or choice.lower() == 'java' or choice.lower() == 'c':
#             clearScreen()
#             java()
#         else: 
#             clearScreen()
#             print("\nINVALID OPTION!")
#             continue
#         while(True):
#             choice = input("\n\nDo you wish to continue?\n1. Yes\n2. No\n\nYour Answer: ")
#             if choice.lower() == "yes" or choice == '1' or choice.lower() == 'a' or choice.lower() == 'y':
#                 break
#             elif choice.lower() == 'no' or choice == '2' or choice.lower() == 'b' or choice.lower() == 'n':
#                 print("\nThank You for attempting the Quiz!!!")
#                 wantToContinue = False
#                 break
#             else:
#                 clearScreen()
#                 print("\nInvalid Input!")
#                 continue

# Function to load quiz data from file
def loadQuizData(filename):
    quizzes = {}
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            question = ""
            options = []
            answer = ""
            for line in lines:
                line = line.strip()
                if line:
                    if not question:
                        question = line
                    elif len(options) < 4:
                        options.append(line)
                    else:
                        answer = line
                        quizzes[question] = (options, answer)
                        question = ""
                        options = []
                        answer = ""
    except FileNotFoundError:
        clearScreen()
        print(f"File '{filename}' not found.")
    except Exception as e:
        clearScreen()
        print(f"Error loading quiz data: {e}")
    return quizzes

# Function to conduct the quiz
def takeQuiz(username, subject, quizzes):
    try:
        score = 0
        questions = list(quizzes.items())
        random.shuffle(questions)
        selectedQuestions = questions[:5]

        for question, (options, correctAnswer) in selectedQuestions:
            while True:
                print(question)
                for option in options:
                    print(option)
                answer = input("Enter your answer (a, b, c, d): ")
                print('\n')
                if answer in ['a', 'b', 'c', 'd']:
                    break
                else:
                    clearScreen()
                    print("Invalid input. Please enter one of the options: a, b, c, d.")
            if answer == correctAnswer:
                score += 1
        clearScreen()
        print(f"You scored {score} out of 5")
        saveResult(username, subject, score, 5)
    except Exception as e:
        clearScreen()
        print(f"Error during quiz: {e}")

# Function to save quiz result
def saveResult(username, subject, score, total):
    try:
        with open('results.txt', 'a') as file:
            file.write(f"{username}:{subject}:{score}/{total}\n")
    except Exception as e:
        clearScreen()
        print(f"Error saving result: {e}")

# Function to view user results
def viewResults(username):
    try:
        with open('results.txt', 'r') as file:
            results = [line.strip() for line in file if line.startswith(username)]
        if results:
            clearScreen()
            print(f"Results for {username}:")
            print('\n')
            for result in results:
                print(result)
            else:
                print('\n\n')
        else:
            clearScreen()
            print("No results found for the user.")
    except FileNotFoundError:
        clearScreen()
        print("No results found.")
    except Exception as e:
        clearScreen()
        print(f"Error loading results: {e}")
        
def exit():
    clearScreen()
    if quizWorking > 0:
        print('\nThank You!, For Attempting the Quiz.')
    else:
        print('\nThank You!, For visiting us.\n')
    pass

def frontPage():
    clearScreen()
    subjects = {
        "1": "Python",
        "2": "C++",
        "3": "Java"
    }
    subjectFiles = {
        "1": "pythonQuiz.txt",
        "2": "cppQuiz.txt",
        "3": "javaQuiz.txt"
    }
    
    loggedInUser = None

    print("\n\t\t\t\tWelcome to the Quiz Application!!!")
    choice = input("\n1. Register\n2. login\n3. Exit\n\nEnter your choice: ")
    
    if choice == '1' or choice.lower() == 'a' or choice.lower() == 'register':
        register()
        # print(userNameGlobal)
        # print(passwordGlobal)
        # sleep(2)
        frontPage()
        
    elif choice == '2' or choice.lower() == 'b' or choice.lower() == 'login':
        # username = login()
        # print(f'\n\nWelcome, {username}!\n')
            loggedInUser = login()
            if loggedInUser:
                    print(f"\nWelcome, {loggedInUser}!\n")
                    while True:
                        print("1. Take Quiz")
                        print("2. View Previous Results")
                        print("3. Logout")
                        subChoice = input("Enter your choice: ")
                        if subChoice == '1':
                            clearScreen()
                            print("Choose a subject for the quiz:")
                            for key, subject in subjects.items():
                                print(f"{key}. {subject}")
                            subjectChoice = input("Enter your choice: ")
                            clearScreen()
                            if subjectChoice in subjectFiles:
                                filename = subjectFiles[subjectChoice]
                                quizzes = loadQuizData(filename)
                                if quizzes:
                                    takeQuiz(loggedInUser, subjects[subjectChoice], quizzes)
                                else:
                                    clearScreen()
                                    print("No quizzes found.")
                            else:
                                clearScreen()
                                print("Invalid choice. Please try again.")
                        elif subChoice == '2':
                            viewResults(loggedInUser)
                        elif subChoice == '3':
                            clearScreen()
                            print("Logging out...")
                            frontPage()
                            break
                        else:
                            clearScreen()
                            print("Invalid choice. Please try again.")
            # print(f'\nWelcome, {user}!')
            # while True:
            #     # clearScreen()
            #     option = input('\nWant to attempt the Quiz?\n1. Yes\n2. No\n\nEnter your choice: ')
            #     if option == '1' or option.lower() == 'a' or option.lower() == 'y' or option.lower() == 'yes':
            #         # print("working 1st option")
            #         quiz()
            #         frontPage()
            #         break
            #     elif option == '2' or option.lower() == 'b' or option.lower() == 'n' or option.lower() == 'no':
            #         # print("working 2nd option")
            #         frontPage()
            #         break
            #     else:
            #         # print("else is working")
            #         clearScreen()
            #         continue
            # print("while finished")
            # frontPage()
        
    elif choice == '3' or choice.lower() == 'c' or choice.lower() == 'exit':
        exit()
        # quiz()
        # frontPage()
    # elif choice == '4' or choice.lower() == 'd' or choice.lower() == 'exit':
    #     exit()

    else:
        frontPage()
###############################################################################3
# IT MUST BE CALLED IF WE ARE SHOWING THIS PROGRAM
frontPage()