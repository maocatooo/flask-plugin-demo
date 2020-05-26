import hashlib


def enc_pwd(old_pwd):
    """
    将传入的密码加盐加密
    :param old_pwd:
    :return:
    """
    pwd = str(old_pwd) + "!@#$%^&*"
    p = pwd.encode()
    pwd = hashlib.sha256(p).hexdigest()
    return pwd
