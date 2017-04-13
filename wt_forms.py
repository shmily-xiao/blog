#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, TextField
from wtforms.validators import DataRequired, Length


# 表单类需要继承 Flask WTF 扩展提供的 Form 类
# 表单类中的一个类属性，就代表了一个字段，即输入框。wtforms 提供了多种类型的字段类
# 字段类的第一个参数为输入框标题，第二个参数为绑定到该字段的检验器列表，由 wtforms.validators 提供
class CommentForm(Form):
    """Form validator for comment."""
    # Set some field(InputBox) for enter the data.
    # patam validators: setup list of validators
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=255)]
    )

    # text = StringField(u'Comment', validators=[DataRequired()])
    text = TextField(u'Comment', validators=[DataRequired()])
