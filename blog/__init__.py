#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for

from config import DevConfig
from blog.models import db
from blog.controllers import blogs
from blog.controllers import main
from blog.extensions import bcrypt


def create_app(object_name):
    """Create the app instance via 'Factory Method'"""
    # 告诉Flask这是入口有点像是java的@controller效果
    app = Flask(__name__)

    # Get the config from object of DecConfig
    # 使用 onfig.from_object() 而不使用 app.config['DEBUG']
    # 是因为这样可以加载 class DevConfig 的配置变量集合，而不需要一项一项的添加和修改。
    # app.config.from_object(DevConfig)
    # 上面是使用工厂模式之前的样子，Devconfig是写死的

    # Set the app config
    app.config.from_object(object_name)

    # Import the views module
    # 1.因为Flask Server 的Route使用main模块中查询路由函数(EG.home)的，
    # 所以必须将views模块中的视图函数(路由函数)导入到main模块的全局作用域中。
    # 2.因为 views 模块中导入了 main.app 对象，而 main 模块又需要导入 views 模块，
    # 所以在 main.py 导入 views.py 之前一定要先生成 main.app 对象，否则会出现 NameError。
    # views = __import__('views')
    # 重构之前

    # Will be load the SQLALCHEMY_DATABASE_URL from config.py to db object
    db.init_app(app)
    # Init the Flask-Bcryt via app object
    bcrypt.init_app(app)



    @app.route('/')
    def index():
        return redirect(url_for('blog.home'))


    # 将新建的蓝图对象 blog_blueprint 注册到 app 中
    # 每次新建一个蓝图都需要在这里添加一个
    app.register_blueprint(blogs.blog_blueprint)
    app.register_blueprint(main.main_blueprint)

    # if __name__ == '__main__':
    #     # Entry the application
    #     app.run()
    return app

    # 以往我们还需要在 main.py 中导入视图模块 views 才能够使这些视图函数生效，
    # 现在因为我们将蓝图对象注册到了 app 对象中，而且 index() 路由函数还重定向
    # 到了 'blog/home() 中 。所以现在我们并不需要将 blog 模块导入到
    # blog/__init__.py 也能使这些视图函数生效了。



