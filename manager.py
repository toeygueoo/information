from flask import Flask
from flask_script import Manager
from info import app

# 7.创建manager管理类
manager = Manager(app)

@app.route('/index')
def index():
    return "hello world!"

if __name__ == '__main__':
    # python xxx.py runserver -h -p -d
    manager .run()