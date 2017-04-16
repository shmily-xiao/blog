#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms.validators import DataRequired, Length, EqualTo, URL
from wtforms import (
    StringField,
    TextField,
    TextAreaField,
    PasswordField,
    BooleanField,
    ValidationError
)

from blog.models import User


# 表单类需要继承 Flask WTF 扩展提供的 Form 类
# 表单类中的一个类属性，就代表了一个字段，即输入框。wtforms 提供了多种类型的字段类
# 字段类的第一个参数为输入框标题，第二个参数为绑定到该字段的检验器列表，由 wtforms.validators 提供

# 这个类的作用类似于java中@valid注解 在调用的controller,
# 里面有一个BindingResult的接口帮你判断是否参数过了校验
class CommentForm(Form):
    """Form validator for comment."""
    # Set some field(InputBox) for enter the data.
    # patam validators: setup list of validators
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=20)]
    )
    text = TextAreaField(u'Comment', validators=[DataRequired()])


class LoginForm(Form):
    """Login Form."""
    username = StringField('Username', validators=[DataRequired(), Length(max=255)])
    password = PasswordField('Password', validators=[DataRequired])

    def validate(self):
        """Validartor for check the account information"""
        print "********************LoginForm validate******************"
        # check_validate = super(LoginForm, self).validate()
        # super 是父类的方法，对父类的方法的重写
        # if not check_validate:
        #     return False

        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('Invalid username or password.')
            return False

        # Check the password whether right.
        if not user.check_password(self.password.data):
            # self.password.errors.append('Invalid username or password')
            self.username.errors.append('Invalid username or password')
            return False

        return True


class RegisterForm(Form):
    """Register Form."""
    username = StringField('Username', validators=[DataRequired(), Length(max=255)])
    password = PasswordField('Password', validators=[DataRequired])
    # or confirm ??
    comfirm = PasswordField('Confirm Password', validators=[DataRequired, EqualTo('password')])

    def validate(self):
        check_validate = super(RegisterForm, self).validate()

        # If validator no pass
        if not check_validate:
            return False

        # Check the user Whether already exist;
        user = User.query.filter_by(username=self.username.data).first()

        if user:
            self.username.errors.append('User with that name already exists.')
            return False

        return True


class PostForm(Form):
    """Post form"""
    title = StringField('Title', [DataRequired(), Length(max=255)])
    text = TextAreaField('Blog Content', [DataRequired])
