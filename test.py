# coding: utf8

import os
from config import config

# basedir = os.path.abspath(os.path.dirname(__file__))
# print(basedir,'\n')
# print(os.environ.get('SECRET_KEY'))
print(os.environ.get('DATABASE_PASSWORD'))
# print(config)

from app import db
# db.create_all()
# print db.cursor.execute('select *')

from config import config
print config['default'].SQLALCHEMY_DATABASE_URI
