# django开发指南
* 查看django版本<br>
    python -m django --version
    
# 创建django项目
    django-admin startproject project-name

# 项目结构
    prject-name
        manage.py
        prject-name
            __init__.py
            setting.py
            urls.py
            wsgi.py
            
# 启动项目
    python manage.py runserver
    
# 创建应用
    python manage.py startapp firms
    
# url 配置
    from django.urls import path
    from . import views    
    urlpatterns = [
        path('index/', views.index),
    ]
# url include
    将其他应用的url包含进来
    path('user/', include('user.urls'))
    
# url path参数
    path(route, view, kwargs, name)  
    route 为需要匹配的url路径，这里会忽略到参数
    view 处理试图
    kwargs 任意的关键字参数可以作为字典传入给试图函数
    name 给route路径取一个别人，在其他地方是使用别名就可以了，后续修改了匹配路径，就在一个地方修改即可

# models编写
    1.在models中写入如下代码，
    from django.db import models    
    class UserInfo(models.Model):
        username = models.CharField(max_length = 32)
        passwd = models.CharField(max_length = 32)
        phone = models.CharField(max_length = 24)
        email = models.EmailField()
    注意，
        a. 所有的models都必须以django.db.models.Model作为基类
        b.创建的表名称为 应用名称_类名称
        c.默认会给每一个表添加一个主键，名称为id
        d.默认使用sqllit数据库，如果使用mysql请在settings配置文件中配置DATEBASE 部分
        
    
# 数据库创建

    可以先通过sqlmirgate查看某个工程的sql语句: python manage.py sqlmigrate appname version_num
        python manage.py sqlmigrate user 001
    也可以使用check命令进行检查
        python manage.py check
    通常情况下使用如下2个命令即可
        python manage.py makemigrations   --为模板的改变生成迁移文件
        python manage.py migrate          -- 应用数据库迁移
        

# manage 相关的命令
    python manage.py shell  --进入一个携带了django环境变量的python shell交互页面
    
    python manage.py createsuperuser -- 创建django管理端的超级管理员
    输入上一条命令后，会需要你输入账号密码[如果你没有输入账号，默认就是你机器的用户名]
    
# register models 到 django admin中
    from django.contrib import admin    
    from .models import UserInfo    
    admin.site.register(UserInfo)
    

# 模板使用
    1.模板定义文件
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{% block title %}{% endblock %}</title>
        <style>
            {% block selfCss %}{% endblock %}
        </style>
        {% block selfJs %} {%  endblock %}
    </head>
    <body>
        {% block body %}{% endblock %}
    </body>
    </html>
    
    2.模板使用文件
    {% extends 'tpl.html' %} ## 说明该页面使用的是哪个模板
    
    {% block title %} 用户管理 {% endblock %}  ##需要替换的模板
    
    {% block body %}
        用户管理界面body
        {% include 'foot.html' %} ## 包含其他页面
    {% endblock %}

# 数据库crud操作
    
    def add(request):
        models.UserInfo.objects.create(username='sky', pwd='aaa111', age=99)

        # obj = models.UserInfo(username='bnmyni', pwd='aaa111')
        # obj.save()
        return HttpResponse('新增成功')


    def list(request):
        querySet = models.UserInfo.objects.all() ## 这种方式返回的是QuerySet<object extends Model>

        # models.UserInfo.objects.all().values()  这种方式返回的是一个QuerySet<dict>
        # models.UserInfo.objects.all().values_list() 这种方式返回的是QuerySet<元组set>
        for row in querySet:
            print(row.id)
            print(row.username)
            print(row.pwd)
            print(row.age)
        return HttpResponse(querySet)

    def getOne(request):
        querySet = models.UserInfo.objects.filter(username='sky', pwd='aaa111')
        return HttpResponse(querySet)
    
    def delete(request):
        models.UserInfo.objects.filter(username='sky').delete()

# 数据库多对多操作
    1.多对多模型写法
        class Books(models.Model):
        name = models.CharField(max_length=128)
        r = models.ManyToManyField("UserInfo")
        
    2.多对多view操作
        def manyTomany(request):
            book = models.Books.objects.get(id=1)
            book.r.add(1)
            book.r.add(2,3,4,5)
            book.r.add(*[1, 2, 3, 4, 5, 8])
        
            book.r.remove(2)
            book.r.remove(2, 3, 4, 5)
            book.r.remove(*[1, 2, 3, 4, 5, 8])
        
            book.r.clear() ## 删除所有id=1
        
            book.r.set([2, 3, 4, 5]) ## 只保留1-2,1-3,1-4,1-5
        
            book.r.update()
    
# view 获取不同类型的值
    获取GET请求参数
        request.GET
    获取POST请求参数
        request.POST   
    获取普通值  request.GET.get("username")
    
    获取多选值 request.POST.getlist("users")
    
    获取文件 request.FILES.get('upload_file')

# urls 中将一个url路由到一个类
    一般来说一个url是路由到一个指定的方法上面，如果需要将一个url路由到一个类上面则需要继承django.views.View
    from django.views import View
    class Home(View):
        def dispatch(self, request, *args, **kwargs):
            print('before filter...')
            rst = super(Home, self).dispatch(request, *args, **kwargs)
            print('after filter...')
            return rst
    
        def get(self, request):
            print('home get..')
            return render(request, 'home.html')
    
        def post(self, request):
            print('home post..')
            return render(request, 'home.html')

