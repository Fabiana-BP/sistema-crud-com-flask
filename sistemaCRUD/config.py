import os.path
basedir = os.path.abspath(os.path.dirname(__file__)) #recuperar endereço absoluto do arquivo atual

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'banco.db') #cria arquivo local sqlite
SQLALCHEMY_TRACK_MODIFICATIONS = True #permite modificações no banco de dados
