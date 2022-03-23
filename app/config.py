import os
from typing import List, Type

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    CONFIG_NAME = "base"
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    DEBUG = True
    SECRET_KEY = os.getenv(
        "DEV_SECRET_KEY", "You can't see California without Marlon Widgeto's eyes"
    )


class QAConfig(BaseConfig):
    CONFIG_NAME = "qa"
    DEBUG = True
    SECRET_KEY = os.getenv(
        "QA_SECRET_KEY", "You can't see California without Marlon Widgeto's eyes"
    )


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig
]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}

