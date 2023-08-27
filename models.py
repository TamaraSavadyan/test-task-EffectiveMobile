#  фамилия, имя, отчество, название организации, телефон рабочий, телефон личный (сотовый)
from dataclasses import dataclass
from phonenumbers import NumberParseException, parse, is_valid_number


@dataclass
class Contact:
    '''
    Class that represents a contact with various attributes.
    '''
    id: int
    first_name: str
    last_name: str
    patronymic: str
    company: str
    phone_corporative: str
    phone_personal: str

    def __post_init__(self):
        '''
        Post-initialization hook to validate the phone numbers of the contact.
        '''
        self.validate_phones()

    def validate_phones(self):
        '''
        Validates the corporative and personal phone numbers of the contact.

        Prints error messages for invalid phone numbers.
        '''
        if not self.is_valid_phone(self.phone_corporative):
            print(
                f'Invalid corporative phone number for {self.first_name} {self.last_name}')
        if not self.is_valid_phone(self.phone_personal):
            print(
                f'Invalid personal phone number for {self.first_name} {self.last_name}')

    def is_valid_phone(self, phone):
        '''
        Validates if the provided phone number is valid.

        Args:
            phone (str): The phone number to be validated.

        Returns:
            bool: True if the phone number is valid, False otherwise.
        '''
        try:
            parsed_phone = parse(phone, None)
            return is_valid_number(parsed_phone)
        except NumberParseException:
            return False


if __name__ == '__main__':
    contact1 = Contact('John', 'Doe', 'Oliver', 'ABC Corp',
                       '+37493276692', '+79099014964')
    contact2 = Contact('John', 'Doe', 'Oliver', 'ABC Corp',
                       '+37493276692', '+79099014964')

    print(contact1.id)
    print(contact2.id)
