from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


def timestamp():
    return int(time.time())


class ModelMixin(object):
    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{0}=({1})'.format(k, v) for k, v in self.__dict__.items())
        return '<{0}:\n\t{1}\n>'.format(class_name, '\n\t'.join(properties))

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)


class User(db.Model, ModelMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    password = db.Column(db.Text)


def db_init():
    db.create_all()


def add_one():
    u = User()
    u.username = '123123'
    u.save()


def find_one():
    u2 = User().find_by_id(10)
    print(u2)


def main():
    find_one()


if __name__ == '__main__':
    db_init()
    main()
