import csv
import os
from auth import AdminAuth


def show_programmer_screen():
    print("Name for programmer: Morhaf Mansour")
    print("University: Yarmouk ")
    print("Major: Cybersecurity ")
    print("-" * 35)
    input("If you want to go to next page please press enter ")

#=========================================================================
class SLMS:
    def __init__(self):
        self.auth_manager = AdminAuth()
        self.students_file = "student_info.csv"

    def main_menu(self):
        while True:
            print("\n=== Screen 3: Main Menu ===")
            print("1. Add Student (add stu)")
            print("2. Modify Student (modi stu)")
            print("3. Show Report (show report)")
            print("4. Logout")
            print("-" * 35)
            if not os.path.exists(self.students_file):
                with open(self.students_file, "w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        ["Student Name", "ID", "First Mark", "Second Mark", "Participation Mark", "Final Mark"])

            choice = input("Enter your choice (1-4): ").strip()


            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.modify_student()
            elif choice == "3":
                self.show_report()
            elif choice == "4":
                print("Logging out from SLMS System... ")
                break
            else:
                print("Invalid choice! Please enter a number from 1 to 4. ")

    def add_student(self):

            print("\n--- [1] Add Student Screen ---")

            student_name = input("Enter student name: ").strip()
            student_id = input("Enter ID: ").strip()
            if not student_name or not student_id:
                print("[-] Error: Student Name and ID cannot be empty! ")
                input("\nPress Enter to return to Main Menu...")
                return
            if os.path.exists(self.students_file):
                with open(self.students_file, "r", newline="", encoding="utf-8") as file:
                    reader = csv.reader(file)
                    next(reader, None)
                    for row in reader:
                        if row and row[1] == student_id:
                            print(f"[-] Error: Student ID '{student_id}' already exists!  ")
                            input("\nPress Enter to return to Main Menu...")
                            return

            first_mark = input("Enter First Mark: ").strip()
            second_mark = input("Enter Second Mark: ").strip()
            participation_mark = input("Enter Participation Mark: ").strip()
            final_mark = input("Enter Final Mark: ").strip()



            with open(self.students_file, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([student_name, student_id, first_mark, second_mark, participation_mark, final_mark])

            print(f"[+] Student '{student_name}' added successfully to {self.students_file}! ")
            input("\nPress Enter to return to Main Menu...")

    def modify_student(self):
        print("\n--- [2] Modify Student Screen ---")
        student_id = input("Enter student ID to search: ").strip()
        found = False

        with open(self.students_file, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    if row and row[1] == student_id:
                        found = True
                        break

        if not found:
            print(f"[-] Error: Student ID '{student_id}' not found! ")
            input("\nPress Enter to return to Main Menu...")
            return
        while True:
            print(f"\n[+] Student ID '{student_id}' found successfully!")
            print("1. Proceed to modification screen ")
            print("0. Cancel and back to Main Menu ")
            print("-" * 35)

            choice = input("Enter your choice (0 or 1): ").strip()

            if choice == "0":
                print("Operation canceled.")
                break
            elif choice == "1":
                from modify_code import Modify
                modifier = Modify(self.students_file, student_id)
                modifier.display_menu()
                break
            else:
                print("Invalid choice! Please enter 0 or 1. ")




        input("\nPress Enter to return to Main Menu...")

    def show_report(self):
        from showing_code import Show
        reporter = Show(self.students_file)

        while True:
            print("\n--- [3] Show Report Screen ---")
            print("1. Show all students report")
            print("2. Show just ID & Name for students report")
            print("3. Show the first mark for students report")
            print("4. Show the second mark for students report")
            print("5. Show the final mark for students report")
            print("6. Return to Main Menu...")
            print("-" * 35)

            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                reporter.show_all_reports()
            elif choice == "2":
                reporter.show_id_and_name()
            elif choice == "3":
                reporter.show_first_mark()
            elif choice == "4":
                reporter.show_second_mark()
            elif choice == "5":
                reporter.show_final_mark()
            elif choice == "6":
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice! Please enter a number from 1 to 6. ")

            input("\nPress Enter to continue...")
    def run(self):
        self.auth_manager.auth_menu(self.main_menu)

#=========================================================================
if __name__ == "__main__":
    show_programmer_screen()

    app = SLMS()
    app.run()