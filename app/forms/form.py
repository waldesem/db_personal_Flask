import enum
from datetime import datetime

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, \
    PasswordField, SelectField, DateField, FileField
from wtforms.validators import InputRequired, Optional, Length

TODAY = datetime.now()

STATUS = dict(newfag='01-Новый',
              update='02-Обновлен',
              manual='03-Проверка',
              auto='04-Автомат',
              robot='05-Робот',
              reply='06-Автоответ',
              poligrafo='07-ПФО',
              result='08-Результат',
              cancel="09-Отменено",
              finish='10-Окончен'
              )


class Status(enum.Enum):
    NEWFAG = 'Новый'
    UPDATE = 'Обновлен'
    MANUAL = 'Проверка'
    AUTO = 'Автомат'
    ROBOT = 'Робот'
    REPLY = 'Автоответ'
    POLIGRAF = 'ПФО'
    RESULT = 'Результат'
    CANCEL = 'Отменено'
    FINISH = 'Окончен'


class LoginForm(FlaskForm):  # форма для входа в систему
    """ Create form for login page"""

    username = StringField(u"Логин: ", validators=[InputRequired(), Length(max=25)],
                           render_kw={"placeholder": "Имя пользователя"})
    password = PasswordField(u"Пароль: ", validators=[InputRequired(), Length(max=25)],
                             render_kw={"placeholder": "Пароль"})
    remember = BooleanField("Запомнить ", default=False, validators=[])
    submit = SubmitField("Войти")


class FileForm(FlaskForm):  # форма для загрузки файла
    """ Create form for file upload"""
    file = FileField("Загрузить файл", validators=[FileAllowed(['xlsx', 'xlsm'])])
    submit = SubmitField("Загрузить")


class StaffForm(FlaskForm):
    """ Create form for staff"""

    position = StringField(u"Должность", validators=[InputRequired(), Length(max=250)])
    department = StringField(u"Деператамент/Кластер", validators=[Optional(), Length(max=250)])
    submit = SubmitField("Сохранить")


class DocumentForm(FlaskForm):  # создаем общий класс паспорта
    """ Create form for documents"""

    view = SelectField(u"Выбрать", choices=['Паспорт гражданина России', 'Иностранный документ', 'Другое'])
    series = StringField(u"Серия документа", validators=[Optional(), Length(max=25)])
    number = StringField(u"Номер документа", validators=[InputRequired(), Length(max=25)])
    agency = StringField(u"Орган выдавший", validators=[Optional(), Length(max=250)])
    issue = DateField(u"Дата выдачи", format='%Y-%m-%d', validators=[InputRequired()])
    submit = SubmitField("Сохранить")


class AddressForm(FlaskForm):  # создаем общий класс адреса
    """ Create form for address"""

    view = SelectField(u"Выбрать", choices=['Адрес регистрации', 'Адрес проживания', 'Другое'])
    region = StringField(u"Регион", validators=[InputRequired(), Length(max=250)])
    address = StringField(u"Полный", validators=[InputRequired(), Length(max=250)])
    submit = SubmitField("Сохранить")


class ContactForm(FlaskForm):  # создаем общий класс контактов
    """ Create form for contact"""

    view = SelectField(u"Выбрать", choices=['Телефон', 'E-mail', 'Другое'])
    contact = StringField(u"Контакт", validators=[InputRequired(), Length(max=250)])
    submit = SubmitField("Сохранить")


class WorkplaceForm(FlaskForm):  # создаем общий класс рабочих мест
    """ Create model for workplaces"""

    period = StringField(u"Период работы", validators=[Optional(), Length(max=25)])
    workplace = StringField(u"Место работы", validators=[InputRequired(), Length(max=250)])
    address = StringField(u"Адрес организации", validators=[Optional(), Length(max=250)])
    position = StringField(u"Должность", validators=[InputRequired(), Length(max=250)])
    submit = SubmitField("Сохранить")


class RelationshipForm(FlaskForm):
    """ Create model for relationships"""

    relation = SelectField(u'Вид связи', choices=['Отец/Мать', 'Брат/Сестра', 'Супруг', 'Дети', 'Другое'])
    fullname = StringField(u"Полное ФИО", validators=[InputRequired(), Length(max=250)])
    birthday = DateField("Дата рождения", format='%Y-%m-%d', validators=[InputRequired()])
    address = StringField(u"Адрес", validators=[Optional(), Length(max=250)])
    workplace = StringField(u"Место работы", validators=[Optional(), Length(max=250)])
    contact = StringField(u"Контакт", validators=[Optional(), Length(max=250)])
    submit = SubmitField("Сохранить")


