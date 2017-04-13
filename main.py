#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from config import DevConfig

# 告诉Flask这是入口有点像是java的@controller效果
app = Flask(__name__)

# Import the views module
# 1.因为Flask Server 的Route使用main模块中查询路由函数(EG.home)的，
# 所以必须将views模块中的视图函数(路由函数)导入到main模块的全局作用域中。
# 2.因为 views 模块中导入了 main.app 对象，而 main 模块又需要导入 views 模块，
# 所以在 main.py 导入 views.py 之前一定要先生成 main.app 对象，否则会出现 NameError。
views = __import__('views')

# Get the config from object of DecConfig
# 使用 onfig.from_object() 而不使用 app.config['DEBUG']
# 是因为这样可以加载 class DevConfig 的配置变量集合，而不需要一项一项的添加和修改。
app.config.from_object(DevConfig)


if __name__ == '__main__':
    # Entry the application
    app.run()



