import sqlite3
import os
from contextlib import closing

dbname = 'timecapsule.sqlite'


def create():
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()

        # executeメソッドでSQL文を実行する
        create_table = '''create table users (id int, name varchar(64),
                          password varchar(64), address varchar(64), mail_address varchar(64))'''
        c.execute(create_table)


def rm_sqlite():
    if os.path.exists('./' + dbname):
        os.remove('./' + dbname)


def create_with_sql():
    rm_sqlite()
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        f = open('./db.sql', 'r')
        sql = f.read()
        c.executescript(sql)


def add_sample_date():
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        insert_sql = 'insert into users (id, name, address, mail_address, password) values (?,?,?,?,?)'
        users = [
            (0, '平木場　風太', '鹿児島県姶良市', 'korosuke613613@gmail.com', 'bibibibi'),
            (1, 'beeno', '福岡県北九州市', 'beeno@example.com', 'fdfdfdf'),
        ]
        c.executemany(insert_sql, users)

        insert_sql = 'insert into events (event_id, user_id, delivery_date, info) values (?,?,?,?)'
        events = [
            (0, 1, '2020-01-01', '荷物'),
            (1, 2, '2025-07-07', '卒論'),
        ]
        c.executemany(insert_sql, events)

        conn.commit()


def sample():
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()

        # SQL文に値をセットする場合は，Pythonのformatメソッドなどは使わずに，
        # セットしたい場所に?を記述し，executeメソッドの第2引数に?に当てはめる値を
        # タプルで渡す．
        sql = 'insert into users (id, name, age, gender) values (?,?,?,?)'
        user = (1, 'Taro', 20, 'male')
        c.execute(sql, user)

        # 一度に複数のSQL文を実行したいときは，タプルのリストを作成した上で
        # executemanyメソッドを実行する
        insert_sql = 'insert into users (id, name, age, gender) values (?,?,?,?)'
        users = [
            (2, 'Shota', 54, 'male'),
            (3, 'Nana', 40, 'female'),
            (4, 'Tooru', 78, 'male'),
            (5, 'Saki', 31, 'female')
        ]
        c.executemany(insert_sql, users)
        conn.commit()

        select_sql = 'select * from users'
        for row in c.execute(select_sql):
            print(row)


if __name__ == '__main__':
    create_with_sql()
    add_sample_date()
