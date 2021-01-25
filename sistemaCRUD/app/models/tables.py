from app import db

class Pessoa(db.Model):
    __tablename__ = 'pessoas'

    #colunas da tabela
    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(50),nullable=False)
    idade = db.Column(db.Integer)
    sexo = db.Column(db.String(1))
    salario = db.Column(db.Float)

    def __init__(self,nome='Anônimo',idade=18,sexo='M',salario=1039.0):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.salario = salario

    '''
    Método para indicar a representação da tabela e assim facilitar o debug
    '''
    def __repr__(self):
        return '<Pessoa %r>' % self.nome
