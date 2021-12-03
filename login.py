def login_menu():
    ans = True
    while ans:
        print(""""
        1.Guest User 
        2.Registered User Login
        3.Admin Login
        """)
        choice = input("Enter: ")
        if choice == "1":
            date = input("Enter date (mm/dd/yyyy): ")
            time = input("Enter time: ")
            guest_num = input("Enter number of guest: ")
            reservation_portal(date, time, guest_num)
        elif choice == "2":
            print("Registered User Login")
            username = input("Username: ")
            password = input("Password: ")
        elif choice == "3":
            print("Admin Login")
            username = input("Username: ")
            password = input("Password: ")
        else:
            ans = False
            print("Invalid Choice")


def reservation_portal(date, time, guest_num):
    pass


def registered_guest_login(username, password):
    pass


def admin_login(username, password):
    pass