# 使用Form进行表单的验证
    django.forms提供了一个表单验证功能,django.forms.fields用于定义字段的类型，django.forms.widgets用于定义该字段在html中表现形式
    
    from django import forms
    from django.shortcuts import render, HttpResponse
    from django.forms import widgets
    from django.forms import fields
    class UserFrom(forms.Form):
        user = fields.CharField(error_messages='用户名不能为空', widgets = widgets.CheckboxInput(attrs={'css', 'c1'}))
        pwd = fields.CharField(max_length=20,
                              min_length=8,
                              error_messages={"max_length": "长度不能大于20", "min_length": "密码长度不能小于6"},
                              widgets = widgets.PasswordInput(attrs={'css': "c2"}))
        email = fields.EmailField()
    
    def login(request):
        if request.method == 'GET':
            return HttpResponse('OK GET...')
        elif request.method == 'POST':
            obj = UserFrom()
            flag = obj.is_valid()
            if flag:
                # 这里就可以直接保存到数据库了 models.UserInfo.create(**obj.cleaned_data)
                ## {{obj.user}} 可以在页面上生成html  {{obj.user.}} {{obj.erros.user.0}}
                ## {{obj.as_p}} {{obj.as_ul}} {{obj.as_table}} 可以生成<p> <ul> 或者<table>
                return HttpResponse(obj.cleaned_data)
            else:
                return HttpResponse(obj.errors)
            
# csrf 防护
    django 默认是开启了csrf防护的，在settings配置了'django.middleware.csrf.CsrfViewMiddleware'中间件，如果不需要可以注释掉
    
    如果需要，则需要在每个页面上都加上 {% csrf_token %}
    
    如果只要设置，或者排除单个路由或者view，可以使用 from django.views.decorators.csrf import csrf_exempt,csrf_protect
    排除 @csrf_exempt
    包含 @csrf_protect
    
# session  使用
    1.django 在session中设置值
        request.session['username'] = user
    2.从session中获取值
        if request.session['username']:
            print('ok')
    3.django session 存储方式,不支持使用redis，如果需要则需要去下载插件
        1.file
        2.db
        3.db + 缓存(memcache)
        4.缓存(memcache)
        5.使用cookie加密（即把session加密后作为cookie放到客户端）

# 缓存
    五种配置
        1.内存级别
        2.文件
        3.数据库
        4.memcached(有2种memcached连接方式)
        5.开发调试版本(即无缓存)
    
    三种应用（优先级从上往下依次变低，在全局的缓存里面就不会到view中了，如果view中获取到了就不会到模板中了）
        1.全局缓存
        2.基于view的 @cache_page
        3.基于模板的  @cache_control
    配置好cache之后，session可以直接使用cache，不用再配置一套session的存储机制了。
    
    
# 信号 signals
    1.django 所有的信号
    models signals
        pre_init
        post_init
        pre_save
        post_save
        pre_delete
        post_delete
        m2m_changed
        class_prepared
    Management signals
        pre_migrate    
        post_migrate   
    Request/Response signals
        request_start  请求开始前
        request_finished 请求结束
        got_request_exception 请求异常
    Test Signals
        settings changed   配置修改
        template_rendered  模板渲染
    DateBase wrappers
        connection_created  数据库连接创建
    
    2.使用信号，编写如下文件命名为sg.py
    from django.core.signals import request_finished,request_started,got_request_exception
    from django.db.models.signals import pre_init,post_init,pre_save,post_save,pre_delete,post_delete,pre_migrate,post_migrate,m2m_changed,class_prepared
    from django.test.signals import setting_changed,template_rendered
    from django.db.backends.signals import connection_created
    
    def f1(sender, **kwargs):
        print(sender)
        
    ## 使用任意一个信号request_finished，request_started
    pre_save.connect(f1) 
       
    3.在__init__文件中导入sg.py
    4.自定义信号步骤
        1.定义信号
        2.注册信号
        3.触发信号
        
# 跨域请求
    由于浏览器有同源策略，导致不能向其他地方请求数据,解决办法:
        1.jsonp(通过jsonp的方式发送的请求都是get请求)
        2.服务器设置cros 
    
    所有有src属性的标签都不受到同源策略的限制
        1.创建一个script标签 
        2.src=远程地址
        3.返回数据必须是js格式
    
    js版本
        var tag = document.createElement('script');
        tag.src = 'www.baidu.com?callback=list&v1=1&v2=2';
        document.head.addChild(tag);
        document.head.removeChild(tag);
    
        function  list(arg) {
            alert(arg)
        }

# XSSFilter 防护
    django提供了XSSFilter对提交的内容进行过滤

# 静态文件配置 static 
    1.settings  文件配置
        a.配置 INSTALLED_APPS
            在INSTALLED_APPS中加入'django.contrib.staticfiles',实际上默认已经加上了，确认下即可
        b.配置STATICFILES_DIRS
            STATIC_URL = '/static/'
            STATICFILES_DIRS = [
                os.path.join(BASE_DIR, "static"),
            ]
    2.文件夹布局
        在project创建static目录，该目录应该与app，templates是同级的，即如下图
            -- you-project-name
                -- you-project-name
                -- you-app-name
                -- static
                -- templates
    3.页面使用
        a.在页面的头部引入static  {% load static %}
        b.通过static引入资源，目录以static作为根目录,如
            <img src="{% static 'portal/blog/images/img05.jpg' %}" width="540" height="250" alt="" />
        

# 使用模板后静态文件使用
    如果某个页面需要引入模板，该页面要使用静态文件，需要在extends模板之后，接着写{% load static %} 不能写在extends 之前
    {% extends 'common/tpl_blog.html' %}
    {% load static %}
    