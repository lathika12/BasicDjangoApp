import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoLevelFour.settings")
import django
django.setup()

from BasicUserCRUD.models import UserProfile
from faker import Faker
faker = Faker()

def create_user(n):

    for i in range(n):
        name = faker.name().split()
        first_name = name[0]
        last_name = name[1]
        email = faker.email()
        phone = faker.phone_number()
        about = faker.text()

        entry = UserProfile.objects.get_or_create(first_name=first_name, last_name=last_name, email=email, phone=phone,
                                                  about=about)

if __name__ == '__main__':
    print("Generating DB")
    create_user(10)
    print("Completed.")