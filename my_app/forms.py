from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# 创建Form
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()]) # 验证器确保提交的数据字段内容不为空或满足一定条件
    submit = SubmitField('Submit')