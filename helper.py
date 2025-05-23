from faker import Faker
import random

faker = Faker()

def generate_registration_data():
    email = faker.email()
    length = random.randint(6, 100)
    password = faker.password(length=length)
    username = faker.user_name()
    return email, password, username

def generate_wrong_password():
    email = faker.email()
    length = random.randint(1, 5)
    password = faker.password(
        length=length,
        special_chars=False,
        digits=False,
        upper_case=False,
        lower_case=True
    )
    username = faker.user_name()
    return email, password, username

def generate_empty_password():
    email = faker.email()
    password = ""
    username = faker.user_name()
    return email, password, username