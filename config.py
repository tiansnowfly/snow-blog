"""
# 添加app需要的配置信息
"""
from datetime import timedelta
import os

base_dir=os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # 修改静态文件自动刷新
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1)
    TEMPLATES_AUTO_RELOAD = True
    # 设置secret key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # 数据库位置
    SQLALCHEMY_DATABASE_URI = "mysql://root:txf1314520520@localhost/snowblog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 有关邮件相关配置
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['13487426939@qq.com']
    POSTS_PER_PAGE = 25
