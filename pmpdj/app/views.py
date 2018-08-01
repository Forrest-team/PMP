from django.http import JsonResponse
from django.shortcuts import render

from app.models import ImgCode
from utils.get_img_code import ValidCodeImg


def index(request):

    return render(request, 'index.html')


def login(request):
    """
    业主登录
    :param request:
    :return:
    """
    return render(request, 'login.html')


def get_img_code(request):
    if request.method == 'GET':
        img = ValidCodeImg()
        data, valid_str = img.get_valid_code_img()

        with open('../media/var_code.png', 'wb') as f:

            f.write(data)

        ImgCode.objects.create(code=valid_str)

    return render(request, 'login.html')