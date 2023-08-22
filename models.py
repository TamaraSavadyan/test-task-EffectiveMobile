#  фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)
from dataclasses import dataclass
from phonenumbers import NumberParseException, parse, is_valid_number

@dataclass
class Contact:
    first_name: str
    last_name: str
    patronymic: str
    company: str
    phone_corporative: str
    phone_personal: str

    _id_counter = 0

    def __post_init__(self):
        Contact._id_counter += 1
        self.id = Contact._id_counter

    def is_valid_phone(self, phone):
        try:
            parsed_phone = parse(phone, None)
            return is_valid_number(parsed_phone)
        except NumberParseException:
            return False