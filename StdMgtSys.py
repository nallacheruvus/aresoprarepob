
import os

FILE = "studentsinfo.txt"

# Console color flags
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

# 1. Register The Student Record
def register_record():
    """Prompt for student details and save the record to file."""
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")
    with open(FILE, "a") as f:
        f.write(sid + "," + name + "," + age + "," + marks + "\n")
    print(BLUE+"Student Record Added Successfully!"+RESET)


# 2. Display All The Students Records Function
def display_records():
    """Read and display all student records in tabular format."""
    if not os.path.exists(FILE):
        print(RED+"No student records found!"+RESET)
        return
    with open(FILE, "r") as f:
        records = f.readlines()
    if not records:
        print(RED+"No student records found!"+RESET)
        return
    print("\nID\tName\tAge\tMarks")
    print("-" * 40)
    for record in records:
        sid, name, age, marks = record.strip().split(",")
        print(sid, "\t", name, "\t", age, "\t", marks)


# 3. Find The Student Record Function
def find_record():
    """Search for and display a student record by ID."""
    sid = input(BLUE+"Enter Existing Student ID to search: "+RESET)
    if not os.path.exists(FILE):
        print("No Student records found!")
        return
    with open(FILE, "r") as f:
        for record in f:
            data = record.strip().split(",")
            if data[0] == sid:
                print(BLUE+"\nStudent Found!"+RESET)
                print("ID:", data[0])
                print("Name:", data[1])
                print("Age:", data[2])
                print("Marks:", data[3])
                return
    print(RED+"Student Record not found!"+RESET)


# 4. Modify The Student Record Function
def modify_record():
    """Update details of an existing student record by ID."""
    sid = input(BLUE+"Enter Existing Student ID to update: "+RESET)
    if not os.path.exists(FILE):
        print(RED+"No records found!"+RESET)
        return
    with open(FILE, "r") as f:
        records = f.readlines()
    found = False
    with open(FILE, "w") as f:
        for record in records:
            data = record.strip().split(",")
            if data[0] == sid:
                print(BLUE+"Enter New Student Details:"+RESET)
                name = input(BLUE+"Enter Name: "+RESET)
                age = input(BLUE+"Enter Age: "+RESET)
                marks = input(BLUE+"Enter Marks: "+RESET)

                f.write(sid + "," + name + "," + age + "," + marks + "\n")
                found = True
            else:
                f.write(record)
    if found:
        print(GREEN+"Student Record updated successfully!"+RESET)
    else:
        print(RED+"Student Record not found!"+RESET)


# 5. Remove Student Record Function
def remove_record():
    """Delete a student record by ID from the file."""
    sid = input(BLUE +"Enter The Student ID to delete: "+RESET)
    if not os.path.exists(FILE):
        print(RED+"No related records found!"+RESET)
        return
    with open(FILE, "r") as f:
        records = f.readlines()
    found = False
    with open(FILE, "w") as f:
        for record in records:
            data = record.strip().split(",")
            if data[0] == sid:
                found = True
            else:
                f.write(record)
    if found:
        print(GREEN+"Student Record deleted successfully!"+RESET)
    else:
        print(RED+"Student not found!"+RESET)


# 6. Record Management Panel
while True:
    print("_"*75)
    print(RED+"\n\t\tSOPRA STERIA STUDENT RECORD MANAGEMENT SYSTEM"+RESET)
    print("_"*75)
    print(BLUE+"1. Register Student Information"+RESET)
    print(BLUE+"2. Display Students Information"+RESET)
    print(BLUE+"3. Find Student Information"+RESET)
    print(BLUE+"4. Modify Student Information"+RESET)
    print(BLUE+"5. Remove Student Information"+RESET)
    print(BLUE+"6. Exit"+RESET)
    choice = input(BLUE+"\nEnter your choice: "+RESET)
    if choice == "1":
        register_record()
    elif choice == "2":
        display_records()
    elif choice == "3":
        find_record()
    elif choice == "4":
        modify_record()
    elif choice == "5":
        remove_record()
    elif choice == "6":
        print(BLUE+"Thank you for using Student Management System!"+RESET)
        break
    else:
        print(RED+"Invalid choice! Please try again."+RESET)
   