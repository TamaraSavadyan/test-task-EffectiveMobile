from database import CRUD


def show_contacts(database_conn: CRUD) -> None:
    page = input('Enter page number you want to see: ')
    try:
        int(page)
    except ValueError:
        print('You need to provide an integer')
        return 
    if not page:
        page = 1
    result = database_conn.read(page=int(page))
    print(result)


def update_contact(database_conn: CRUD) -> None:
    id_ = input('Enter contact id to modify it: ')

    result = 5


def delete_contact(database_conn: CRUD) -> None:
    id_ = input('Enter contact id to delete it: ')
    result = database_conn.delete(id_=int(id_))
    print(result)

def add_contact(database_conn: CRUD) -> None:
    pass


def find_contact(database_conn: CRUD) -> None:
    pass


def main():
    database_conn = CRUD()
    print('Welcome to Phone Book !!!\nYou can add new contact to this book\nRead or modify existing contacts')
    user_input = input('Choose a command. Enter /help to see list of commands\n')
    if user_input == '/help':
        print('Congrats u dumb dumb\n')
    show_contacts(database_conn)
    delete_contact(database_conn)


if __name__ == '__main__':
    main()
