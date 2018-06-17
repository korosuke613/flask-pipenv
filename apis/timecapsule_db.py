import sqlite3
from contextlib import closing

dbname = 'timecapsule.sqlite'


class TimeCapsule:
    def __init__(self):
        pass

    def get_event_id_max(self, c):
        sql = 'select max(event_id) from events'
        for row in c.execute(sql):
            return row[0]

    def add_user(self, id, name, address, mail_address, password):
        with closing(sqlite3.connect(dbname)) as conn:
            c = conn.cursor()
            insert_sql = 'insert into users (id, name, address, mail_address, password) values (?,?,?,?,?)'
            user = (id, name, address, mail_address, password)
            c.execute(insert_sql, user)
            conn.commit()

    def add_event(self, user_id, delivery_date, info):
        with closing(sqlite3.connect(dbname)) as conn:
            c = conn.cursor()
            insert_sql = 'insert into events (event_id, user_id, delivery_date, info) values (?,?,?,?)'
            event_id = self.get_event_id_max(c) + 1
            event = (event_id, user_id, delivery_date, info)
            c.execute(insert_sql, event)
            conn.commit()

    def get_user_event(self, user_id):
        with closing(sqlite3.connect(dbname)) as conn:
            c = conn.cursor()
            sql = 'select * from events where user_id = ?'
            events = []
            for row in c.execute(sql, (user_id,)):
                events.append({'event_id': row[0], 'user_id': row[1],
                               'delivery_date': row[2], 'info': row[3]})
            return events

    def get_user(self, user_id):
        with closing(sqlite3.connect(dbname)) as conn:
            c = conn.cursor()
            sql = 'select * from users where id = ?'
            for row in c.execute(sql, (user_id,)):
                return {'id': row[0], 'name': row[1],
                        'address': row[2], 'mail_address': row[3],
                        'password': row[4]}
