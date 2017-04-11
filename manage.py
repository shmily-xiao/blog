#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from flask.ext.script import Manager, Server
from flask_script import Manager, Server
import main

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
    print main.app
    return dict(app=main.app)

if __name__ == '__main__':
    manager.run()