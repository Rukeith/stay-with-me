from flaskr import db
from sqlalchemy import text
from datetime import datetime
from sqlalchemy.dialects.mysql import ENUM, JSON


arrangment_user = db.Table(
    'arrangment_user',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id'), primary_key=True),
    db.Column('arrangement_id', db.Integer, db.ForeignKey('arrangement.arrangement_id'), primary_key=True)
)


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    # one-to-one
    search_condition = db.relationship(
        'SearchCondition',
        uselist=False,
        backref='user'
    )
    # many-to-many
    arrangements = db.relationship(
        'Arrangement',
        secondary=arrangment_user,
        lazy='subquery',
        backref=db.backref('participants', lazy='joined')
    )
    # one-to-many
    self_expenses_record = db.relationship(
        'ExpensesRecord',
        lazy='subquery',
        backref=db.backref('owner', lazy='joined')
    )
    # one-to-many
    chatrooms = db.relationship(
        'Chatroom',
        lazy='subquery',
        backref=db.backref('owner', lazy='joined')
    )

    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    classes = db.relationship('Classes', backref='classes')

    books = db.relationship('Book', backref='book')

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
    condition = db.Column(JSON, default=lambda: {})

    def __init__(self, search_condition_id, user_id, condition):
        self.search_condition_id = search_condition_id
        self.user_id = user_id
        self.condition = condition

    def __repr__(self):
        return '<SearchCondition %r>' % self.search_condition_id

    def save(self):
        db.session.add(self)
        db.session.commit()


class Arrangement(db.Model):
    __tablename__ = 'arrangement'
    arrangement_id = db.Column(db.Integer, primary_key=True)


class ExpensesRecord(db.Model):
    __tablename__ = 'expenses_record'
    record_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(
        ENUM('buy_candy', 'transfer_candy', 'spend_candy', 'exchange_money'),
        nullable=False
    )
    owner_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))


class Chatroom(db.Model):
    __tablename__ = 'chatroom'
    chatroom_id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    # one-to-many
    messages = db.relationship(
        'Message',
        lazy='subquery',
        backref=db.backref('chatroom', lazy='joined')
    )


class Message(db.Model):
    __tablename__ = 'message'
    message_id = db.Column(db.Integer, primary_key=True)
    message_type = db.Column(
        ENUM('video', 'img', 'link', 'text'),
        nullable=False
    )
    chatroom_id = db.Column(db.Integer, db.ForeignKey('chatroom.chatroom_id'))