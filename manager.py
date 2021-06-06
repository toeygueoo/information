from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager


app = Flask(__name__)


class Config(object):
    """工程配置信息"""
    DEBUG = True
    # redis 配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 设置加密字符串
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    # flask_session的配置信息
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    # 不设置永久存储
    SESSION_PERMANENT = False
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400*2  # session 的有效期，单位是秒

# 添加配置信息
app.config.from_object(Config)
# 创建数据库对象
db = SQLAlchemy(app)
# 创建redis存储对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
# 开启CSRF
CSRFProtect(app)
# 创建session对象
Session(app)
# 创建manager管理类
manager = Manager(app)




@app.route('/index')
def index():
    return "hello world!"

if __name__ == '__main__':
    # python xxx.py runserver -h -p -d
    manager .run()