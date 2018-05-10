from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
from user import models
# Create your views here.

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
# ##  在页面中循环一个dict，也可以my_dict.keys|my_dict.values
# {% for k,v in my_dict.items %}
# 	{{k}}-{{v}}
# {% endfor %}

def detail(request, **kwargs):
    print(kwargs)
    return HttpResponse('detail-%d-%d-%d' % (kwargs['year'], kwargs['month'], kwargs['day']))

## fbv模式
def index(request):
    return HttpResponse('index')

def add(request):
    models.UserInfo.objects.create(username='sky', pwd='aaa111', age=99)

    # obj = models.UserInfo(username='bnmyni', pwd='aaa111')
    # obj.save()
    return HttpResponse('新增成功')


def list(request):
    querySet = models.UserInfo.objects.all()

    # models.UserInfo.objects.all().values()
    # models.UserInfo.objects.all().values_list()
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

def login(request):
    print('wlecome to logion.....')
    if request.method == 'GET':
        return render(request, "login.html")
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        # s = request.POST.getlist('services')
        # sex = request.POST.get('sex')
        # city = request.POST.getlist('city')
        # upload_file = request.POST.get('upload_file')
        file = request.FILES.get('upload_file')

        f = open(file.name, mode='bw')
        for i in file.chunks():
            f.write(i)
        f.close()


        if u == 'aspire' and p == '123456':
            return HttpResponseRedirect('/index/')
        else:
            return render(request, 'login.html')
    else:
        return HttpResponseRedirect('/index/')

## cbv 模式, 类似servlet(dispatch) ,struts的模式
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

from django.test.signals import setting_changed, template_rendered