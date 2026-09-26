import json
import os

CATEGORIES = [
    "Museums",
    "Historical Sites",
    "Nature",
    "Adventure",
    "Cultural Attractions"
]

my_trip = []

TRANSPORT_COST = {
    "Cairo": 100,
    "Giza": 120,
    "Alexandria": 200,
    "Luxor": 300,
    "Aswan": 350,
    "Monufia": 80,
    "Dakahlia": 90,
    "Qalyubia": 80,
    "Sharqia": 90,
    "Gharbia": 90,
    "Beheira": 100,
    "Fayoum": 110,
    "Matrouh": 250,
    "New Valley": 280,
    "South Sinai": 280,
    "Red Sea": 300
}
DEFAULT_TRANSPORT_COST = 100


def load_users():
    file_path = os.path.join(os.path.dirname(__file__), "users.json")

    if not os.path.exists(file_path):
        return []

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


def load_attractions():
    file_path = os.path.join(os.path.dirname(__file__), "attractions.json")

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as file:
        data = json.load(file)

    return data["attractions"]


def save_attractions(attractions):
    file_path = os.path.join(os.path.dirname(__file__), "attractions.json")

    with open(file_path, "w") as file:
        json.dump({"attractions": attractions}, file, indent=4)


def valid_price(value):
    try:
        return float(value) >= 0
    except ValueError:
        return False


def valid_rating(value):
    try:
        rating = float(value)
        return 0 <= rating <= 5
    except ValueError:
        return False

def browse_categories():
    attractions = load_attractions()

    while True:
        print("\n--- Categories ---")

        for i, category in enumerate(CATEGORIES, 1):
            print(f"{i}. {category}")

        print(f"{len(CATEGORIES) + 1}. Back")

        choice = input("Choose a category: ")

        if choice == str(len(CATEGORIES) + 1):
            return

        if not choice.isdigit() or not 1 <= int(choice) <= len(CATEGORIES):
            print("Invalid choice.")
            continue

        category = CATEGORIES[int(choice) - 1]
        filtered = [a for a in attractions if a["category"] == category]
        show_attractions_by_category(category, filtered)


def show_attractions_by_category(category, attractions):
    while True:
        print(f"\n--- {category} ---")

        if not attractions:
            print("No attractions found in this category.")
            return

        for i, a in enumerate(attractions, 1):
            print(f"{i}. {a['name']} - {a['governorate']} - {a['price']} EGP")

        print(f"{len(attractions) + 1}. Back")

        choice = input("Choose an attraction to view: ")

        if choice == str(len(attractions) + 1):
            return

        if not choice.isdigit() or not 1 <= int(choice) <= len(attractions):
            print("Invalid choice.")
            continue

        attraction_page(attractions[int(choice) - 1])


def attraction_page(attraction):
    global my_trip

    while True:
        print(f"\n--- {attraction['name']} ---")
        print(f"Governorate: {attraction['governorate']}")
        print(f"Category: {attraction['category']}")
        print(f"Ticket Price: {attraction['price']} EGP")
        print(f"Rating: {attraction['rating']} / 5")
        print(f"Estimated Visit Time: {attraction['visit_time']} hour(s)")

        in_trip = any(t["name"] == attraction["name"] for t in my_trip)

        print("\n1. Remove from My Trip" if in_trip else "\n1. Add to My Trip")
        print("2. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            if in_trip:
                my_trip[:] = [t for t in my_trip if t["name"] != attraction["name"]]
                print("Removed from My Trip.")
            else:
                my_trip.append(attraction)
                print("Added to My Trip.")
        elif choice == "2":
            return
        else:
            print("Invalid choice.")
def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)

    return merge(left, right, key)


def merge(left, right, key):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def sort_attractions():
    attractions = load_attractions()

    print("\n--- Sort Attractions ---")
    print("1. By Price (Low to High)")
    print("2. By Rating (High to Low)")
    print("3. By Visit Time (Shortest First)")
    print("4. Back")

    choice = input("Choose an option: ")

    if choice == "1":
        results = merge_sort(attractions, lambda a: a["price"])

    elif choice == "2":
        results = merge_sort(attractions, lambda a: -a["rating"])

    elif choice == "3":
        results = merge_sort(attractions, lambda a: a["visit_time"])

    elif choice == "4":
        return

    else:
        print("Invalid choice.")
        return

    if not results:
        print("No attractions found.")
        return

    while True:
        print("\n--- Sorted Attractions ---")

        for i, a in enumerate(results, 1):
            print(
                f"{i}. {a['name']} - "
                f"{a['price']} EGP - "
                f"Rating {a['rating']} - "
                f"{a['visit_time']}h"
            )

        print(f"{len(results) + 1}. Back")

        choice = input("Choose an attraction to view: ")

        if choice == str(len(results) + 1):
            return

        if not choice.isdigit() or not 1 <= int(choice) <= len(results):
            print("Invalid choice.")
            continue

        attraction_page(results[int(choice) - 1])


