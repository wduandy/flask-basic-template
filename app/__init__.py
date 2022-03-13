from flask import Flask
from flask_login import LoginManager


login_manager = LoginManager()
login_manager.login_view = 'login'

def create_app():
    from app.models import config_db
    from app.views import config_views
    name = __name__.split('.')[0]
    app = Flask(name)
    app.secret_key = 'SUPERSECRETKEY'
    app.config.from_pyfile('config.cfg')
    app.config['ENV'] = 'development'
    app.template_folder = 'views/templates'
    app.static_folder = 'views/static'
    config_db(app)
    config_views(app)
    login_manager.init_app(app)
    return app
