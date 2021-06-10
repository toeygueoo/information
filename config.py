from redis import StrictRedis

class Config(object):
    """工程配置父类"""
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
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400*2  # session 的有效期，单位是秒


class DevelopmentConfig(Config):
    """开发阶段的项目配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生产模式下的项目配置"""
    DEBUG = False
    # 修改数据库的链接对象
    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@服务器的地址:3306/information"

# 暴露一个接口给外界使用
# 使用方式：config_dict["development"]
config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}