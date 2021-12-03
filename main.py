from login import login_menu


class User:
    def __inti__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.Email = email


class Registered(User):
    def __init__(self, name, phone_number, email, mail_address, bill_address, points, pay_method):
        super().__inti__(name, phone_number, email)
        self.mail_address = mail_address
        self.bill_address = bill_address
        self.points = points
        self.pay_method = pay_method


if __name__ == '__main__':
    login_menu()
