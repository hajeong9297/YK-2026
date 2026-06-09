import csv
import mysql.connector
from mysql.connector import Error


class MySQLHelper:
    def __init__(self, host, user, password, database):
        self.connection = None

        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )

            if self.connection.is_connected():
                print('MySQL 연결 성공')

        except Error as error:
            print('MySQL 연결 실패:', error)

    def execute_query(self, query, values=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()

        except Error as error:
            print('쿼리 실행 실패:', error)

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print('MySQL 연결 종료')


def read_weather_csv(file_name):
    weather_data = []

    try:
        with open(file_name, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                print(row)

                weather_data.append({
                    'mars_date': row['mars_date'],
                    'temp': int(row['temp']),
                    'storm': int(row['storm'])
                })

    except FileNotFoundError:
        print(file_name, '파일을 찾을 수 없습니다.')

    except KeyError as error:
        print('CSV 컬럼명이 올바르지 않습니다:', error)

    except ValueError as error:
        print('CSV 데이터 형식이 올바르지 않습니다:', error)

    return weather_data


def insert_weather_data(mysql_helper, weather_data):
    insert_query = '''
        INSERT INTO mars_weather (mars_date, temp, storm)
        VALUES (%s, %s, %s)
    '''

    for weather in weather_data:
        values = (
            weather['mars_date'],
            weather['temp'],
            weather['storm']
        )

        mysql_helper.execute_query(insert_query, values)

    print('CSV 데이터 INSERT 완료')


def main():
    file_name = 'mars_weathers_data.csv'

    mysql_helper = MySQLHelper(
        host='localhost',
        user='root',
        password='본인_mysql_비밀번호',
        database='mars_db'
    )

    if mysql_helper.connection is None:
        return

    print('CSV 데이터 읽기 시작')

    weather_data = read_weather_csv(file_name)

    if weather_data:
        insert_weather_data(mysql_helper, weather_data)
    else:
        print('INSERT할 데이터가 없습니다.')

    mysql_helper.close()


if __name__ == '__main__':
    main()