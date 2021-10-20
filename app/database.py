from peewee import *

from local_settings import DATABASE_USERNAME
from local_settings import DATABASE_PASSWORD

db = MySQLDatabase('notificaciones_cripto',
                    user=DATABASE_USERNAME,
                    password=DATABASE_PASSWORD,
                    host='localhost', port=3306)

class User(Model):
    username = CharField(max_length=255, null=False)
    email = CharField(max_length=255, null=False)

    class Meta:
        database = db
        table_name = 'users'

class CriptoCurrency(Model):
    name = CharField(max_length=255, null=False)
    symbol = CharField(max_length=255, null=False)
    # coingeeko_id = ''

    class Meta:
        database = db
        table_name = 'cripto_currencies'

class UserCripto(Model):
    user = ForeignKeyField(User, backref='criptos')
    criptocurrency = ForeignKeyField(CriptoCurrency, backref='users')
    stop_limit = IntegerField(null=True)

    class Meta:
        database = db
        table_name = 'user_criptos'

    def __str__(self):
        return f'Stop limit {self.stop_limit}'