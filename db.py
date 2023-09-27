import psycopg2
import config as conf

# connection = psycopg2.connect(
#     database=conf.DB_NAME,
#     user=conf.DB_USER,
#     password=conf.DB_PASSWORD,
#     host=conf.DB_HOST
# )
#
# cursor = connection.cursor()

class BaseConnection:
    def __init__(self):
        self.connection = psycopg2.connect(
            database=conf.DB_NAME,
            user=conf.DB_USER,
            password=conf.DB_PASSWORD,
            host=conf.DB_HOST
        )
        # self.cursor = connection.cursor()

    def manager(self, sql, *args,
                commit: bool = False,
                fetchone: bool = False,
                fetchall: bool = False):
        with self.connection as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result  = db.commit()
                if fetchone:
                    result = cursor.fetchone()
                if fetchall:
                    result = cursor.fetchall()
                return result


# connection = BaseConnection()

class TableManager(BaseConnection):
    def create_categories_table(self):
        sql = '''
        drop table if exists categories;
        create table if not exists categories(
            category_id integer primary key generated always as identity,
            category_name VARCHAR(50)
        );
        '''
        self.manager(sql, commit=True)

    def create_products_table(self):
        sql = '''
        drop table if exists products;
        create table if not exists products(
            product_id integer primary key generated always as identity,
            title VARCHAR(100),
            price FLOAT,
            description TEXT,
            image TEXT,
            rate FLOAT,
            rate_count INTEGER,
            category_id integer references categories(category_id)
        );
        '''
        self.manager(sql, commit=True)


class QueryManager(BaseConnection):
    def insert_categories(self, categories_list):
        sql = 'INSERT INTO categories(category_name) VALUES (%s);'
        for category in categories_list:
            self.manager(sql, category, commit=True)
            print(f'Категория: {category} успешно добавлена!')

# table_manager = TableManager()
#
# table_manager.create_categories_table()
# table_manager.create_products_table()
