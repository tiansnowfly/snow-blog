from app import app
from flask import render_template,flash,redirect,url_for,request
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm,PostForm,RegisterForm
from app.models import Post,User


@app.route('/',methods=['GET','POST'])
@app.route('/login', methods=['GET', 'POST'])
# 当一个没有登录的用户访问被`@login_required`装饰器保护的视图函数时，装饰器将重定向到登录页面
# @login_required
def login():
    # current_user变量来自Flask_Login，在处理过程任何时候调用都能获取当前用户对象
    if current_user.is_authenticated: # 用户已经登录定位到主页
        return redirect(url_for('login'))
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        # 用户不存在或者密码错误
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('login'))
        # login_user()函数将用户状态转为登录
        login_user(user,remember=form.remember_me.data)
        return redirect(url_for('login'))
    return render_template('login.html',form=form)

# 用户登出
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    return render_template('register.html',form=form)
