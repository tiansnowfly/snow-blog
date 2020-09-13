from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# 添加配置
app.config.from_object(Config)
"""
添加各种插件：数据库/login/bootstrap/mail
"""
db=SQLAlchemy(app) # 添加数据库
login=LoginManager(app) # 登录插件实例的创建
# login.login_view='login'
bootstrap=Bootstrap(app)

from app import routes
