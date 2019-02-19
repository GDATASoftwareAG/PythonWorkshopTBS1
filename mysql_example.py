import pymysql


def main():
    connection = pymysql.connect(host='some_host', port=3306, user='some_user', passwd='some_pw', db='some_db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM some_table WHERE some_key = "some_value"')
    count = cursor.rownumber
    data = cursor.fetchone()
    while data is not None:
        print(data)
        data = cursor.fetchone()
    connection.close()


if __name__ == "__main__":
    main()
