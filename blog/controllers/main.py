#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

from flask import flash, url_for, redirect, render_template, Blueprint
from blog.forms import LoginForm, RegisterForm

from blog.models import db, User

main_blueprint = Blueprint(
    'main',
    __name__,
    # path.join( 'template/main')
    template_folder=path.join(path.pardir, 'template', 'main'),
    url_prefix='/main'
)


@main_blueprint.route('/')
def index():
    return redirect(url_for('blog.home'))


@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """View function for login."""
    # Will be check the account whether rigjt
    # LoginForm.validate() 会被执行
    form = LoginForm()

    print ("*********************login*******************")

    if form.validate_on_submit():
        flash('You have been logged in.', category="success")
        return redirect(url_for("blog.home"))
    return render_template('login.html',
                           form=form)


@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    """View function for Register"""

    # RegisterForm.validate() 会被执行
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        password=form.password.data)
        db.session.add(new_user)
        db.session.commit()

        flash('Your user has been created, please login.',
              category="success")
        return redirect(url_for('main.login'))
    return render_template('register.html',
                           form=form)


@main_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    """View function for logout"""

    flash('You have been logged out.', category="success")
    return redirect(url_for('blog.home'))

