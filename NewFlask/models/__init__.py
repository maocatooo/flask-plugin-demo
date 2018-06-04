# from app import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=True)
    pwd = db.Column(db.String(120),nullable=True)

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

    def __repr__(self):
        return '<User %r>' % self.name


if __name__=="__main__":
    # db.create_all()# 创建表结构
    ...
    from utils import enc_pwd
    username = "180dagaoge"
    pwd = enc_pwd("123456")
    user = User(username,pwd)
    db.session.add(user)
    db.session.commit()
