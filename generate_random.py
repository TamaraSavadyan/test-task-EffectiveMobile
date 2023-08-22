import random
import csv
from models import Contact

first_names = ["Иван", "Мария", "Александр", "Екатерина", "Дмитрий", "Ольга", "Андрей", "Анна", "Сергей", "Александра"]
last_names = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", "Васильев", "Морозов", "Новиков", "Федоров", "Соколов"]
companies = ["ООО Рога и Копыта", "ЗАО Профит", "ИП Развитие", "АО ТехноСервис", "Группа Инновации", "АКБ Финансы"]
phone_formats = ["555-123-4567", "(555) 555-5555", "555.555.1234", "123-456-7890", "5555555555"]

def generate_random_contact() -> Contact:
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    patronymic = random.choice(first_names)
    company = random.choice(companies)
    phone_corporative = random.choice(phone_formats)
    phone_personal = random.choice(phone_formats)

    return Contact(
        first_name=first_name,
        last_name=last_name,
        patronymic=patronymic,
        company=company,
        phone_corporative=phone_corporative,
        phone_personal=phone_personal
    )

random_contacts = [generate_random_contact() for _ in range(20)]

with open('database.csv', mode='w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['first_name', 'last_name', 'patronymic', 'company', 'phone_corporative', 'phone_personal'])
    for contact in random_contacts:
        csv_writer.writerow([contact.first_name, contact.last_name, contact.patronymic, contact.company, contact.phone_corporative, contact.phone_personal])
