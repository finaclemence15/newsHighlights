import os

class Config:

    # NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    # NEWS_SOURCES_BASE_URL='https://newapi.org/v2/sources?category&apiKey=5b632280af14422cac83cec2cc9314db'
    SOURCE_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=5b632280af14422cac83cec2cc9314db'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=5b632280af14422cac83cec2cc9314db'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    # SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}