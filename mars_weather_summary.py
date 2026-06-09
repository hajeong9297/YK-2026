import csv
import mysql.connector


class MySQLHelper:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, values=None):
        self.cursor.execute(query, values)
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()


def create_table(db_helper):
    query = '''
    CREATE TABLE IF NOT EXISTS mars_weather (
        weather_id INT AUTO_INCREMENT PRIMARY KEY,
        mars_date DATETIME NOT NULL,
        temp INT,
        storm INT
    )
    '''
    db_helper.execute_query(query)


def read_csv_file(file_name):
    weather_data = []

    with open(file_name, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            mars_date = row[0]
            temp = int(row[1])
            storm = int(row[2])
            weather_data.append((mars_date, temp, storm))

    return weather_data


def insert_weather_data(db_helper, weather_data):
    query = '''
    INSERT INTO mars_weather (
        mars_date,
        temp,
        storm
    )
    VALUES (
        %s,
        %s,
        %s
    )
    '''

    for data in weather_data:
        db_helper.execute_query(query, data)


def main():
    db_helper = MySQLHelper(
        host='localhost',
        user='root',
        password='1234',
        database='mars_db'
    )

    create_table(db_helper)

    weather_data = read_csv_file('mars_weathers_data.csv')

    for data in weather_data:
        print(data)

    insert_weather_data(db_helper, weather_data)

    print('데이터 저장 완료')

    db_helper.close()


if __name__ == '__main__':
    main()