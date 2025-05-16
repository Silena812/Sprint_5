from faker import Faker

faker = Faker()

def generate_registration_data():
    email = faker.email()
    password = faker.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    username = faker.user_name()
    return email, password, username

