from faker import Faker

class FakeData:
    def __init__(self):
        self.fake = Faker()

    def get_first_name(self):
        return self.fake.first_name()

    def get_last_name(self):
        return self.fake.last_name()

    def get_email(self):
        return self.fake.unique.email()

    def get_telephone(self):
        # Generate 10-digit number
        return self.fake.random_number(digits=10, fix_len=True)

    def get_password(self):
        return self.fake.password(length=8)