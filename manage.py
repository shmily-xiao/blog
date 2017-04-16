#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# from flask_script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager, Server

import blog.models as models
from blog import create_app

# Get the ENV from os_environ
# 现在的 manager shell 在每次启动的时候，都会获取一次 OS 的环境变量，并以此来创建 app 对象。
# 默认使用 DevConfig 配置
env = os.environ.get('BLOG_ENV', 'dev')

# Create thr app instance via Factory Method
app = create_app('blog.config.%sConfig' % env.capitalize())

# Init manager object via app object
manager = Manager(app)

# Init migrate object via app and db object
# migrate 移动
migrate = Migrate(app, models.db)

# Create a new commands: server
# This command will be run the Flask development_env server
manager.add_command("server", Server())
# manager.add_command("server", Server(host='127.0.0.1', port=8089))
# new command
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    """Ceate a python CLI.
    
    return:Default import object
    type:'Dict'
    """
    # 我们每在 models.py 中新定义一个数据模型, 都需要在 manager.py 中导入并添加到返回 dict 中.
    print ("hello i am the manage shell: ", app)

    # dict 的几个参数可以在manager shell 中可以查看，也只能查看这几个参数
    return dict(app=app,
                db=models.db,
                User=models.User,
                Post=models.Post,
                Comment=models.Comment,
                Tag=models.Tag)

if __name__ == '__main__':
    manager.run()