from forms.index import LoginForm
from flask import (
    Blueprint,
    render_template as render,
    flash,
    url_for,
    redirect,
    jsonify,
    request,

)
from flask import Blueprint
from flask_login import login_required, login_user, current_user, logout_user
from models import User as U


bp = Blueprint(__name__, 'index')


@bp.route("/", methods=["GET", "POST"])
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


@bp.route("/details", methods=['GET', 'POST'])
@login_required
def details():
    if request.method == 'GET':
        # print("log for current_user", current_user.__dict__, type(current_user.__dict__))
        return render("index/details.html")
    elif request.method == "POST":
        del current_user.__dict__['_sa_instance_state']
        return jsonify(current_user.__dict__)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".index"))