# My Trip + Trip Total Cost feature
def view_my_trip():
    global my_trip

    while True:
        print("\n--- My Trip ---")

        if not my_trip:
            print("Your trip is empty.")
            print("1. Back")

            choice = input("Choose an option: ")

            if choice == "1":
                return
            else:
                print("Invalid choice.")
                continue

        for i, a in enumerate(my_trip, 1):
            print(f"{i}. {a['name']} - {a['governorate']} - {a['price']} EGP")

        remove_option = len(my_trip) + 1
        summary_option = len(my_trip) + 2
        back_option = len(my_trip) + 3

        print(f"{remove_option}. Remove an Attraction")
        print(f"{summary_option}. View Final Summary (Trip Total Cost)")
        print(f"{back_option}. Back")

        choice = input("Choose an option: ")

        if choice == str(remove_option):
            index = input("Enter the number of the attraction to remove: ")

            if index.isdigit() and 1 <= int(index) <= len(my_trip):
                removed = my_trip.pop(int(index) - 1)
                print(f"Removed {removed['name']} from My Trip.")
            else:
                print("Invalid choice.")

        elif choice == str(summary_option):
            show_final_summary()

        elif choice == str(back_option):
            return

        else:
            print("Invalid choice.")


def show_final_summary():
    global my_trip

    print("\n--- Final Trip Summary ---")

    if not my_trip:
        print("Your trip is empty.")
        return

    tickets_total = 0
    governorates = set()

    for a in my_trip:
        print(f"- {a['name']} ({a['governorate']}) - {a['price']} EGP")
        tickets_total += a["price"]
        governorates.add(a["governorate"])

    transport_total = sum(TRANSPORT_COST.get(g, DEFAULT_TRANSPORT_COST) for g in governorates)
    trip_total_cost = tickets_total + transport_total

    print(f"\nGovernorates visited: {', '.join(governorates)}")
    print(f"Tickets Total: {tickets_total} EGP")
    print(f"Transportation Cost: {transport_total} EGP")
    print(f"Trip Total Cost: {trip_total_cost} EGP")


