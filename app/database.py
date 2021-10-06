from peewee import *

from local_settings import DATABASE_USERNAME
from local_settings import DATABASE_PASSWORD

db = MySQLDatabase('notificaciones_cripto',
                    user=DATABASE_USERNAME,
                    password=DATABASE_PASSWORD,
                    host='localhost', port=3306)

class UserCripto(Model):
    # username
    # token
    stop_limit = IntegerField(null=True)

    class Meta:
        database = db
        table_name = 'user_criptos'

    def __str__(self):
        return f'Stop limit {self.stop_limit}'