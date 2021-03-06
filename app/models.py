from app import db
from flask_login import UserMixin # 用于登录认证等
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from app import login

"""
flask_login用户会话中存储唯一标识符来跟踪用户
每当已登录用户导航到新的页面，Flask_Login将从会话中检索用户ID，然后将该用户的实例加载到内存中
"""
@login.user_loader
def user_loader(id):
    return User.query.get(int(id))

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# 存储用户的动态
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)