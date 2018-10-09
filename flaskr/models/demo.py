from flaskr import db


class Demo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Demo %r>' % self.username


def createData():
    admin = Demo(username='admin', email='admin@example.com')
    db.session.add(admin)
    db.session.commit()


def queryData():
    result = Demo.query.all()
    print('Result = %s', result)