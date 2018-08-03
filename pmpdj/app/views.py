from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render


from app.models import ImgCode, Owner

from app.models import ImgCode, Complain

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
        # 成功登录后，保存user_id到服务端session中
        request.session['user_id'] = user.owner_id
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
        user_id = request.session.get('user_id')
        user = Owner.objects.filter(owner_id=user_id).first()
        if user:
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
    if request.method == 'GET':
        user = request.session.get('user_id')
        return render(request, 'user/update_info.html', {'user': user})

    if request.method == 'POST':
        user_id = request.session.get('user_id')
        username = request.POST.get('username')
        telephone = request.POST.get('phone')
        sex_ = request.POST.get('sex')
        sex = 1 if sex_ == '男' else '0'
        Owner.objects.filter(owner_id=user_id).update(owner_name=username,
                                                      owner_phone=telephone,
                                                      owner_sex=sex)

        json = {
            'code': 200,
        }

        return JsonResponse(json)



def complain(request):
    """
    :param request:业主投诉信息
    :return:
    """
    if request.method == 'GET':
        return render(request, 'complain.html')

    if request.method == 'POST':
        owner_id = request.session.user_id
        cont = request.POST.get('contian')
        status = '待处理'
        Complain.objects.create(complain_content=cont, owner_id=owner_id, complain_status=status)
        data = {'cont': cont, 'status': status}
        return JsonResponse(data)


def deal_with(request):
    """
    物业处理投诉信息
    :param request:
    :return:
    """
    content = Complain.objects.all()

    return render(request, 'deal_with.html', {"content": content})


def del_deal(request):

    if request.method == 'GET':
        return render(request, 'del_deal.html')

    if request.method == 'POST':
        owner_id = request.POST.get('owner_id')
        deal = Complain.objects.filter(owner_id=owner_id).first()

        Complain.objects.filter(complain_content=deal.complain_content).delete()
        data = {'code': 200, 'message': '删除成功'}
        return JsonResponse(data)


def entrance_card(request):
    #门禁卡办理
    if request.method == 'GET':
        pass
    return render(request, 'complain.html')


def get_user_no(request):
    """
    通过user_id 拿到模型Owner，返回房屋等数据
    :param request:
    :return:
    """
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        user = Owner.objects.filter(owner_id=user_id).first()

        json = user.to_dict

        return JsonResponse(json)

