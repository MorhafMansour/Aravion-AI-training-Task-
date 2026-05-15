import hashlib
import os

class AdminAuth:
    def __init__(self):
        self.auth_file = "admin_creds.txt"

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_admin(self):
        print("\n=== [Sign Up] Register Admin Account ===")
        username = input("Create Admin Username: ").strip()
        password = input("Create Admin Password: ").strip()

        hashed_password = self.hash_password(password)

        with open(self.auth_file, "a") as file:
            file.write(f"{username},{hashed_password}\n")

        print("[+] Admin account created successfully! ")

    def login_admin(self):
        print("\n=== Admin Login ===")
        if not os.path.exists(self.auth_file):
            print("[-] No admin registered yet! Please register an account first. ")
            return False

        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()

        input_hash = self.hash_password(password)

        with open(self.auth_file, "r") as file:
            for line in file:
                if line.strip():
                    stored_username, stored_hash = line.strip().split(",")
                    if username == stored_username and input_hash == stored_hash:
                        print("[+] Login Successful! Access Granted. ")
                        return True

        print("[-] Invalid Username or Password! ")
        return False

    def auth_menu(self, main_menu_callback):
        while True:
            print("\n=== Screen 2: Authentication Menu ===")
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            print("-" * 35)

            choice = input("Enter your choice (1-3): ").strip()

            if choice == "1":
                if self.login_admin():
                    main_menu_callback()
            elif choice == "2":
                self.register_admin()
            elif choice == "3":
                print("Exiting System. Goodbye! ")
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3. ")