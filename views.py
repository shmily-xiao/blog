#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template
from sqlalchemy import func
import datetime

from main import app
from models import db, User, Post, Tag, Comment, posts_tags
from wt_forms import CommentForm

# 1.获取主要的数据表对象, EG. posts
# 2.获取与该表由关联的数据表对象, EG. posts 与 comments 是 one to many 的关系,
#   posts 与 tags 是 many to many 的关系, 所以会 通过 posts 对象来获取 tags 对象和 comments 对象.
# 3.最后会补充获取这一 Jinja 模板中仍需要的数据对象, EG. recent/top_tags
def sidebar_data():
    """Set the sidebar function."""

    # Get post of recent
    recent = db.session.query(Post).order_by(
        Post.publish_date.desc()
    ).limit(5).all()

    # Get the tags and sort bt count of posts
    top_tags = db.session.query(
        Tag, func.count(posts_tags.c.post_id).label('total')
    ).join(
        posts_tags
    ).group_by(Tag).order_by('total DESC').limit(5).all()
    return recent, top_tags


# 指定 URL='/' 的路由规则
# 当访问 HTTP://server_ip/ GET(Default) 时，call home()
@app.route('/')
@app.route('/<int:page>')
def home(page=1):
    """View function for home page"""

    posts = Post.query.order_by(
        Post.publish_date.desc()
    ).paginate(page, 10)

    recent, top_tags = sidebar_data()

    return render_template('home.html',
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    """View function for post page"""
    # Form object:'Comment'
    form = CommentForm()
    # form.validate_on_submit() will be true and return the
    # data object to form instance from user enter
    # when the HTTP request is POST
    # form.validata_on_submit() 方法会隐式的判断该 HTTP 请求是不是 POST,
    # 若是, 则将请求中提交的表单数据对象传入上述的 form 对象并进行数据检验.
    if form.validate_on_submit():
        new_comment = Comment(name=form.name.data)
        new_comment.text = form.text.data
        new_comment.data = datetime.datetime.now()
        new_comment.post_id = post_id
        db.session.add(new_comment)
        db.session.commit()

    post = db.session.query(Post).get_or_404(post_id)
    tags = post.tags
    comments = post.comments.order_by(Comment.date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template('post.html',
                           post=post,
                           tags=tags,
                           comments=comments,
                           recent=recent,
                           top_tags=top_tags,
                           form=form)


@app.route('/tag/<string:tag_name>')
def tag(tag_name):
    """View function for tag page"""
    tag = db.session.query(Tag).filter_by(title=tag_name).first_or_404()
    posts = tag.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template('tag.html',
                           tag=tag,
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)


@app.route('/user/<string:username>')
def user(username):
    """View function for user page"""

    user = db.session.query(User).filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = sidebar_data()

    # render_template 作用和springMVC的model接口作用相似
    return render_template('user.html',
                           user=user,
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)






