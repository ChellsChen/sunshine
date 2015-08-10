# sunshine

sunshine是我基于flask做的扩展和封装, 实现自动加载flask里 blueprints功能，自动加载restful api的功能，提供了一个插件式的结构,可以很方便的增加新的功能,

目录说明：
>* actions/：路由和视图函数接口目录
        actions/blueprints/   flask中蓝图接口
        actions/restfulapi/   基于restful的api接口
>* config/: flask内置的一些配置
>* packages/: 接口目录，开发的接口模块可以放在这里面
>* static/: 静态文件
>* templates/：模板文件
>* webapp.py: web应用的初始化
>* manage.py: 启动程序
            启动命令： python manage.py run
