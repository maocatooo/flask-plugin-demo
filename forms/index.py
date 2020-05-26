from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Regexp, Length


class LoginForm(FlaskForm):
    """
    页面的form
    """
    name = StringField(u'账号', validators=[DataRequired("不能为空"), Length(min=3, max=10, message=u"用户名长度3-10")])
    pwd = PasswordField(u'密码', validators=[DataRequired("不能为空"), Length(min=3, max=10, message=u"密码长度3-10")])
    sub = SubmitField('提交')

