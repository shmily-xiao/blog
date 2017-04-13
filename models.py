#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
from main import app

# init the sqlalchemy object
# will be load the SQLALCHEMY_DATABASE_URL from config.py
# SQLAlchemy 会自动的从app对象中的DevConfig 中加载连接数据库的配置项
# db 是 class SQLAlchemy 的实例化对象, 包含了 SQLAlchemy 对数据库操作的支持类集.
db = SQLAlchemy(app)


# 我们每在 models.py 中新定义一个数据模型, 都需要在 manager.py 中导入并添加到返回 dict 中.
class User(db.Model):
    """Represent Proected users."""

    # Set the name for table
    __tablename__ = 'user'
    # id 和 username，password都是user的属性
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    print 'user is run'

    # 我们还需要在父表类 User 中定义出这种 one to many 的关系：
    # 会在 SQLAlchemy 中创建一个虚拟的列，该列会与 Post.user_id (db.ForeignKey) 建立联系。
    # 这一切都交由 SQLAlchemy 自身管理。
    # backref：用于指定表之间的双向关系，如果在一对多的关系中建立双向的关系，
    #          这样的话在对方看来这就是一个多对一的关系。
    # lazy：指定 SQLAlchemy 加载关联对象的方式。
    #       lazy=subquery: 会在加载 Post 对象后，将与 Post 相关联的对象全部加载，这样就可以减少
    #           Query 的动作，也就是减少了对 DB 的 I/O 操作。
    #           但可能会返回大量不被使用的数据，会影响效率。
    #       lazy=dynamic: 只有被使用时，对象才会被加载，并且返回式会进行过滤，
    #            如果现在或将来需要返回的数据量很大，建议使用这种方式。Post 就属于这种对象。
    posts = db.relationship(
        'Post',
        backref='users',
        lazy='dynamic'
    )

    # 这个应该就是java中的构造函数了 self是java中的this
    # 如果我们不写下面这个构造器，SQLAlchemy会帮我创建一个 这样的构造器 def __init__(self, id, username, password)
    # def __init__(self, username):
    #     print 'user username __init__ is run'
    #     self.username = username

    def __init__(self, id, username, password):
        print 'user id, username, password __init__ is run'
        self.id = id
        self.username = username
        self.password = password

    # 该方法返回一个对象的 字符串表达式. 与 __str__() 不同, __repr__返回的是字符串表达式, 能被 eval() 处理
    # __str__返回的是字符串, 不能被 eval() 处理得到原来的对象, 但与 print 语句结合使用时, 会被默认调用.
    # 与 repr() 类似,
    # 将对象转化为便于供 Python 解释器读取的形式, 返回一个可以用来表示对象的可打印字符串.
    # 直接调用对象实际上是隐式的调用了 User.__repr__(user)
    # __repr__() 其定义了类实例化对象的可打印字符串表达式
    def __repr__(self):
        """Define the string format for instance of User."""
        print 'user __repr__ is run'
        return "<Model User '{}'>".format(self.username)

# 关联表，表示多对多的关系
# 实际上 db.Table 对象对数据库的操作比 db.Model 更底层一些。
# 后者是基于前者来提供的一种对象化包装，表示数据库中的一条记录。
# posts_tags 表对象之所以使用 db.Table 不使用 db.Model 来定义，
# 是因为我们不需要对 posts_tags (self.name)进行直接的操作(不需要对象化)，
# posts_tags 代表了两张表之间的关联，会由数据库自身来进行处理。
posts_tags = db.Table('posts_tags',
                      db.Column('post_id', db.INTEGER, db.ForeignKey('posts.id')),
                      db.Column('tag_id', db.INTEGER, db.ForeignKey('tags.id')))


# 我们还需要在父表类 User 中定义出这种 one to many 的关系
class Post(db.Model):
    """Represents Proected posts."""
    __tablename__ = 'posts'
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime)

    # set the foreign key for Post
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'))

    # Establish contact with Comment's Foreignkey:post_id
    comments = db.relationship(
        'Comment',
        backref='posts',
        lazy='dynamic'
    )

    # many to many: post <==> tags
    # seconddary(次级)：会告知 SQLAlchemy 该 many to many 的关联保存在 posts_tags 表中
    # backref：声明表之间的关系是双向，帮助手册 help(db.backref)。
    # 需要注意的是：在 one to many 中的 backref 是一个普通的对象，
    # 而在 many to many 中的 backref 是一个 List 对象。
    tags = db.relationship(
        'Tag',
        secondary=posts_tags,
        backref=db.backref('posts', lazy='dynamic')
    )

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Model Post '{}'>".format(self.title)


# 评论
class Comment(db.Model):
    """Represent Proected comments"""

    __tablename__ = 'comments'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.INTEGER, db.ForeignKey('posts.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Model Comment '{}'".format(self.name)


class Tag(db.Model):
    """Represent Protected tags."""

    __tablename__ = 'tags'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Model Tag '{}'".format(self.name)






