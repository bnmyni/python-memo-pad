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
