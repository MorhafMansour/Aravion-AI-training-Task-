import csv
import os


class Show:
    def __init__(self, students_file):
        self.students_file = students_file

    def _file_exists_and_not_empty(self):
        if not os.path.exists(self.students_file):
            print("[-] Error: No student data found! File does not exist. ")
            return False
        return True

    def show_all_reports(self):
        if not self._file_exists_and_not_empty(): return

        print(f"\n{'=' * 95}\n{'FULL STUDENTS REPORT':^95}\n{'=' * 95}")
        print(
            f"{'Name':<20} | {'ID':<10} | {'First Mark':<12} | {'Second Mark':<12} | {'Participation':<15} | {'Final Mark':<10}")
        print("-" * 95)

        with open(self.students_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if row:
                    print(f"{row[0]:<20} | {row[1]:<10} | {row[2]:<12} | {row[3]:<12} | {row[4]:<15} | {row[5]:<10}")
        print("=" * 95)

    def show_id_and_name(self):
        if not self._file_exists_and_not_empty(): return

        print(f"\n{'=' * 35}\n{' STUDENTS ID & NAME':^35}\n{'=' * 35}")
        print(f"{'Name':<20} | {'ID':<10}")
        print("-" * 35)

        with open(self.students_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if row:
                    print(f"{row[0]:<20} | {row[1]:<10}")
        print("=" * 35)

    def show_first_mark(self):
        if not self._file_exists_and_not_empty(): return

        print(f"\n{'=' * 35}\n{'FIRST MARK REPORT':^35}\n{'=' * 35}")
        print(f"{'Name':<20} | {'First Mark':<10}")
        print("-" * 35)

        with open(self.students_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if row:
                    print(f"{row[0]:<20} | {row[2]:<10}")
        print("=" * 35)

    def show_second_mark(self):
        if not self._file_exists_and_not_empty(): return

        print(f"\n{'=' * 35}\n{' SECOND MARK REPORT':^35}\n{'=' * 35}")
        print(f"{'Name':<20} | {'Second Mark':<10}")
        print("-" * 35)

        with open(self.students_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if row:
                    print(f"{row[0]:<20} | {row[3]:<10}")
        print("=" * 35)

    def show_final_mark(self):
        if not self._file_exists_and_not_empty(): return

        print(f"\n{'=' * 35}\n{' FINAL MARK REPORT':^35}\n{'=' * 35}")
        print(f"{'Name':<20} | {'Final Mark':<10}")
        print("-" * 35)

        with open(self.students_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if row:
                    print(f"{row[0]:<20} | {row[5]:<10}")
        print("=" * 35)