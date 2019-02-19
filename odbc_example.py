import pyodbc


def main():
    connection = pyodbc.connect('DRIVER={SQL_SERVER};SERVER=tcp:SOME_SERVER\\SOME_INSTANCE', autocommit=True)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM some_table WHERE some_key = "some_value"')
    data = cursor.fetchone()
    while data is not None:
        print(data)
        data = cursor.fetchone()

    cursor.execute('UPDATE some_table SET some_value = 3 WHERE some_other_value = 1')
    print(f"Affected rows: {cursor.rowcount}")
    connection.close()


if __name__ == "__main__":
    main()
