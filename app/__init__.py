from peewee import MySQLDatabase

from .database import db

from .database import User
from .database import CriptoCurrency
from .database import UserCripto


def create_app():
    db.create_tables([User, CriptoCurrency, UserCripto])

    return True