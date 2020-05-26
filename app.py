from flask import Flask
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    UserMixin,
    current_user,

)

from plugin import db
from plugin import login_manager


app = Flask(__name__)
app.secret_key = "flask"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)
db.init_app(app)
db.app = app
login_manager.init_app(app)


if __name__ == '__main__':
    conf = dict(
        host='0.0.0.0',
        port=8001,
        debug=True
    )
    app.run(**conf)
