from studnts import add
from studnts import search_student
from studnts import show_students
from studnts import average_student
from studnts import statistics
from studnts import random_student
from studnts import Top_students
is_running=True
while is_running:
    print("┌────────────────────────┐")
    print("│   STUDENT MANAGEMENT   │")
    print("│────────────────────────│")
    print("│   1 - Add student      │")
    print("│   2 - Show Students    │")
    print("│   3 - Search Student   │")
    print("│   4 - Calculate average│")
    print("│   5 - Show Statistics  │")
    print("│   6 - Random Student   │")
    print("│   7 - Exit             │")
    print("│   8 - Top student      │")
    print("│────────────────────────│")
    choice=int(input("  Enter your number : "))

    if choice == 1:
        print("│────────────────────────────────┐")
        print("│     Yes , Add your student     │")
        print("│────────────────────────────────│")
        name_user=input("│  Name of student : ")
        age_user=int(input("│  Age of student : "))
        print("│────────────────────────────────┐")
        print("│ Now you must enter the 3 grades│")
        print("│────────────────────────────────│")
        grade_1=int(input("│  First grade : "))
        grade_2=int(input("│  Second grade : "))
        grade_3=int(input("│  Third grade : "))
        add(name_user, [grade_1, grade_2, grade_3], age_user)
        print("│────────────────────────────────┐")
        print("│       Succesfully added        │")
        print("│────────────────────────────────│")
    elif choice == 2:
        print("│────────────────────────────────┐")
        print("│           Students             │")
        print("│────────────────────────────────│")    
        show_students()
    elif choice == 3:
        print("│────────────────────────────────┐")
        print("│         Search Station         │")
        print("│────────────────────────────────│")  
        search_student()
    elif choice == 4:
        print("│────────────────────────────────┐")
        print("│       Average Calculator       │")
        print("│────────────────────────────────│")          
        average_student()
    elif choice == 7 :
        is_running = False
    elif choice == 5:
        statistics()
    elif choice == 6:
        random_student()
    elif choice == 8:
        Top_students()
    else:
        print("Invzlid command 🛑")