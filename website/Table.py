import index

db = index.db

class CalcTable(db.Model):
    __tablename__ = 'calcs'
    id = db.Column(db.Integer, primary_key=True)
    w = db.Column(db.Float)
    h = db.Column(db.Float)
    BMI = db.Column(db.Float)
    Desc = db.Column(db.String(64))


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship('User', backref='role')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    username = db.Column(db.String(64), unique=True, index=True)
