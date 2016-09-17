# coding: utf8

from flask import render_template, session, redirect, url_for, current_app, jsonify
from .. import db
from ..models import User, Role
from ..email import send_email
from . import main
from .forms import NameForm, AppForm


@main.route('/ass', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            # if current_app.config['FLASKY_ADMIN']:
            #     send_email(current_app.config['FLASKY_ADMIN'], 'New User',
            #                'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))


@main.route('/app', methods=['GET', 'POST'])
def app():
    form = AppForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
        return redirect(url_for('.app'))
    # 种子函数 ok
    # 测试数据库事件 ok

    # 打印 Role 表内容 ok
    user_data = User.query.all()
    role_data = Role.query.all()
    return render_template('app.html',
                           form=form,
                           user_data=user_data,
                           role_data=role_data)

@main.route('/delete', methods=['delete'])
def delete():
    return jsonify(result=4)

@main.route('/post', methods=['post'])
def post():

    return jsonify(asdf=5432)