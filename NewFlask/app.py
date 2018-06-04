from flask import Flask
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    UserMixin,
    current_user,

)
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Regexp,Length
from flask_sqlalchemy import SQLAlchemy
from flask import (
    Blueprint,
    render_template as render,
    flash,
    url_for,
    redirect,
    jsonify,
    request,


)
from models import db
app = Flask(__name__)
app.secret_key = "NO20flask"
# login_manager = LoginManager()
# login_manager.init_app(app)
Bootstrap(app)
# from views.index import main as index_main

# app.register_blueprint(index_main)
login_manager = LoginManager()
login_manager.init_app(app)
# app.register_blueprint(login_main,url_prefix='/login')
login_manager.login_view = ".index"
login_manager.login_message="登录后进行访问"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# db = SQLAlchemy(app)
db.init_app(app)
db.app = app
from models import User as U


class LoginForm(FlaskForm):
    """
    页面的form
    """
    name = StringField(u'账号', validators=[DataRequired("不能为空"),Length(min=3, max=10,message=u"用户名长度3-10")])
    pwd = PasswordField(u'密码', validators=[DataRequired("不能为空"),Length(min=3, max=10,message=u"密码长度3-10")])
    sub = SubmitField('提交')


# from models import User

# class User(UserMixin):
#     import uuid
#     user = {"user_id": 1, "name": "zhangsan", "pwd": "123456"}
#
#     @classmethod
#     def get(cls, user_id):
#         print(user_id)
#         if user_id == cls.user["user_id"]:
#
#             return cls
#         else:
#             return None


@login_manager.user_loader
def load_user(userid):
    user = U.query.filter_by(id=userid).first()
    return user


@app.route("/",methods=["GET", "POST"])
def index():
    """
    登录主页
    :return:
    """
    form = LoginForm()
    if form.validate_on_submit():
        ...
        user_name = request.form.get('name', None)
        password = request.form.get('pwd', None)
        user = U.query.filter_by(name=user_name).first()
        if user is not None:

            # print("user pwd",user.pwd)
            # user = U(user_name)
            from utils import enc_pwd
            if enc_pwd(password) == user.pwd:
                ...
                # print("is_loging")
                login_user(user)
                return redirect(url_for(".details"))
            else:
                flash('密码错误.')
        flash('账号错误.')
    return render('index/index.html', form=form)


@app.route("/details",methods=['GET', 'POST'])
@login_required
def details():
    if request.method == 'GET':
        # print("log for current_user", current_user.__dict__, type(current_user.__dict__))
        return render("index/details.html")
    elif request.method == "POST":
        del current_user.__dict__['_sa_instance_state']
        return jsonify(current_user.__dict__)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".index"))


if __name__ == '__main__':
    conf = dict(
        host='0.0.0.0',
        port=8000,
        debug=True
    )
    app.run(**conf)
