# coding: utf-8

from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField(u'用户名:', validators=[Required()])
    psw = PasswordField(u'密码:', validators=[Required()])
    submit = SubmitField(u'确定')