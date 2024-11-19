import pymysql.cursors

connection = pymysql.connect(host='localhost', user='root', password='12345678', db='testdb', charset='utf8')

with connection:
    print(connection.get_server_info())

    with connection.cursor() as cursor:
        cursor.execute('insert into student (user_name, age) values (%s, %s)', ('tom', 23))
        # connection is not autocommit by default. So you must commit to save your changes.
        connection.commit()

    with connection.cursor() as cursor:
        cursor.execute('select * from student')
        fetch_result = cursor.fetchall()
        print(fetch_result)
