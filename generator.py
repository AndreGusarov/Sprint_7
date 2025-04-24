from faker import Faker

def register_new_courier():
    fake = Faker()
    login = fake.user_name()
    password = fake.password()
    firstName = fake.name()
    payload = {
        "login": login,
        "password": password,
        "name": firstName
    }
    return payload

def register_new_courier_without_login():
    fake = Faker()
    login = fake.user_name()
    firstName = fake.name()
    payload = {
        "login": login,
        "name": firstName
    }
    return payload

def register_new_courier_without_password():
    fake = Faker()
    password = fake.password()
    firstName = fake.name()
    payload = {
        "password": password,
        "name": firstName
    }
    return payload