import random
students=[]
def add(name, grades, age):
    student = {"name" : name ,
               "grades" : grades,
               "age" : age }
    students.append(student)

add("Adam", [14, 17, 15], 16)
add("Youssef", [17, 18, 19], 17)
add("Omar", [12, 20, 14], 17)
add("Ahmed", [14,15,17], 16)
add("Hamza", [12,11,10], 16)
add("Anas", [18,18,19], 16)
add("Ayoub", [17,15,12], 16)
add("Bilal", [15,16,13], 15)
add("Asia", [20,12,18], 17)
add("Maryam", [13,15,18], 16)
add("Samia", [14,19,20], 16)
add("Zakaria", [16,18,15], 16)
add("Samir", [19,15,20], 16)
add("Yassir", [11,10,12], 16)
add("Mehdi", [16,16,18], 17)
add("Soufiane", [19,15,16], 15)
add("Salma", [16,11,19], 17)
add("Faris", [9,12,14], 16)
add("Nora", [13,15,11], 16)
add("Amine", [15,7,18], 16)
add("Hicham", [12,11,12], 16)
add("Taha", [18,13,18], 16)
add("Marouane", [19,13,17], 16)
add("Reda", [18,18,16], 16)
add("Rim", [19,15,16], 17)
add("Chihab", [17,13,19], 17)
add("Nail", [11,10,11], 17)
add("Sara", [6,17,13], 18)
add("Mohammed", [19,18,17], 15)
def show_students():
    print("───────────────────────────────────────────────")
    for index, student in enumerate(students):
        
        print(f"│{index+1}/ {student["name"]} - age is {student["age"]} │")
        print(f"│ grades:  {student["grades"]}│")
        print("───────────────────────────────────────────────")

def search_student():
    name=input("Enter a student : ").capitalize()
    found = False
    for student in students:
       if name == student["name"]:
           print("Student Found!!")
           print(f" {student["name"]} - age is {student["age"]} ")
           print(f" grades:  {student["grades"]}")
           found = True
           break
    if not found:
        print("Not found")    

def average_student():
    name=input("Enter a student : ").capitalize()
    found = False
    for student in students:
       if name == student["name"]:
           average = int(sum(student["grades"]))/int(len(student["grades"]))
           print(f"Average : {average:.2f}")
           found = True
           break
    if not found:
        print("Not found")    

def statistics():
    print("┌────────────────────────┐")
    print("│    CLASS STATISTICS    │")
    print("│────────────────────────│")
    somme = len(students)
    print(f"│  Total students is : {somme}│")
    total_age = 0
    for student in students:
        total_age+=student["age"]

    average =total_age/somme
    print(f"│ Average of age : {average:.2f} │")
    average_grades= []
    for student in students :
        averagegrade=sum(student["grades"])/len(student["grades"])
        average_grades.append(averagegrade)
    print(f"│  Highest average :{max(average_grades):.2f}│")
    print(f"│  Lowest average :{min(average_grades):.2f} │")
    print("│────────────────────────│") 

def random_student():
    choice=random.choice(students)
    print("───────────────────────────────────────────────")
    
    print("So this is your random student : ")    
    print(f"  {choice["name"]} - age is {choice["age"]} ")
    print(f"    grades:  {choice["grades"]}")
    print("───────────────────────────────────────────────")

def Top_students():
    average_grades= []
    for student in students :
        averagegrade=sum(student["grades"])/len(student["grades"])
        average_grades.append(averagegrade)
    
    for index, avgrade in enumerate(average_grades,start=1):
        if avgrade == max(average_grades):
            print("Top student")
            print(f"{students[index - 1]["name"]}")
            print(f"Average : {avgrade}")
        
       

   

    
    




