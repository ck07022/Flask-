import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_DRI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'pybp.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False