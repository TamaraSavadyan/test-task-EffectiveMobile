#  фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)
from dataclasses import dataclass
from phonenumbers import NumberParseException, parse, is_valid_number

@dataclass
class Contact:
    id: int
    first_name: str
    last_name: str
    patronymic: str
    company: str
    phone_corporative: str
    phone_personal: str


    def __post_init__(self):
        self.validate_phones()

    def validate_phones(self):
        if not self.is_valid_phone(self.phone_corporative):
            print(f"Invalid corporative phone number for {self.first_name} {self.last_name}")
        if not self.is_valid_phone(self.phone_personal):
            print(f"Invalid personal phone number for {self.first_name} {self.last_name}")

    def is_valid_phone(self, phone):
        try:
            parsed_phone = parse(phone, None)
            return is_valid_number(parsed_phone)
        except NumberParseException:
            return False


if __name__ == '__main__':
    contact1 = Contact("John", "Doe", "Oliver", "ABC Corp", "+37493276692", "+79099014964")
    contact2 = Contact("John", "Doe", "Oliver", "ABC Corp", "+37493276692", "+79099014964")

    print(contact1.id)
    print(contact2.id)
