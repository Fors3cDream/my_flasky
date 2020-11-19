from flask import Flask, render_template, flash
from flask import session, redirect, url_for
from my_app.catalog.models import User
from my_app.catalog.forms import NameForm
from flask import Blueprint
from my_app import db

app_blue = Blueprint("app_blue", __name__)


@app_blue.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app_blue.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Flask 使用上下文临时把某些对象变为全局课访问。有了上下文，便可以在试图函数中获取这些变量。
# 应用可以把数据存储在用户会话中，以便在请求之间“记住”数据。
# 用户会话是一种私有存储，每个连接到服务器的客户端都可以访问
# session是请求上下文中的变量 
@app_blue.route('/', methods=['GET', 'POST'])
def index():
    # return render_template('index.html')
    # name = None
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        # old_name = session.get('name')
        # if old_name is not None and old_name != form.name.data:
        #     flash('Looks loke you have changed your name!', 'warning') # flash消息 with category
        session['name'] = form.name.data
        # form.name.data = ''
        return redirect(url_for('app_blue.index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))

# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name=name)
