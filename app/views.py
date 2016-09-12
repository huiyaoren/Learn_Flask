# coding: utf-8

from . import app

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # 读取数据库内容
    # 添加数据库内容

    return "hello world again"