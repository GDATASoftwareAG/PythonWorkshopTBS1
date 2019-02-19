import sqlite3


def main():
    connection = sqlite3.connect('example_database.db')

    cursor = connection.cursor()
    cursor.execute('SELECT SQLITE_VERSION()')
    data = cursor.fetchone()
    print(data)

    cursor.execute('CREATE TABLE `users`('
                   'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                   'first_name text NOT NULL,'
                   'last_name text NOT NULL,'
                   'access_level INTEGER)')

    cursor.execute('INSERT INTO users (first_name, last_name, access_level) VALUES ("Manuel", "Beelen", 5)')
    connection.commit()
    cursor.execute('INSERT INTO users (first_name, last_name, access_level) VALUES ("Stefan", "Decker", 5)')
    connection.commit()
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchone()
    print(data)
    connection.close()


if __name__ == "__main__":
    main()
