from flaskr import db
from sqlalchemy import text
from datetime import datetime
from sqlalchemy.dialects.mysql import ENUM, JSON


arrangment_user = db.Table(
    'arrangment_user',
    db.Column(
        'user_id',
        db.Integer,
        db.ForeignKey('user.user_id'),
        primary_key=True
    ),
    db.Column(
        'arrangement_id',
        db.Integer,
        db.ForeignKey('arrangement.arrangement_id'),
        primary_key=True
    ),
    extend_existing=True
)


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {
        "useexisting": True
    }

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)

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

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return '<User %r>' % self.username

    def save(self):
        db.session.add(self)
        db.session.commit()


class SearchCondition(db.Model):
    __tablename__ = 'search_condition'
    __table_args__ = {
        "useexisting": True
    }

    search_condition_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    condition = db.Column(JSON, default=lambda: {})

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return '<SearchCondition %r>' % self.search_condition_id

    def save(self):
        db.session.add(self)
        db.session.commit()


class Arrangement(db.Model):
    __tablename__ = 'arrangement'
    __table_args__ = {
        "useexisting": True
    }

    arrangement_id = db.Column(db.Integer, primary_key=True)

    def __init__(self, **kwargs):
        super(Arrangement, self).__init__(**kwargs)

    def __repr__(self):
        return '<Arrangement %r>' % self.arrangement_id

    def save(self):
        db.session.add(self)
        db.session.commit()


class ExpensesRecord(db.Model):
    __tablename__ = 'expenses_record'
    __table_args__ = (
        db.Index('ix_owner_receiver', 'owner_id', 'receiver_id'),
    )

    record_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(
        ENUM('buy_candy', 'transfer_candy', 'spend_candy', 'exchange_money'),
        nullable=False
    )
    owner_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __init__(self, **kwargs):
        super(ExpensesRecord, self).__init__(**kwargs)

    def __repr__(self):
        return '<ExpensesRecord %r>' % self.record_id

    def save(self):
        db.session.add(self)
        db.session.commit()


class Chatroom(db.Model):
    __tablename__ = 'chatroom'
    __table_args__ = (
        db.UniqueConstraint(
            'owner_id',
            'receiver_id',
            name='uix_owner_receiver'
        ),
        db.Index('ix_owner_receiver', 'owner_id', 'receiver_id'),
    )

    chatroom_id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    # one-to-many
    messages = db.relationship(
        'Message',
        lazy='subquery',
        backref=db.backref('chatroom', lazy='joined')
    )

    def __init__(self, **kwargs):
        super(Chatroom, self).__init__(**kwargs)

    def __repr__(self):
        return '<Chatroom %r>' % self.chatroom_id

    def save(self):
        db.session.add(self)
        db.session.commit()


class Message(db.Model):
    __tablename__ = 'message'
    __table_args__ = {
        "useexisting": True
    }

    message_id = db.Column(db.Integer, primary_key=True)
    message_type = db.Column(
        ENUM('video', 'img', 'link', 'text'),
        nullable=False
    )
    chatroom_id = db.Column(db.Integer, db.ForeignKey('chatroom.chatroom_id'))

    def __init__(self, **kwargs):
        super(Message, self).__init__(**kwargs)

    def __repr__(self):
        return '<Message %r>' % self.message_id

    def save(self):
        db.session.add(self)
        db.session.commit()
