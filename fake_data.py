#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import random

from blog.models import db, User, Tag, Post

user = User(id=1, username='shmily', password='qazwsx')
db.session.add(user)
db.session.commit()

user = db.session.query(User).first()
tag_one = Tag(name='Python')
tag_two = Tag(name='Flask')
tag_three = Tag(name='SQLAlchemy')
tag_four = Tag(name='Java')
tag_list = [tag_one, tag_two, tag_three, tag_four]

s = 'EXAMPLE TEXT'

for i in range(100):
    new_post = Post(title='Post' + str(i+1))
    new_post.user = user
    new_post.publish_date = datetime.datetime.now()
    new_post.text = s + str(i+1)
    new_post.tags = random.sample(tag_list, random.randint(1, 3))
    db.session.add(new_post)

db.session.commit()
