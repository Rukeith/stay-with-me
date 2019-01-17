from flaskr import db
from sqlalchemy import text
from datetime import datetime
from geoalchemy2.types import Geometry
from sqlalchemy.dialects.postgresql import UUID, ENUM, JSON


# arrangment_user = db.Table(
#     'arrangment_user',
#     db.Column(
#         'user_id',
#         UUID(as_uuid=True),
#         db.ForeignKey('user.user_id'),
#         primary_key=True
#     ),
#     db.Column(
#         'arrangement_id',
#         UUID(as_uuid=True),
#         db.ForeignKey('arrangement.arrangement_id'),
#         primary_key=True
#     ),
#     extend_existing=True
# )


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {
        'extend_existing': True,
    }

    user_id = db.Column(UUID(as_uuid=True), primary_key=True)
    # email = db.Column(db.String(150), unique=True, nullable=False)
    # username = db.Column(db.String(50), unique=True, nullable=False)
    # age = db.Column(db.Integer, server_default=text("18"))
    # sex = db.Column(ENUM('male', 'female', name='gender_types'), nullable=False)
    # role = db.Column(ENUM('sponsor', 'recipient', name='role_types'), nullable=False)

    # created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False, index=True)
    # updated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False, onupdate=datetime.utcnow, index=True)
    # deleted_at = db.Column(db.DateTime, nullable=True, index=True)

    # # one-to-one
    # search_condition = db.relationship(
    #     'SearchCondition',
    #     uselist=False,
    #     backref='user'
    # )
    # # many-to-many
    # arrangements = db.relationship(
    #     'Arrangement',
    #     secondary=arrangment_user,
    #     lazy='subquery',
    #     backref=db.backref('participants', lazy='joined')
    # )
    # # one-to-many
    # self_expenses_record = db.relationship(
    #     'ExpensesRecord',
    #     lazy='subquery',
    #     backref=db.backref('owner', lazy='joined')
    # )
    # # one-to-many
    # chatrooms = db.relationship(
    #     'Chatroom',
    #     lazy='subquery',
    #     backref=db.backref('owner', lazy='joined')
    # )

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return '<User %r>' % self.username

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def remove(self):
        self.deleted_at = datetime.utcnow()
        db.session.add(self)
        db.session.commit()


# class Permission(db.Model):
#     __tablename__ = 'permission'
#     __table_args__ = {
#         'extend_existing': True,
#     }

#     permission_id = db.Column(UUID(as_uuid=True), primary_key=True)
#     created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False, index=True)
#     updated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False, onupdate=datetime.utcnow, index=True)
#     deleted_at = db.Column(db.DateTime, nullable=True, index=True)

#     def __init__(self, **kwargs):
#         super(Permission, self).__init__(**kwargs)

#     def __repr__(self):
#         return '<Permission %r>' % self.permission_id

#     def save(self):
#         db.session.add(self)
#         db.session.commit()


# class SearchCondition(db.Model):
#     __tablename__ = 'search_condition'
#     __table_args__ = {
#         'extend_existing': True,
#     }

#     search_condition_id = db.Column(UUID(as_uuid=True), primary_key=True)
#     user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.user_id'))
#     condition = db.Column(JSON, default=lambda: {})
#     created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False, index=True)
#     updated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False, onupdate=datetime.utcnow, index=True)
#     deleted_at = db.Column(db.DateTime, nullable=True, index=True)

#     def __init__(self, **kwargs):
#         super(SearchCondition, self).__init__(**kwargs)

#     def __repr__(self):
#         return '<SearchCondition %r>' % self.search_condition_id

#     def save(self):
#         db.session.add(self)
#         db.session.commit()


class Arrangement(db.Model):
    __tablename__ = 'arrangement'
    __table_args__ = {
        'extend_existing': True,
    }

    arrangement_id = db.Column(UUID(as_uuid=True), primary_key=True)
    name = db.Column(db.String(255))
    dating_time = db.Column(db.DateTime, nullable=False, index=True)
    location = db.Column(Geometry(geometry_type='POINT', srid=4326))
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False, index=True)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False, onupdate=datetime.utcnow, index=True)
    deleted_at = db.Column(db.DateTime, nullable=True, index=True)

    def __init__(self, **kwargs):
        super(Arrangement, self).__init__(**kwargs)

    def __repr__(self):
        return '<Arrangement %r>' % self.arrangement_id

    def save(self):
        db.session.add(self)
        db.session.commit()


# class ExpensesRecord(db.Model):
#     __tablename__ = 'expenses_record'
#     __table_args__ = (
#         db.Index('ix_record_owner_receiver', 'owner_id', 'receiver_id'),
#         {
#             'extend_existing': True,
#         }
#     )

#     record_id = db.Column(UUID(as_uuid=True), primary_key=True)
#     actions = db.Column(
#         ENUM('buy_candy', 'transfer_candy', 'spend_candy', 'exchange_money', name='candy_action'),
#         nullable=False
#     )
#     owner_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.user_id'))
#     receiver_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.user_id'))
#     created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False, index=True)
#     updated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False, onupdate=datetime.utcnow, index=True)
#     deleted_at = db.Column(db.DateTime, nullable=True, index=True)

#     def __init__(self, **kwargs):
#         super(ExpensesRecord, self).__init__(**kwargs)

#     def __repr__(self):
#         return '<ExpensesRecord %r>' % self.record_id

#     def save(self):
#         db.session.add(self)
#         db.session.commit()


# class Chatroom(db.Model):
#     __tablename__ = 'chatroom'
#     __table_args__ = (
#         db.UniqueConstraint(
#             'owner_id',
#             'receiver_id',
#             name='uix_owner_receiver'
#         ),
#         db.Index('ix_chatroom_owner_receiver', 'owner_id', 'receiver_id'),
#         {
#             'extend_existing': True,
#         }
#     )

#     chatroom_id = db.Column(UUID(as_uuid=True), primary_key=True)
#     owner_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.user_id'))
#     receiver_id = db.Column(UUID(as_uuid=True), db.ForeignKey('user.user_id'))
#     created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False, index=True)
#     updated_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False, onupdate=datetime.utcnow, index=True)
#     deleted_at = db.Column(db.DateTime, nullable=True, index=True)

#     # one-to-many
#     messages = db.relationship(
#         'Message',
#         lazy='subquery',
#         backref=db.backref('chatroom', lazy='joined')
#     )

#     def __init__(self, **kwargs):
#         super(Chatroom, self).__init__(**kwargs)

#     def __repr__(self):
#         return '<Chatroom %r>' % self.chatroom_id

#     def save(self):
#         db.session.add(self)
#         db.session.commit()


# class Message(db.Model):
#     __tablename__ = 'message'
#     __table_args__ = {
#         'extend_existing': True,
#     }

#     message_id = db.Column(UUID(as_uuid=True), primary_key=True)
#     message_type = db.Column(
#         ENUM('video', 'img', 'link', 'text', name='message_types'),
#         nullable=False
#     )
#     text = db.Column(db.Text)
#     chatroom_id = db.Column(UUID(as_uuid=True), db.ForeignKey('chatroom.chatroom_id'))

#     def __init__(self, **kwargs):
#         super(Message, self).__init__(**kwargs)

#     def __repr__(self):
#         return '<Message %r>' % self.message_id

#     def save(self):
#         db.session.add(self)
#         db.session.commit()
