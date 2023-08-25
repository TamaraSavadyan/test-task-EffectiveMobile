from database import CRUD
from utils import check_if_integer


def show_contacts(database_conn: CRUD) -> None:
    page = input(
        'Enter page number you want to see (you can leave this empty): ')
    if not page:
        page = 1

    if not check_if_integer(page):
        print('You need to provide an integer')
        return

    while True:

        result = database_conn.read(page=int(page))
        print(result)
        print('If you want to see another page enter "next" to see next page or "prev" to see previous page')
        print('Also you can enter another page number')
        user_input = input('To exit enter "exit": ')

        if user_input == 'next':
            page += 1
        elif user_input == 'prev' and page > 1:
            page -= 1
        elif check_if_integer(user_input):
            page = int(user_input)
        elif user_input == 'exit':
            break
        else:
            print('I dont understand, enter again')


def update_contact(database_conn: CRUD) -> None:
    id_ = input('Enter contact id to modify it: ')
    if not check_if_integer(id_):
        print('You need to provide an integer')
        return
    
    keys_input = input('Enter keys to update in one line: ')
    values_input = input('Enter corresponding values in one line: ')

    keys = keys_input.split()
    values = values_input.split()

    if len(keys) != len(values):
        print("Number of keys and values must be the same.")
        return

    kwargs = {key: value for key, value in zip(keys, values)}

    result = database_conn.update(id_=int(id_), **kwargs)
    print(result)



def delete_contact(database_conn: CRUD) -> None:
    id_ = input('Enter contact id to delete it: ')
    if not check_if_integer(id_):
        print('You need to provide an integer')
        return
    result = database_conn.delete(id_=int(id_))
    print(result)


def add_contact(database_conn: CRUD) -> None:
    print('Do not provide id')
    keys_input = input('Enter all keys in one line: ')
    values_input = input('Enter all values in one line: ')

    keys = keys_input.split()
    if len(keys) > 6:
        print('You must provide 6 key:value pairs')
        return
    values = values_input.split()

    if len(keys) != len(values):
        print("Number of keys and values must be the same.")
        return

    kwargs = {key: value for key, value in zip(keys, values)}

    result = database_conn.create(**kwargs)
    print(result)


def find_contact(database_conn: CRUD) -> None:
    key = input('Enter field name: ')
    value = input('Enter field value: ')
    if key == 'id':
        value = int(value)
    result = database_conn.filter(**{key: value})
    print(result)


def main():
    database_conn = CRUD()
    print('Welcome to The Phone Book !!!\nYou can add new contact to this book\nRead or modify existing contacts')

    while True:
        user_input = input(
            'Choose a command. Enter /help to see list of commands\n')
        if user_input == '/help':
            print('Commands:')
            print('show -> shows phone book page by page')
            print('add -> add new coctact to phone book')
            print('find -> find contact using any parameter ')
            print('update -> update existing contact')
            print('delete -> delete existing contact')
            print('exit -> stop this programm')
        elif user_input == 'show':
            show_contacts(database_conn)
        elif user_input == 'delete':
            delete_contact(database_conn)
        elif user_input == 'update':
            update_contact(database_conn)
        elif user_input == 'find':
            find_contact(database_conn)
        elif user_input == 'add':
            add_contact(database_conn)
        elif user_input == 'exit':
            break
        else:
            print('I do not understand, please enter again')


if __name__ == '__main__':
    main()
