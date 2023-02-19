from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

ma = Marshmallow()

db = SQLAlchemy()


class Personal(db.Model):  # создаем общий класс модели базы данных
    __abstract__ = True


class Users(Personal, UserMixin):  # модель пользователей системы
    """ Create model for users"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)
    role = db.Column(db.Text)


class Candidate(Personal):  # модель анкетных данных
    """ Create model for candidates dates"""

    __tablename__ = 'candidates'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    region = db.Column(db.Text)
    full_name = db.Column(db.Text, index=True)
    last_name = db.Column(db.Text)
    birthday = db.Column(db.Text)
    birth_place = db.Column(db.Text)
    country = db.Column(db.Text)
    snils = db.Column(db.Text)
    inn = db.Column(db.Text)
    education = db.Column(db.Text)
    addition = db.Column(db.Text)
    update_date = db.Column(db.Text)
    status = db.Column(db.Text)
    request_id = db.Column(db.Text)
    passports = db.relationship('Passport', backref='candidates')
    addresses = db.relationship('Address', backref='candidates')
    workplaces = db.relationship('Workplace', backref='candidates')
    contacts = db.relationship('Contact', backref='candidates')
    relations = db.relationship('RelationShip', backref='candidates')
    staffs = db.relationship('Staff', backref='candidates')
    checks = db.relationship('Check', backref='candidates')
    registries = db.relationship('Registry', backref='candidates')
    poligrafs = db.relationship('Poligraf', backref='candidates')
    inqueries = db.relationship('Inquery', backref='candidates')
    investigations = db.relationship('Investigation', backref='candidates')


class Passport(Personal):  # модель паспорта
    """ Create model for passport dates"""

    __tablename__ = 'passports'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    series_passport = db.Column(db.Text)
    number_passport = db.Column(db.Text)
    agency = db.Column(db.Text)
    date_given = db.Column(db.Text)
    passport_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class Address(Personal):  # создаем общий класс модель адреса
    """ Create model for addresses"""

    __tablename__ = 'addresses'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    region = db.Column(db.Text)
    address = db.Column(db.Text)
    type = db.Column(db.Text)
    address_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class Workplace(Personal):  # создаем общий класс модель рабочих мест
    """ Create model for workplaces"""

    __tablename__ = 'workplaces'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    period = db.Column(db.Text)
    work_place = db.Column(db.Text)
    address = db.Column(db.Text)
    staff = db.Column(db.Text)
    work_place_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class Contact(Personal):  # создаем общий класс телефонного номера
    """ Create model for phones"""

    __tablename__ = 'contacts'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    type = db.Column(db.Text)
    contact = db.Column(db.Text)
    contact_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class RelationShip(Personal):  # создаем общий класс связи
    """ Create model for relations"""

    __tablename__ = 'relations'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    relation = db.Column(db.Text)
    full_name = db.Column(db.Text)
    birthday = db.Column(db.Text)
    address = db.Column(db.Text)
    workplace = db.Column(db.Text)
    contact = db.Column(db.Text)
    relation_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class Staff(Personal):  # создаем общий класс должности
    """ Create model for staff"""

    __tablename__ = 'staffs'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    staff = db.Column(db.Text)
    department = db.Column(db.Text)
    staff_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class Check(Personal):  # модель данных проверки кандидатов
    """ Create model for candidates checks"""

    __tablename__ = 'checks'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    check_work_place = db.Column(db.Text)
    former_employee = db.Column(db.Text)
    check_passport = db.Column(db.Text)
    check_inn = db.Column(db.Text)
    check_debt = db.Column(db.Text)
    check_bankruptcy = db.Column(db.Text)
    check_bki = db.Column(db.Text)
    check_court = db.Column(db.Text)
    check_affiliation = db.Column(db.Text)
    check_terrorist = db.Column(db.Text)
    check_mvd = db.Column(db.Text)
    check_internet = db.Column(db.Text)
    check_cronos = db.Column(db.Text)
    check_cross = db.Column(db.Text)
    check_addition = db.Column(db.Text)
    pfo = db.Column(db.Text)
    comment = db.Column(db.Text)
    resume = db.Column(db.Text)
    date_check = db.Column(db.Text)
    officer = db.Column(db.Text)
    url = db.Column(db.Text)
    check_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))
    registries = db.relationship('Registry', backref='checks')


class Registry(Personal):  # модель данных результаты ПФО
    """ Create model for poligraf"""

    __tablename__ = 'registries'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    marks = db.Column(db.Text)
    decision = db.Column(db.Text)
    dec_date = db.Column(db.Text)
    supervisor = db.Column(db.Text)
    registry_check_id = db.Column(db.Integer, db.ForeignKey('checks.id'))
    registry_cand_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class Poligraf(Personal):  # модель данных результаты ПФО
    """ Create model for poligraf"""

    __tablename__ = 'poligrafs'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    theme = db.Column(db.Text)
    results = db.Column(db.Text)
    officer = db.Column(db.Text)
    date_pfo = db.Column(db.Text)
    poligraf_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class Investigation(Personal):  # модель данных служебных расследований
    """ Create model for ivestigation"""
    __tablename__ = 'investigations'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    theme = db.Column(db.Text)
    info = db.Column(db.Text)
    date_inv = db.Column(db.Text)
    inv_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class Inquery(Personal):  # модель данных запросов по работникам
    """ Create model for candidates inqueries"""

    __tablename__ = 'inqueries'

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    info = db.Column(db.Text)
    initiator = db.Column(db.Text)
    date_inq = db.Column(db.Text)
    iquery_id = db.Column(db.Integer, db.ForeignKey('candidates.id'))


class CandidateSchema(ma.Schema):
    class Meta:
        fields = ('id', 'full_name', 'birthday', 'birth_place', 'series_passport', 'number_passport',
                  'agency', 'date_given', 'snils', 'inn', 'reg_address', 'live_address', 'phone', 'email')


cand_schema = CandidateSchema()
