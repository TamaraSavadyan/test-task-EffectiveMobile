import pandas as pd
from models import Contact


class Database:
    db: str = 'database.csv'


class CRUD(Database):
    '''
    This class provides basic CRUD (Create, Read, Update, Delete) operations 
    for managing contact records in a CSV-based database.
    '''

    def create(self, **kwargs) -> str:
        '''
        Create a new contact record in the database.

        Args:
            **kwargs: Keyword arguments representing contact information.

        Returns:
            str: A message indicating the result of the operation.
        '''
        df = pd.read_csv(self.db)

        if not df.empty:
            max_id = df['id'].max()
        else:
            max_id = 0

        new_id = max_id + 1
        kwargs['id'] = new_id

        new_row = pd.DataFrame(kwargs, index=[0])
        updated_df = pd.concat([df, new_row], ignore_index=True)
        updated_df.to_csv(self.db, index=False)

        created_entity = new_row.to_string(index=False, header=False)
        return f'{created_entity}\nCreated successfully'

    def read(self, page: int) -> str:
        '''
        Read and return a paginated view of contact records from the database.

        Args:
            page (int): The page number for pagination.

        Returns:
            str: A formatted string containing the paginated contact records.
        '''
        records_per_page = 5
        df = pd.read_csv(self.db)
        start_idx = (page - 1) * records_per_page
        end_idx = start_idx + records_per_page

        paginated_df = df[start_idx:end_idx]
        if paginated_df.empty:
            return 'Page does not exists'

        return paginated_df.to_string(index=False)

    def update(self, id_: int, **kwargs) -> str:
        '''
        Update an existing contact record in the database.

        Args:
            id_ (int): The ID of the contact to be updated.
            **kwargs: Keyword arguments representing contact information to be updated.

        Returns:
            str: A message indicating the result of the operation.
        '''
        df = pd.read_csv(self.db)
        entity_to_update = df[df['id'] == id_]

        if entity_to_update.empty:
            return 'Entity was not found'

        entity_idx = entity_to_update.index[0]
        df.loc[entity_idx, list(kwargs.keys())] = list(kwargs.values())
        updated_row = df.loc[entity_idx]
        df.to_csv(self.db, index=False)

        updated_entity = df[df['id'] == id_]

        return f'{updated_entity}\nUpdated successfully'

    def delete(self, id_: int) -> str:
        '''
        Delete a contact record from the database.

        Args:
            id_ (int): The ID of the contact to be deleted.

        Returns:
            str: A message indicating the result of the operation.
        '''
        df = pd.read_csv(self.db)
        entity_to_delete = df[df['id'] == id_]

        if entity_to_delete.empty:
            return 'Entity was not found'

        df = df[df['id'] != id_]
        df.to_csv(self.db, index=False)

        return f'{entity_to_delete}\nDeleted successfully'

    def filter(self, **kwargs) -> str:
        '''
        Filter contact records based on provided criteria.

        Args:
            **kwargs: Keyword arguments representing filtering criteria.

        Returns:
            str: A formatted string containing the filtered contact records.
        '''
        df = pd.read_csv(self.db)
        filtered_df = df.copy()

        for field, value in kwargs.items():
            filtered_df = filtered_df[filtered_df[field] == value]

        if filtered_df.empty:
            return 'Entity was not found'

        return filtered_df.to_string(index=False)


if __name__ == '__main__':
    crud = CRUD()

    res = crud.create(first_name='name', patronymic='name', company='name')
    print(res)
