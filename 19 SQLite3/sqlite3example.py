import sqlite3

connection = sqlite3.connect('studentInfo.db')
cursor = connection.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS student (
        rollno INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')

def view_students():
    cursor.execute("SELECT * FROM student")
    for row in cursor.fetchall():
        print(row)

def add_student(rollno, name, age):
    cursor.execute("INSERT INTO student (rollno, name, age) VALUES (?,?,?)", (rollno, name, age))
    connection.commit()

def update_student(rollno, name, age):
    cursor.execute("UPDATE student SET name = ?, age = ? WHERE rollno = ?", (name, age, rollno))
    connection.commit()

def delete_student(rollno):
    cursor.execute("DELETE FROM student WHERE rollno = ?", (rollno,))
    connection.commit()

def main():
    while True:
        print("\nStudent Database Manager")
        print("1. View Students")
        print("2. Add Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_students()
        elif choice == '2':
            rollno = int(input("Enter Roll Number: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            add_student(rollno, name, age)
        elif choice == '3':
            rollno = int(input("Enter Roll Number to Update: "))
            name = input("Enter New Name: ")
            age = int(input("Enter New Age: "))
            update_student(rollno, name, age)
        elif choice == '4':
            rollno = int(input("Enter Roll Number to Delete: "))
            delete_student(rollno)
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

    connection.close()
    print("\nConnection Closed!\n")

if __name__ == "__main__":
    main()
