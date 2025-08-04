# Employee Management System (EMS)

# Step 1: Data Storage using dictionary
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Anita', 'age': 30, 'department': 'IT', 'salary': 70000},
    103: {'name': 'Ravi', 'age': 25, 'department': 'Finance', 'salary': 60000}
}

# Step 3: Add Employee Function
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("Employee ID already exists. Please enter a unique ID.")
            return
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))
        
        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }
        print(f"Employee '{name}' added successfully.\n")
    except ValueError:
        print("Invalid input. Please enter correct data types.\n")

# Step 4: View All Employees Function
def view_employees():
    if not employees:
        print("No employees available.\n")
    else:
        print(f"{'ID':<6}{'Name':<15}{'Age':<6}{'Department':<15}{'Salary':<10}")
        print("-" * 52)
        for emp_id, details in employees.items():
            print(f"{emp_id:<6}{details['name']:<15}{details['age']:<6}{details['department']:<15}{details['salary']:<10.2f}")
        print()

# Step 5: Search for Employee
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            details = employees[emp_id]
            print("Employee Found:")
            print(f"Name      : {details['name']}")
            print(f"Age       : {details['age']}")
            print(f"Department: {details['department']}")
            print(f"Salary    : {details['salary']:.2f}\n")
        else:
            print("Employee not found.\n")
    except ValueError:
        print("Invalid input. Please enter a numeric ID.\n")

# Step 2 & 6: Menu Function
def main_menu():
    while True:
        print("=== Employee Management System ===")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the Employee Management System.")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.\n")

# Run the program
if __name__ == "__main__":
    main_menu()
