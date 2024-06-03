"""Baxtiyorova Diyora"""
import requests
import time
from enum import Enum
import psycopg2
import threading


class Color(Enum):
    black = 'black'
    grey = 'grey'
    white = 'white'


def commit(func):
    def wrapper():
        func()
        conn.commit()
    return wrapper


"""task - 1"""
db_name = 'n47'
user = 'postgres'
host = 'localhost'
password = '123'
port = 5432

conn = psycopg2.connect(database=db_name, user=user,
                        host=host, password=password, port=port)
cur = conn.cursor()


def create_table():
    create_table_query = """CREATE TABLE IF NOT EXISTS product(
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(255) NOT NULL,
                            price FLOAT NOT NULL,
                            color VARCHAR(255) NOT NULL,
                            image VARCHAR(255) NOT NULL);"""
    cur.execute(create_table_query)
    conn.commit()


"""task - 2"""


def select_all_products():
    select_query = """SELECT * FROM product;"""
    cur.execute(select_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)


@commit
def insert_product():
    insert_query = """INSERT INTO product(name, price, color, image)
                      VALUES(%s, %s, %s, %s)"""
    n = input('Enter name: ')
    p = float(input('Enter price: '))
    i = input('Enter image: ')
    data = (n, p, Color.black.value, i)
    cur.execute(insert_query, data)


@commit
def update_product():
    id_ = int(input('Enter product of id to be updated: '))
    n_name = input('Enter new name: ')
    update_query = """UPDATE product SET name = %s WHERE id = %s"""
    cur.execute(update_query, (n_name, id_))


@commit
def delete_product():
    d_id = int(input('Enter product id to be deleted: '))
    delete_query = """DELETE FROM product WHERE id = %s;"""
    cur.execute(delete_query, (d_id,))


"""task - 3"""
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Alphabet:
    def __init__(self):
        self.index = 0
        self.el = ' '

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(alphabet):
            raise StopIteration
        self.el = alphabet[self.index]
        self.index += 1
        return self.el


a = Alphabet()
for i in a:
    print(i)


"""task - 4"""


def print_numbers():
    for b in range(1, 6):
        print(b)
        time.sleep(1)


def print_letters():
    for el in 'ABCDE':
        print(el)
        time.sleep(1)


# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()


"""task - 5"""


class Product:
    def __init__(self, name: str, price: float, color: str, image: str):
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def save(self):
        q = """INSERT INTO product(name, price, color, image)
                            VALUES(%s, %s, %s, %s)"""
        data = (self.name, self.price, self.color, self.image)
        cur.execute(q, data)
        conn.commit()


p = Product('sofa', 12.67, 'green', 'https//:sofa')
p.save()

"""task - 6"""


class DBConnect:
    def __enter__(self):
        self.conn = conn
        self.curr = conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Connected to DB.')


with DBConnect() as db:
    print('Activating context manager.')
    db.curr.execute("""SELECT * FROM product;""")
    for e in db.curr.fetchall():
        print(e)


"""task - 7"""


@commit
def add_to_products():
    url = 'https://dummyjson.com/products/'
    r = requests.get(url)
    i_query = """INSERT INTO product(name, price, color, image)
                                VALUES(%s, %s, %s, %s)"""
    for product in r.json()['products']:
        cur.execute(i_query, (product['title'], product['price'], Color.black.value, product['images'][0]))
