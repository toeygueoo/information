from flask import Flask


app = Flask(__name__)


class Config(object):
    """工程配置信息"""
    DEBUG = True
# 添加配置信息
app.config.from_object(Config)

@app.route('/index')
def index():
    return "hello world!"

if __name__ == '__main__':
    app.run()