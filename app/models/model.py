from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields

db = SQLAlchemy()
ma = Marshmallow()


class User(db.Model, UserMixin):  # модель пользователей системы
    """ Create model for users"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    role = db.Column(db.String)


class Candidate(db.Model):  # модель анкетных данных
    """ Create model for candidates dates"""

    __tablename__ = 'candidates'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    region = db.Column(db.String(250))
    fullname = db.Column(db.String(250), index=True)
    previous = db.Column(db.String(250))
    birthday = db.Column(db.Date)
    birthplace = db.Column(db.String(250))
    country = db.Column(db.String(250))
    snils = db.Column(db.String(11))
    inn = db.Column(db.String(12))
    education = db.Column(db.String(250))
    addition = db.Column(db.Text)
    deadline = db.Column(db.DateTime)
    status = db.Column(db.String(250))
    recruiter = db.Column(db.String(250))
    request_id = db.Column(db.Integer)
    documents = db.relationship('Document', backref='candidates', cascade="all, delete-orphan")
    addresses = db.relationship('Address', backref='candidates', cascade="all, delete-orphan")
    workplaces = db.relationship('Workplace', backref='candidates', cascade="all, delete-orphan")
    contacts = db.relationship('Contact', backref='candidates', cascade="all, delete-orphan")
    relations = db.relationship('RelationShip', backref='candidates', cascade="all, delete-orphan")
    staffs = db.relationship('Staff', backref='candidates', cascade="all, delete-orphan")
    checks = db.relationship('Check', backref='candidates')
    poligrafs = db.relationship('Poligraf', backref='candidates', cascade="all, delete-orphan")
    inquiries = db.relationship('Inquiry', backref='candidates', cascade="all, delete-orphan")
    investigations = db.relationship('Investigation', backref='candidates', cascade="all, delete-orphan")


class Staff(db.Model):  # создаем общий класс должности
    """ Create model for staff"""

    __tablename__ = 'staffs'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    position = db.Column(db.String(250))
    department = db.Column(db.String(250))
    cand_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class Document(db.Model):  # модель паспорта
    """ Create model for Document dates"""

    __tablename__ = 'documents'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    view = db.Column(db.String(250))
    series = db.Column(db.String(25))
    number = db.Column(db.String(25))
    agency = db.Column(db.String(250))
    issue = db.Column(db.Date)
    cand_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class Address(db.Model):  # создаем общий класс модель адреса
    """ Create model for addresses"""

    __tablename__ = 'addresses'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    view = db.Column(db.String(250))
    region = db.Column(db.String(250))
    address = db.Column(db.String(250))
    cand_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class Workplace(db.Model):  # создаем общий класс модель рабочих мест
    """ Create model for workplaces"""

    __tablename__ = 'workplaces'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    period = db.Column(db.String(250))
    workplace = db.Column(db.String(250))
    address = db.Column(db.String(250))
    position = db.Column(db.String(250))
    cand_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class Contact(db.Model):  # создаем общий класс телефонного номера
    """ Create model for phones"""

    __tablename__ = 'contacts'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    view = db.Column(db.String(250))
    contact = db.Column(db.String(250))
    cand_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class RelationShip(db.Model):  # создаем общий класс связи
    """ Create model for relations"""

    __tablename__ = 'relations'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    relation = db.Column(db.String(250))
    fullname = db.Column(db.String(250))
    birthday = db.Column(db.Date)
    address = db.Column(db.String(250))
    workplace = db.Column(db.String(250))
    contact = db.Column(db.String(250))
    cand_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class Check(db.Model):  # модель данных проверки кандидатов
    """ Create model for candidates checks"""

    __tablename__ = 'checks'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    workplace = db.Column(db.Text)
    employee = db.Column(db.Text)
    document = db.Column(db.Text)
    inn = db.Column(db.Text)
    debt = db.Column(db.Text)
    bankruptcy = db.Column(db.Text)
    bki = db.Column(db.Text)
    courts = db.Column(db.Text)
    affiliation = db.Column(db.Text)
    terrorist = db.Column(db.Text)
    mvd = db.Column(db.Text)
    internet = db.Column(db.Text)
    cronos = db.Column(db.Text)
    cros = db.Column(db.Text)
    addition = db.Column(db.Text)
    path = db.Column(db.String(250))
    pfo = db.Column(db.Boolean)
    comments = db.Column(db.Text)
    conclusion = db.Column(db.String(250))
    deadline = db.Column(db.DateTime)
    officer = db.Column(db.String(250))
    cand_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))
    registries = db.relationship('Registry', backref='checks', cascade="all, delete-orphan")


class Registry(db.Model):  # модель данных результаты ПФО
    """ Create model for poligraf"""

    __tablename__ = 'registries'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    comments = db.Column(db.Text)
    decision = db.Column(db.String(250))
    deadline = db.Column(db.DateTime)
    supervisor = db.Column(db.String(25))
    check_id = db.Column(db.Integer, db.ForeignKey('checks.id'))


class Poligraf(db.Model):  # модель данных результаты ПФО
    """ Create model for poligraf"""

    __tablename__ = 'poligrafs'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    theme = db.Column(db.String(250))
    results = db.Column(db.Text)
    officer = db.Column(db.String(25))
    deadline = db.Column(db.Date)
    cand_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class Investigation(db.Model):  # модель данных служебных расследований
    """ Create model for ivestigation"""

    __tablename__ = 'investigations'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    theme = db.Column(db.String(250))
    info = db.Column(db.Text)
    deadline = db.Column(db.Date)
    cand_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class Inquiry(db.Model):  # модель данных запросов по работникам
    """ Create model for candidates inqueries"""

    __tablename__ = 'inquiries'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    info = db.Column(db.Text)
    initiator = db.Column(db.String(250))
    source = db.Column(db.String(250))
    deadline = db.Column(db.Date)
    cand_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class CandidateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Candidate


class DocumentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Document
        exclude = ("id",)


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address
        exclude = ("id",)


class StaffSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Staff
        exclude = ("id",)


class WorkplaceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Workplace
        exclude = ("id",)


class ContactSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contact
        exclude = ("id",)


class CheckSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Check


class SerialResume(ma.SQLAlchemyAutoSchema):
    resume = fields.Nested(CandidateSchema())
    document = fields.Nested(DocumentSchema())
    staff = fields.Nested(StaffSchema())
    addresses = fields.List(fields.Nested(AddressSchema()))
    workplaces = fields.List(fields.Nested(WorkplaceSchema()))
    contacts = fields.List(fields.Nested(ContactSchema()))


class DecerialResume:
    """Класс для десериализации резюме"""

    def __init__(self) -> None:
        self.send_resume = None
        self.resume = CandidateSchema(only=('id', 'fullname', 'birthday', 'birthplace', 'snils', 'inn',))
        self.document = DocumentSchema()
        self.address = AddressSchema(only=('address',))

    def decer_res(self, new_id, **kwargs):
        resum = db.session.query(Candidate).filter_by(id=new_id).first()
        docum = db.session.query(Document).filter_by(cand_id=new_id).order_by(Document.id.desc()).first()
        addr = db.session.query(Address).filter_by(cand_id=new_id).filter(Address.view.ilike("%регистрац%")). \
            order_by(Address.id.desc()).first()
        self.send_resume = self.resume.dump(resum) | self.document.dump(docum) | \
                           self.address.dump(addr) | dict(kwargs)
        return self.send_resume


decerial_resume = DecerialResume()  # схема для десериализации анкеты для отправки на проверку
check_schema = CheckSchema()  # схема для десериализации и верификации результата проверки
candidate_schema = SerialResume()  # схема для сериализации и верификации анкеты присланной по API

# db.create_all()
