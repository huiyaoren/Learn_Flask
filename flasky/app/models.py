# coding: utf8
from . import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

    # todo have not tested
    @staticmethod
    def seed():
        db.session.add_all(map(lambda r: Role(name=r), ['Guest', 'Administrator']))
        db.session.commit()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

    @staticmethod
    def on_created(target, value, oldvalue, initiator):
        # target.role = Role.query.filter_by(name='Guest').first()
        target.role_id = 1


db.event.listen(User.username, 'set', User.on_created)
