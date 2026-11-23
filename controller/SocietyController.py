from model.SocietyModel import (
    add_member,
    get_all_members,
    get_member_by_id,
    update_member,
    delete_member,
    search_member,
)


def _print_members(records):
    if not records:
        print("No members found.")
        return
    print("-" * 90)
    print(f"{'ID':<6}{'Name':<20}{'Flat':<12}{'Phone':<15}{'Maintenance':<14}{'Status':<10}")
    print("-" * 90)
    for r in records:
        print(f"{r[0]:<6}{r[1]:<20}{r[2]:<12}{r[3]:<15}{r[4]:<14}{r[5]:<10}")
    print("-" * 90)


def add_member_controller():
    member_name = input("Enter member name: ").strip()
    if not member_name:
        print("Member name cannot be empty.")
        return

    flat_number = input("Enter flat number: ").strip()
    if not flat_number:
        print("Flat number cannot be empty.")
        return

    phone = input("Enter phone number: ").strip()
    if not phone:
        print("Phone number cannot be empty.")
        return

    amount_input = input("Enter monthly maintenance amount: ").strip()
    try:
        monthly_maintenance = float(amount_input)
    except ValueError:
        print("Monthly maintenance must be a valid number.")
        return
    if monthly_maintenance < 0:
        print("Monthly maintenance cannot be negative.")
        return

    payment_status = input("Enter payment status (Paid/Pending): ").strip().capitalize()
    if payment_status not in ("Paid", "Pending"):
        print("Payment status must be Paid or Pending.")
        return

    if add_member(member_name, flat_number, phone, monthly_maintenance, payment_status):
        print("Member added successfully.")
    else:
        print("Failed to add member.")


def view_members_controller():
    records = get_all_members()
    _print_members(records)


def search_member_controller():
    choice = input("Search by (1) ID or (2) Name: ").strip()
    if choice == "1":
        id_input = input("Enter member ID: ").strip()
        try:
            member_id = int(id_input)
        except ValueError:
            print("Member ID must be a valid integer.")
            return
        record = get_member_by_id(member_id)
        if record:
            _print_members([record])
        else:
            print("Member not found.")
    elif choice == "2":
        name = input("Enter member name (partial allowed): ").strip()
        if not name:
            print("Name cannot be empty.")
            return
        records = search_member(name)
        _print_members(records)
    else:
        print("Invalid choice.")


def update_member_controller():
    id_input = input("Enter member ID to update: ").strip()
    try:
        member_id = int(id_input)
    except ValueError:
        print("Member ID must be a valid integer.")
        return

    existing = get_member_by_id(member_id)
    if not existing:
        print("Member not found.")
        return

    print("Existing details:")
    _print_members([existing])

    member_name = input(f"Enter new name (blank to keep '{existing[1]}'): ").strip()
    if not member_name:
        member_name = existing[1]

    flat_number = input(f"Enter new flat number (blank to keep '{existing[2]}'): ").strip()
    if not flat_number:
        flat_number = existing[2]

    phone = input(f"Enter new phone (blank to keep '{existing[3]}'): ").strip()
    if not phone:
        phone = existing[3]

    amount_input = input(f"Enter new monthly maintenance (blank to keep '{existing[4]}'): ").strip()
    if amount_input == "":
        monthly_maintenance = float(existing[4])
    else:
        try:
            monthly_maintenance = float(amount_input)
        except ValueError:
            print("Monthly maintenance must be a valid number.")
            return
    if monthly_maintenance < 0:
        print("Monthly maintenance cannot be negative.")
        return

    status_input = input(f"Enter new payment status (Paid/Pending, blank to keep '{existing[5]}'): ").strip()
    if status_input == "":
        payment_status = existing[5]
    else:
        payment_status = status_input.capitalize()
    if payment_status not in ("Paid", "Pending"):
        print("Payment status must be Paid or Pending.")
        return

    if update_member(member_id, member_name, flat_number, phone, monthly_maintenance, payment_status):
        print("Member updated successfully.")
    else:
        print("Failed to update member.")


def delete_member_controller():
    id_input = input("Enter member ID to delete: ").strip()
    try:
        member_id = int(id_input)
    except ValueError:
        print("Member ID must be a valid integer.")
        return

    existing = get_member_by_id(member_id)
    if not existing:
        print("Member not found.")
        return

    _print_members([existing])
    confirm = input("Are you sure you want to delete? (Y/N): ").strip().upper()
    if confirm != "Y":
        print("Deletion cancelled.")
        return

    if delete_member(member_id):
        print("Member deleted successfully.")
    else:
        print("Failed to delete member.")


def display_menu():
    print("=========================================")
    print(" SOCIETY MAINTENANCE MANAGEMENT SYSTEM")
    print("=========================================")
    print("1. Add Society Member")
    print("2. View All Members")
    print("3. Search Member")
    print("4. Update Member")
    print("5. Delete Member")
    print("6. Exit")
    print()
    print("Select an option:", end=" ")


def run_app():
    while True:
        display_menu()
        choice = input().strip()
        if choice == "1":
            add_member_controller()
        elif choice == "2":
            view_members_controller()
        elif choice == "3":
            search_member_controller()
        elif choice == "4":
            update_member_controller()
        elif choice == "5":
            delete_member_controller()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
        print()
