from peewee import MySQLDatabase

from local_settings import DATABASE_USERNAME
from local_settings import DATABASE_PASSWORD

db = MySQLDatabase('notificaciones_cripto',
                    user=DATABASE_USERNAME,
                    password=DATABASE_PASSWORD,
                    host='localhost', port=3306)