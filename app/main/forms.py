# coding:utf8
from flask_wtf import Form
from flask_wtf import FlaskForm as Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class AppForm(Form):
    name = StringField(u'用户名：', validators=[Required()])
    psw = PasswordField(u'角色 ID：', validators=[Required()])
    submit = SubmitField(u'确认')
