# 基于flask封装的web框架

-----

>  本框架在flask基础上封装的，集成了flask-ext-form, flask-ext-login, flask-ext-restful, flask-ext-sqlalchemy等模块。

> 实现自动加载flask里 blueprints功能，自动加载restful api的功能。

> 这个框架带有一个简易的登录系统。


### 目录说明：

#### actions/：路由和视图函数接口目录

*  actions/blueprints/   flask中蓝图接口
*  actions/restfulapi/   基于flask-ext-restful的api接口
*  actions/plugins/      在flask自带的接口add_url_rule上实现的基于restful思想的api接口

#### config/: flask内置的一些配置

#### packages/: 接口目录，开发的接口模块可以放在这里面

#### static/: 静态文件

#### templates/：模板文件

#### webapp.py: web应用的初始化

#### manage.py: 启动程序

启动命令： python manage.py run
数据库初始化命令： python manage.py createdb


----------
第一次启动程序之前，要先初始化数据库(创建用户表，添加用户名和密码)

