from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from config import config_dict

app = Flask(__name__)





# 1.添加配置信息
app.config.from_object(config_dict["development"])
# 2.创建数据库对象
db = SQLAlchemy(app)
# 3.创建redis存储对象
redis_store = redis.StrictRedis(host=config_dict["development"].REDIS_HOST,port=config_dict["development"].REDIS_PORT)
# 4.开启CSRF
CSRFProtect(app)
# 5.创建session对象
Session(app)
# 6.创建manager管理类
manager = Manager(app)




@app.route('/index')
def index():
    return "hello world!"

if __name__ == '__main__':
    # python xxx.py runserver -h -p -d
    manager .run()