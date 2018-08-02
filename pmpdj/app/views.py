from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.models import ImgCode, Owner
from utils.get_img_code import ValidCodeImg


def index(request):
    """
    首页
    :param request:
    :return:
    """
    if request.method == 'GET':
        user = request.session.get('user_id')
        return render(request, 'index.html', {'user': user})


def login(request):
    """
    业主登录
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        number = request.POST.get('number')
        password = request.POST.get('password')
        img_code = request.POST.get('img_code')
        code = ImgCode.objects.filter(code=img_code).first()
        if not code:
            ctx = {'code': 1001, 'msg': '验证码输入错误'}
            return render(request, 'login.html', ctx)
        user = Owner.objects.filter(number=number, password=password).first()
        if not user:

            ctx = {'code': 1002, 'msg': '用户名或密码输入错误'}
            return render(request, 'login.html', ctx)

        request.session['user_id'] = user.number
        # 设置session值存活时间为一天(86400秒)
        request.session.set_expiry(86400)

        return HttpResponseRedirect('/user/mineInfo')


def logout(request):

    if request.method == 'GET':

        # 清除session中的用户数据
        # request.session.flush()
        # del request.session['user_id']
        request.session.clear()

        response = HttpResponseRedirect('/user/login')

        return response


def get_img_code(request):
    """
    随机生成验证码
    :param request:
    :return:
    """
    if request.method == 'GET':
        img = ValidCodeImg()
        data, valid_str = img.get_valid_code_img()

        with open('media/var_code.png', 'wb') as f:
            f.write(data)

        # 清除无用的验证码数据
        ImgCode.objects.filter().delete()
        # 保存此时需验证的数据
        ImgCode.objects.create(code=valid_str)
        json_data = {
            'code': 200,
        }

        return JsonResponse(json_data)


def user_mine_info(request):
    """
    业主个人中心页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        user = request.session.get('user_id')
        return render(request, 'user/mine_info.html', {'user': user})


def living_pay(request):
    """
    生活缴费
    :param request:
    :return:
    """
    user = request.session.get('user_id')
    return render(request, 'user/living_pay.html', {'user': user})


def update_info(request):
    """
    修改住户信息
    :param request:
    :return:
    """
    user = request.session.get('user_id')
    return render(request, 'user/update_info.html', {'user': user})


def get_user_no(request):
    """
    通过user_id 拿到模型，返回房屋等数据
    :param request:
    :return:
    """
    if request.method == 'GET':
        number = request.session.get('user_id')
        user = Owner.objects.filter(number=number).first()
        json = {
            'code': 200,
            'user': user.to_dict
        }
        return JsonResponse(json)