def binary_search(arr, target, field, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    value = arr[mid][field].lower()

    if value == target:
        return arr[mid]

    if target < value:
        return binary_search(arr, target, field, start, mid - 1)

    return binary_search(arr, target, field, mid + 1, end)

def search_attractions():
    attractions = load_attractions()

    print("\n--- Search ---")
    print("1. Search by Name")
    print("2. Search by Governorate")
    print("3. Back")

    choice = input("Choose an option: ")

    if choice == "1":
        field = "name"
        keyword = input("Enter attraction name: ").strip().lower()

    elif choice == "2":
        field = "governorate"
        keyword = input("Enter governorate: ").strip().lower()

    elif choice == "3":
        return

    else:
        print("Invalid choice.")
        return

    attractions = merge_sort(attractions, lambda a: a[field].lower())

    result = binary_search(
        attractions,
        keyword,
        field,
        0,
        len(attractions) - 1
    )

    if result is None:
        print("No attractions found.")
        return

    print("\n--- Search Result ---")
    print(
        f"{result['name']} - "
        f"{result['governorate']} - "
        f"{result['category']}"
    )

def admin_panel():
    while True:
        print("\n===== Admin Panel =====")
        print("1. View All Attractions")
        print("2. Add Attraction")
        print("3. Update Attraction")
        print("4. Remove Attraction")
        print("5. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            view_all_attractions()
        elif choice == "2":
            add_attraction()
        elif choice == "3":
            update_attraction()
        elif choice == "4":
            remove_attraction()
        elif choice == "5":
            return
        else:
            print("Invalid choice.")


def view_all_attractions():
    attractions = load_attractions()

    print("\n--- All Attractions ---")

    if not attractions:
        print("No attractions found.")
        return

    for i, a in enumerate(attractions, 1):
        print(f"{i}. {a['name']} | {a['governorate']} | {a['category']} | "
              f"{a['price']} EGP | Rating {a['rating']} | {a['visit_time']}h")


def add_attraction():
    attractions = load_attractions()

    print("\n--- Add New Attraction ---")

    name = input("Enter attraction name: ")

    while not name.strip():
        print("Name can't be empty.")
        name = input("Enter attraction name: ")

    while any(a["name"].lower() == name.lower() for a in attractions):
        print("An attraction with this name already exists.")
        name = input("Enter attraction name: ")

    governorate = input("Enter governorate: ")

    while not governorate.strip():
        print("Governorate can't be empty.")
        governorate = input("Enter governorate: ")

    price = input("Enter ticket price (EGP): ")

    while not valid_price(price):
        print("Invalid price. Enter a positive number.")
        price = input("Enter ticket price (EGP): ")

    rating = input("Enter rating (0-5): ")

    while not valid_rating(rating):
        print("Invalid rating. Enter a number between 0 and 5.")
        rating = input("Enter rating (0-5): ")

    visit_time = input("Enter estimated visit time (in hours): ")

    while not valid_price(visit_time):
        print("Invalid visit time. Enter a positive number.")
        visit_time = input("Enter estimated visit time (in hours): ")

    print("\nCategories:")
    for i, category in enumerate(CATEGORIES, 1):
        print(f"{i}. {category}")

    cat_choice = input("Choose a category: ")

    while not cat_choice.isdigit() or not 1 <= int(cat_choice) <= len(CATEGORIES):
        print("Invalid choice.")
        cat_choice = input("Choose a category: ")

    new_attraction = {
        "name": name,
        "governorate": governorate,
        "price": float(price),
        "rating": float(rating),
        "visit_time": float(visit_time),
        "category": CATEGORIES[int(cat_choice) - 1]
    }

    attractions.append(new_attraction)
    save_attractions(attractions)

    print("Attraction added successfully!")


def find_attraction_by_name(attractions):
    name = input("Enter the exact name of the attraction: ").strip().lower()

    for a in attractions:
        if a["name"].lower() == name:
            return a

    return None


def update_attraction():
    attractions = load_attractions()

    print("\n--- Update Attraction ---")

    if not attractions:
        print("No attractions found.")
        return

    target = find_attraction_by_name(attractions)

    if not target:
        print("Attraction not found.")
        return

    while True:
        print(f"\nEditing: {target['name']}")
        print("1. Update Name")
        print("2. Update Governorate")
        print("3. Update Ticket Price")
        print("4. Update Rating")
        print("5. Update Visit Time")
        print("6. Update Category")
        print("7. Save & Back")

        choice = input("Choose an option: ")

        if choice == "1":
            new_name = input("Enter new name: ")
            if new_name.strip():
                target["name"] = new_name
            else:
                print("Name can't be empty.")

        elif choice == "2":
            new_gov = input("Enter new governorate: ")
            if new_gov.strip():
                target["governorate"] = new_gov
            else:
                print("Governorate can't be empty.")

        elif choice == "3":
            price = input("Enter new ticket price: ")
            while not valid_price(price):
                print("Invalid price.")
                price = input("Enter new ticket price: ")
            target["price"] = float(price)

        elif choice == "4":
            rating = input("Enter new rating (0-5): ")
            while not valid_rating(rating):
                print("Invalid rating.")
                rating = input("Enter new rating (0-5): ")
            target["rating"] = float(rating)

        elif choice == "5":
            visit_time = input("Enter new visit time (in hours): ")
            while not valid_price(visit_time):
                print("Invalid visit time.")
                visit_time = input("Enter new visit time (in hours): ")
            target["visit_time"] = float(visit_time)

        elif choice == "6":
            for i, category in enumerate(CATEGORIES, 1):
                print(f"{i}. {category}")
            cat_choice = input("Choose a category: ")
            if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(CATEGORIES):
                target["category"] = CATEGORIES[int(cat_choice) - 1]
            else:
                print("Invalid choice.")

        elif choice == "7":
            save_attractions(attractions)
            print("Attraction updated successfully!")
            return

        else:
            print("Invalid choice.")


def remove_attraction():
    attractions = load_attractions()

    print("\n--- Remove Attraction ---")

    if not attractions:
        print("No attractions found.")
        return

    target = find_attraction_by_name(attractions)

    if not target:
        print("Attraction not found.")
        return

    confirm = input(f"Are you sure you want to remove '{target['name']}'? (yes/no): ").strip().lower()

    if confirm == "yes":
        attractions.remove(target)
        save_attractions(attractions)
        print("Attraction removed successfully!")
    else:
        print("Cancelled.")


def user_home():
    while True:
        print("\n===== User Home =====")
        print("1. Browse Categories")
        print("2. Search Attractions")
        print("3. Sort Attractions")
        print("4. My Trip")
        print("5. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            browse_categories()
        elif choice == "2":
            search_attractions()
        elif choice == "3":
            sort_attractions()
        elif choice == "4":
            view_my_trip()
        elif choice == "5":
            return
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

            if result == "admin":
                admin_panel()
            elif result is not None:
                user_home()

        elif choice == "2":
            register()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main_menu()
