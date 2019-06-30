#！/user/bin/python
# -*- coding:utf-8 -*-
# @Time: 2018/8/29 21:14
# @Author: 小民


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="color:blue">Hello World!</h1>'


if __name__ == '__main__':
    app.run()