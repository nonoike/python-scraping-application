import os

from app.assets.database import init_db, insert_from_csv


def run():
    print('start!')
    print('checking past data...')
    __remove_data_db_file()
    print('initializing...')
    init_db()
    print('inserting...')
    insert_from_csv('app/assets/data.csv')
    print('complete!')


def __remove_data_db_file(file_path='app/assets/data.db'):
    if os.path.exists(file_path):
        print('removing past data...')
        os.remove(file_path)


if __name__ == '__main__':
    run()
