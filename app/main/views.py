# coding: utf-8
from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm
from .. import db
from .. models import User

@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def index():
    form = NameForm()
    # 读取数据库内容
    # 添加数据库内容
    if form.validate_on_submit():
        pass
    return render_template('index.html',
                           form=form
                           )
    # return "hello world again"s