from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = ".index"
login_manager.login_message = "登录后进行访问"
db = SQLAlchemy()


@login_manager.user_loader
def load_user(userid):
    from models import User as U
    user = U.query.filter_by(id=userid).first()
    return user

