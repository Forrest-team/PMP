from django.shortcuts import render


def index(request):

    return render(request, 'index.html')


def login(request):
    """
    业主登录
    :param request:
    :return:
    """
    return render(request, 'login.html')
