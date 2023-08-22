import pandas as pd
from models import Contact

class Database:
    db: str = 'database.csv'

class CRUD(Database):
    def create(self, contact: Contact):
        df = pd.read_csv(self.db)
        new_row = pd.DataFrame({
            'id': [contact.id],
            'first_name': [contact.first_name],
            'last_name': [contact.last_name],
            'patronymic': [contact.patronymic],
            'company': [contact.company],
            'phone_corporative': [contact.phone_corporative],
            'phone_personal': [contact.phone_personal]
        })
        updated_df = pd.concat([df, new_row], ignore_index=True)
        updated_df.to_csv(self.db, index=False)
        print('Created successfully')


    def read(self):
        df = pd.read_csv(self.db)
        contacts = []
        for _, row in df.iterrows():
            contact = Contact(row['id'], row['first_name'], row['last_name'], row['patronymic'],
                            row['company'], row['phone_corporative'], row['phone_personal'])
            contacts.append(contact)
        print(contacts)

    def update(self, id_):
        df = pd.read_csv(self.db)
        df.loc[df['id'] == self.contact.id, ['first_name', 'last_name', 'patronymic',
                                                'company', 'phone_corporative', 'phone_personal']] = \
            self.contact.first_name, self.contact.last_name, self.contact.patronymic, \
            self.contact.company, self.contact.phone_corporative, self.contact.phone_personal
        df.to_csv(self.db, index=False)
        print('Updated successfully')


    def delete(self, id_):
        df = pd.read_csv(self.db)
        df = df[df['id'] != id_]
        df.to_csv(self.db, index=False)
        print('Deleted successfully')
