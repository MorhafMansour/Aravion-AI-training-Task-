import csv

class Modify:
    def __init__(self, students_file, student_id):
        self.students_file = students_file
        self.student_id = student_id

    def get_current_student(self):
        with open(self.students_file, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if row and row[1] == self.student_id:
                    return row
        return None

    def display_menu(self):
        while True:
            current_student = self.get_current_student()

            if current_student:
                print("\n" + "=" * 40)
                print("       CURRENT STUDENT DETAILS      ")
                print("=" * 40)
                print(f" Name:               {current_student[0]}")
                print(f" ID:                 {current_student[1]}")
                print(f" First Mark:         {current_student[2]}")
                print(f" Second Mark:        {current_student[3]}")
                print(f" Participation Mark: {current_student[4]}")
                print(f" Final Mark:         {current_student[5]}")
                print("=" * 40)
            else:
                print("[-] Error: Student record not found or deleted! ")
                break

            print("\n=== Screen 4: Modify Student Options ===")
            print("1. Modify Name")
            print("2. Modify ID")
            print("3. Modify First Mark")
            print("4. Modify Second Mark")
            print("5. Modify Participation Mark")
            print("6. Modify Final Mark")
            print("7. Back to Main Menu (Screen 3)")
            print("-" * 35)

            choice = input("Enter your choice (1-7): ").strip()

            if choice == "7":
                print("Returning to Main Menu...")
                break
            elif choice in ["1", "2", "3", "4", "5", "6"]:
                self.execute_modification(choice)
            else:
                print("Invalid choice! Please enter a number from 1 to 7. ")

    def execute_modification(self, option):
        rows = []
        modified = False
        new_id = self.student_id

        with open(self.students_file, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)
            rows.append(header)

            for row in reader:
                if row and row[1] == self.student_id:
                    modified = True
                    if option == "1":
                        row[0] = input("Enter new Student Name: ").strip()
                    elif option == "2":
                        temp_id = input("Enter new ID: ").strip()
                        if self.is_id_duplicate(temp_id) and temp_id != self.student_id:
                            print("[-] Error: This ID already exists! Modification canceled. ")
                            return
                        row[1] = temp_id
                        new_id = temp_id
                    elif option == "3":
                        row[2] = input("Enter new First Mark: ").strip()
                    elif option == "4":
                        row[3] = input("Enter new Second Mark: ").strip()
                    elif option == "5":
                        row[4] = input("Enter new Participation Mark: ").strip()
                    elif option == "6":
                        row[5] = input("Enter new Final Mark: ").strip()
                rows.append(row)

        if modified:
            with open(self.students_file, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            self.student_id = new_id
            print("[+] Student data updated successfully! ")

    def is_id_duplicate(self, check_id):
        with open(self.students_file, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if row and row[1] == check_id:
                    return True
        return False