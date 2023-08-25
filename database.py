import pandas as pd
from models import Contact


class Database:
    db: str = 'database.csv'


class CRUD(Database):
    def create(self, **kwargs) -> str:
        df = pd.read_csv(self.db)
        new_row = pd.DataFrame(kwargs, index=[0])
        updated_df = pd.concat([df, new_row], ignore_index=True)
        updated_df.to_csv(self.db, index=False)
        return 'Created successfully'

    def read(self, page: int) -> str:
        records_per_page = 10
        df = pd.read_csv(self.db)
        start_idx = (page - 1) * records_per_page
        end_idx = start_idx + records_per_page

        paginated_df = df[start_idx:end_idx]
        if paginated_df.empty:
            return 'Page does not exists'
        
        return paginated_df.to_string(index=False)

    def update(self, id_: int, **kwargs) -> str:
        df = pd.read_csv(self.db)
        df.loc[df['id'] == id_, list(kwargs.keys())] = list(kwargs.values())
        df.to_csv(self.db, index=False)
        return 'Updated successfully'

    def delete(self, id_: int) -> str:
        df = pd.read_csv(self.db)
        entity_to_delete = df[df['id'] == id_]

        if entity_to_delete.empty:
            return 'Entity was not found'
        
        df = df[df['id'] != id_]
        df.to_csv(self.db, index=False)
        
        return f'{entity_to_delete}\nDeleted successfully'

    def filter(self, **kwargs) -> str:
        df = pd.read_csv(self.db)
        filtered_df = df.copy()

        for field, value in kwargs.items():
            filtered_df = filtered_df[filtered_df[field] == value]

        if filtered_df.empty:
            return 'Entity was not found'

        return filtered_df.to_string(index=False)


if __name__ == '__main__':
    crud = CRUD()
