#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager, Server
from flask_script import Manager, Server
import main
import models

# Init manager object via app object
manager = Manager(main.app)

# Create a new commands: server
# This command will be run the Flask development_env server
manager.add_command("server", Server())

@manager.shell
def make_shell_context():
    """Ceate a python CLI.
    
    return:Default import object
    type:'Dict'
    """
    # 我们每在 models.py 中新定义一个数据模型, 都需要在 manager.py 中导入并添加到返回 dict 中.
    print "hello it's me:"
    print main.app
    # dict 的几个参数可以在manager shell 中可以查看，也只能查看这几个参数
    return dict(app=main.app,
                db=models.db,
                User=models.User,
                Post=models.Post,
                Comment=models.Comment,
                Tag=models.Tag)

if __name__ == '__main__':
    manager.run()