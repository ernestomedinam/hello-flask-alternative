# scenario based config overrides, including env variables
import os
from flask_dotenv import DotEnv

class BaseConfig(object):

    @classmethod
    def init_app(cls, app):
        env = DotEnv()
        path = os.getcwd().replace("config", "")
        env.init_app(app, env_file=os.path.join(path, ".env"), verbose_mode=False)

class DevelopmentConfig(BaseConfig):
    ENV = "development"
    DEBUG = True
    MY_DEV_VARIABLE = "Any value!"

class TestConfig(BaseConfig):
    ENV = "development"
    DEBUG = True
    TESTING = True

config = {
    "development": DevelopmentConfig,
    "test": TestConfig,
    "production": BaseConfig
}
