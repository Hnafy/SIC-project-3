import json
import os

navigation_stack = []

def load_users():
    file_path = os.path.join(os.path.dirname(__file__), "users.json")

    with open(file_path, "r") as file:
        data = json.load(file)

    return data["users"]

def save_users(users):
    file_path = os.path.join(os.path.dirname(__file__), "users.json")

    with open(file_path, "w") as file:
        json.dump({"users": users}, file, indent=4)


def register():
    users = load_users()

    print("\n--- Registeration ---")

    name = input("Enter your name: ")

    while not name.strip():
        print("Name can't be empty.")
        name = input("Enter your name: ")

    phone = input("Enter your phone: ")

    while not valid_phone(phone):
        print("Invalid phone number, Enter 11 digits.")
        phone = input("Enter your phone number: ")

    while any(user["phone"] == phone for user in users):
        print("Phone number is already registered.")
        phone = input("Enter your phone number: ")

    while not valid_phone(phone):
        print("Invalid phone number, Enter 11 digits.")
        phone = input("Enter your phone number: ")

    email = input("Enter your email: ")

    while "@" not in email or "." not in email: 
        print("Invalid email.")
        email = input("Enter your email: ")

    while any(user["email"] == email for user in users): 
        print("Email is already registered.")
        email = input("Enter your email: ")

    gender = input("Enter your gender (Male/Female): ").strip().capitalize()

    while gender not in ["Male", "Female"]:
        print("Please enter Male or Female.")
        gender = input("Enter your gender (Male/Female): ").strip().capitalize()

    governorates = [
        "Cairo",
        "Giza",
        "Alexandria",
        "Monufia",
        "Dakahlia",
        "Qalyubia",
        "Sharqia",
        "Gharbia",
        "Beheira",
        "Fayoum"
    ]

    print("\nGovernorates:")

    for i, governorate in enumerate(governorates, 1):
        print(f"{i}. {governorate}")

    choice = input("Choose your governorate: ")

    while not choice.isdigit() or not 1 <= int(choice) <= len(governorates):
        print("Invalid choice. Please choose a valid number.")
        choice = input("Choose your governorate: ")

    governorate = governorates[int(choice) - 1]
    
    password = input("Enter your password: ")

    while len(password) < 8:
        print("Password must be at least 8 characters.")
        password = input("Enter your password: ")
    
    age = input("Enter your age: ")

    while not valid_age(age):
        print("Invalid age.")
        age = input("Enter your age: ")

    age = int(age)

    national_id = input("Enter your national_id: ")

    while not valid_national_id(national_id):
        print("Invalid national_id, Enter 14 digits.")
        national_id = input("Enter your national_id: ")


    for user in users:
        if user["email"] == email:
            print("Email is already registered.")
            return

    new_user = {
        "name": name,
        "phone": phone,
        "email": email,
        "gender": gender,
        "governorate": governorate,
        "password": password,
        "age": age,
        "national_id": national_id
    }

    users.append(new_user)
    save_users(users)

    print("Registration successful!")

def valid_phone(phone):
    return phone.isdigit() and len(phone) == 11

def valid_national_id(national_id):
    return national_id.isdigit() and len(national_id) == 14

def valid_age(age):
    return age.isdigit() and 1 <= int(age) <= 100



def login():
    users = load_users()

    print("\n--- Login ---")

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email == "admin@gmail.com" and password == "admin123":
        print("Welcome Admin!")
        return "admin"

    for user in users:
        if user["email"] == email and user["password"] == password:
            print(f"Welcome {user['name']}!")
            return email
        
    print("Invalid email or password.")
    return None


def go_to(page):
    navigation_stack.append(page)


def go_back():
    if navigation_stack:
        return navigation_stack.pop()
    return None


def user_home():
    while True:
        print("\n===== User Home =====")
        print("1. Browse Categories")
        print("2. My Trip")
        print("3. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            go_to("User Home")
            print("Categories")

        elif choice == "2":
            go_to("User Home")
            print("My Trip")

        elif choice == "3":
            previous_page = go_back()

            if previous_page:
                print(f"Back to {previous_page}")
            else:
                print("No previous page.")

        else:
            print("Invalid choice.")
    

def main_menu():
    while True:
        print("\n===== Egypt Explorer =====")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            result = login()

            if result is not None:
                user_home()
        elif choice == "2":
            register()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main_menu()