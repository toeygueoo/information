from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import config_dict

# 1.创建app对象
app = Flask(__name__)
# 2.添加配置信息
app.config.from_object(config_dict["development"])
# 3.创建数据库对象
db = SQLAlchemy(app)
# 4.创建redis存储对象
redis_store = StrictRedis(host=config_dict["development"].REDIS_HOST,port=config_dict["development"].REDIS_PORT)
# 5.开启CSRF
CSRFProtect(app)
# 6.创建session对象
Session(app)

