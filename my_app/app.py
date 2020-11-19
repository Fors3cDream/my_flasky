from flask import Flask, render_template
from flask import session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# Flask用这个秘钥保护用户会话，以防被篡改
app.config['SECRET_KEY'] = 'hard to guess string' 

bootstrap = Bootstrap(app)

moment = Moment(app)

# 创建Form
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()]) # 验证器确保提交的数据字段内容不为空或满足一定条件
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Flask 使用上下文临时把某些对象变为全局课访问。有了上下文，便可以在试图函数中获取这些变量。
# 应用可以把数据存储在用户会话中，以便在请求之间“记住”数据。
# 用户会话是一种私有存储，每个连接到服务器的客户端都可以访问
# session是请求上下文中的变量 
@app.route('/', methods=['GET', 'POST'])
def index():
    # return render_template('index.html')
    # name = None
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        # form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name=name)
