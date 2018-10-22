from flaskr import db
from sqlalchemy import text
from datetime import datetime
from sqlalchemy.dialects.mysql import ENUM, JSON


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    search_condition = db.relationship('SearchCondition', uselist=False, backref='user')

    teachers = db.relationship('TeacherUser', backref=db.backref('users', lazy='joined'), lazy='dynamic')

    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    classes = db.relationship('Classes', backref='classes')

    books = db.relationship('Book',backref='book')

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<Demo %r>' % self.username

    def save(self):
        db.session.add(self)
        db.session.commit()


class SearchCondition(db.Model):
    __tablename__ = 'search_condition'
    search_condition_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    condition = db.Column(JSON, server_default=text(r"{}"))


class TeacherUser(db.Model):
    __tablename__ = 'teacher_user'
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.teacher_id'))


class Teacher(db.Model):
    __tablename__ = 'teacher'
    teacher_id = db.Column(db.Integer, primary_key=True)
    participants = db.relationship('TeacherUser', backref=db.backref('teachers', lazy='joined'), lazy='dynamic')


class Classes(db.Model):
    __tablename__ = 'classes'
    class_id = db.Column(db.Integer, primary_key=True)


class Book(db.Model):
    __tablename__ = 'book'
    book_id = db.Column(db.Integer, primary_key=True)
    own_id = db.Colum(db.Integer,db.ForeignKey('user.id'))