class ResumeForm(FlaskForm):  # форма для анкетных данных и служебных отметок
    """ Create form for create/edit resume page"""

    region = SelectField(u'Регион', choices=['Главный офис', 'Томск', 'РЦ Запад', 'РЦ Юг', 'РЦ Запад', 'РЦ Урал'])
    fullname = StringField(u"Полное ФИО", validators=[InputRequired(), Length(max=250)])
    previous = StringField(u"Изменение имени", validators=[Optional(), Length(max=250)])
    birthday = DateField("Дата рождения", format='%Y-%m-%d', validators=[InputRequired()])
    birthplace = StringField(u"Место рождения", validators=[Optional(), Length(max=250)])
    country = StringField(u"Гражданство", validators=[Optional(), Length(max=50)])
    snils = StringField(u"СНИЛС", validators=[Optional(), Length(min=11, max=11)])
    inn = StringField(u"ИНН", validators=[Optional(), Length(min=12, max=12)])
    education = StringField(u"Образование", validators=[Optional(), Length(max=250)])
    addition = TextAreaField(u"Дополнительно", validators=[Optional()])
    recruiter = StringField(u"Рекрутер", validators=[Optional(), Length(max=250)])
    submit = SubmitField("Принять")


class CheckForm(FlaskForm):  # форма для проверки
    """ Create form for page adding check """

    employee = TextAreaField(u"Проверка по кадровому учету", validators=[Optional()])
    workplace = TextAreaField(u"Проверка по месту работы", validators=[Optional()])
    document = TextAreaField(u"Проверка документов", validators=[Optional()])
    inn = TextAreaField(u"Проверка паспорта", validators=[Optional()])
    debt = TextAreaField(u"Проверка задолженностей", validators=[Optional()])
    bankruptcy = TextAreaField(u"Проверка банкротства", validators=[Optional()])
    bki = TextAreaField(u"Проверка кредитной истории", validators=[Optional()])
    courts = TextAreaField(u"Проверка по решениям судов", validators=[Optional()])
    affiliation = TextAreaField(u"Проверка аффилированности", validators=[Optional()])
    terrorist = TextAreaField(u"Проверка списка террористов", validators=[Optional()])
    mvd = TextAreaField(u"Проверка учетам МВД", validators=[Optional()])
    internet = TextAreaField(u"Проверка по открытым источникам", validators=[Optional()])
    cronos = TextAreaField(u"Проверка Кронос", validators=[Optional()])
    cros = TextAreaField(u"Проверка Крос", validators=[Optional()])
    addition = TextAreaField(u"Дополнительная информация", validators=[Optional()])
    pfo = BooleanField(u"Полиграф", default=False, validators=[])
    conclusion = SelectField(u'Результат', choices=['Без замечаний', 'С комментарием', 'Негатив',
                                                    'Снят с проверки', 'Сохранить'])
    comments = StringField(u"Комментарий", validators=[Optional(), Length(max=250)])
    submit = SubmitField("Принять")


class RegistryForm(FlaskForm):  # форма для согласования кандидата
    """ Create form for page registry"""

    comments = TextAreaField(u"Комментарий", validators=[Optional()])
    decision = SelectField(u'Решение', choices=['СОГЛАСОВАНО', 'СОГЛАСОВАНО С КОММЕНТАРИЕМ',
                                                'СОГЛАСОВАНО С РИСКОМ', 'ОТКАЗАНО В СОГЛАСОВАНИИ'])
    submit = SubmitField("Принять")


class PoligrafForm(FlaskForm):  # форма для результатов ПФО
    """ Create form for page adding poligraf"""

    theme = SelectField(u"Тема проверки", choices=['Проверка кандидата', 'Служебная проверка',
                                                   'Служебное расследование', 'Другое'])
    results = TextAreaField(u"Информация", validators=[InputRequired()])
    deadline = DateField("Дата проведения", format='%Y-%m-%d', default=TODAY, validators=[InputRequired()])
    submit = SubmitField("Принять")


class InvestigationForm(FlaskForm):  # форма для результатов служебных проверок
    """ Create form for page adding investigation"""

    theme = StringField(u"Тема проверки", validators=[InputRequired(), Length(max=250)])
    info = TextAreaField(u"Информация", validators=[InputRequired()])
    deadline = DateField("Дата окончания проверки", format='%Y-%m-%d', default=TODAY, validators=[Optional()])
    submit = SubmitField("Принять")


class InquiryForm(FlaskForm):  # форма для запросов из других организаций
    """ Create form for page adding inquiry"""

    info = TextAreaField(u"Информация", validators=[InputRequired()])
    initiator = StringField(u"Инициатор", validators=[InputRequired(), Length(max=250)])
    source = StringField(u"Источник", validators=[InputRequired(), Length(250)])
    deadline = DateField("Дата запроса", format='%Y-%m-%d', default=TODAY, validators=[InputRequired()])
    submit = SubmitField("Принять")


class InfoForm(FlaskForm):  # форма для формирования статинформации
    """ Create form for statistic information"""

    start = DateField("Начало периода", format='%Y-%m-%d', validators=[InputRequired()])
    end = DateField("Конец периода", format='%Y-%m-%d', validators=[InputRequired()])
    submit = SubmitField("Применить")
