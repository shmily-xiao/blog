#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_bcrypt import Bcrypt
from flask_login import LoginManager


# Create the Flask-Bcrypt's instance
# 以后所有的扩展都会在这里
# 所以这里我们使用 Bcrypt 哈希算法，这是一种被刻意设计成抵消且缓慢的哈希计算方式，从而极大的加长了暴力破解的时间和成本，以此来保证安全性。
bcrypt = Bcrypt()

# Create the Flask-Login's instance
login_manager = LoginManager()


# Setup the configuration for login manager.
#     1. Set the login page.
#     2. Set the more stronger auth-protection.
#     3. Show the information when you are logging.
#     4. Set the Login Messages type as `information`.
login_manager.login_view = "main.login"
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page."
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(user_id):
    """Load the user's info."""

    from models import User
    return User.query.filter_by(id=user_id).first()