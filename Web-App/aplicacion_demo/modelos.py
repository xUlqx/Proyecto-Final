from . import db
from sqlalchemy import Table, Column, Integer, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

automovil_persona = Table('association', Base.metadata,
                          Column('automovil_id', Integer, ForeignKey('automovil.id')),
                          Column('persona_id', Integer, ForeignKey('persona.id'))
                          )

class AutoPersona(db.Model):
    __tablename__ = 'autopersona'
    automovil_id = Column(Integer, ForeignKey('automovil.id'), primary_key=True)
    persona_id = Column(Integer, ForeignKey('persona.id'), primary_key=True)

tarjeta_cliente = Table('association2', Base.metadata,
                          Column('tarjeta_id', Integer, ForeignKey('tarjeta.id')),
                          Column('cliente_id', Integer, ForeignKey('cliente.id'))
                          )

class TarjetaCliente(db.Model):
    __tablename__ = 'tarjetacliente'
    tarjeta_id = Column(Integer, ForeignKey('tarjeta.id'), primary_key=True)
    cliente_id = Column(Integer, ForeignKey('cliente.id'), primary_key=True)

    @classmethod
    def get_all(cls):
        tarjetaclientes = TarjetaCliente.query.all()
        return tarjetaclientes


"""venta_cliente = Table('association3', Base.metadata,
                          Column('venta_id', Integer, ForeignKey('venta.id')),
                          Column('cliente_id', Integer, ForeignKey('cliente.id'))
                          )

class VentaCliente(db.Model):
    __tablename__ = 'ventacliente'
    venta_id = Column(Integer, ForeignKey('venta.id'), primary_key=True)
    cliente_id = Column(Integer, ForeignKey('cliente.id'), primary_key=True)"""


class Automovil(db.Model):
    __tablename__ = 'automovil'
    id = db.Column(db.Integer,
                   primary_key=True)
    marca = db.Column(db.String(64),
                       index=False,
                       unique=False,
                       nullable=False)
    modelo = db.Column(db.String(80),
                         index=False,
                         unique=False,
                         nullable=False)
    creado = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    activo = db.Column(db.Boolean,
                      index=False,
                      unique=False,
                      nullable=False)
    personas = relationship("Persona", secondary='autopersona')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        automoviles = Automovil.query.all()
        return automoviles

    def __repr__(self):
        return '<Automovil {}, {}>'.format(self.marca, self.modelo)

class Persona(db.Model):
    __tablename__ = 'persona'
    id = db.Column(db.Integer,
                   primary_key=True)
    nombre = db.Column(db.String(64),
                       index=False,
                       unique=False,
                       nullable=False)
    apellido = db.Column(db.String(80),
                         index=False,
                         unique=False,
                         nullable=False)
    creado = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    activo = db.Column(db.Boolean,
                      index=False,
                      unique=False,
                      nullable=False)
    automoviles = relationship("Automovil", secondary='autopersona')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        personas = Persona.query.all()
        return personas

    def __repr__(self):
        return '<Persona {}, {}>'.format(self.apellido, self.nombre)


class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer,
                   primary_key=True)
    nombre = db.Column(db.String(64),
                       index=False,
                       unique=False,
                       nullable=False)
    apellido = db.Column(db.String(80),
                         index=False,
                         unique=False,
                         nullable=False)
    creado = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    activo = db.Column(db.Boolean,
                      index=False,
                      unique=False,
                      nullable=False)
    
    tarjetas = relationship("Tarjeta", secondary="tarjetacliente")
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        clientes = Cliente.query.all()
        return clientes

    def __repr__(self):
        return '<Cliente {}, {}>'.format(self.apellido, self.nombre)

class Tarjeta(db.Model):
    __tablename__ = 'tarjeta'
    id = db.Column(db.Integer,
                   primary_key=True)
    tipo = db.Column(db.String(64),
                       index=False,
                       unique=False,
                       nullable=False)
    numero = db.Column(db.Integer,
                         index=False,
                         unique=False,
                         nullable=False)
    codigoSeguridad = db.Column(db.Integer,
                         index=False,
                         unique=False,
                         nullable=False)
    vencimientoMes = db.Column(db.String(64),
                      index=False,
                      unique=False,
                      nullable=False)
    vencimientoAnio = db.Column(db.String(64),
                      index=False,
                      unique=False,
                      nullable=False)
    montoMax = db.Column(db.Float,
                         index=False,
                         unique=False,
                         nullable=False)
    token = db.Column(db.Text,
                         index=False,
                         unique=False,
                         nullable=False)
                         
    
    clientes = relationship("Cliente", secondary='tarjetacliente')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        tarjetas = Tarjeta.query.all()
        return tarjetas

class Venta(db.Model):
    __tablename__ = 'venta'
    id = db.Column(db.Integer,
                   primary_key=True)
    monto = db.Column(db.Float,
                         index=False,
                         unique=False,
                         nullable=False)
    token = db.Column(db.Text,
                         index=False,
                         unique=False,
                         nullable=False)
    id_cliente = db.Column(Integer,
                           index=False,
                           unique=False,
                           nullable=False)
    
    
   
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        ventas = Venta.query.all()
        return ventas
