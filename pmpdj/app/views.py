from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from app.models import ImgCode, House, HouseOrderModel, Orders, Owner, Complain
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
        request.session['user_id'] = user.owner_id
        # 设置session值存活时间为一天(86400秒)
        request.session.set_expiry(86400)

        return HttpResponseRedirect('/user/mineInfo')


def logout(request):
    """
    退出登录，清除session数据
    :param request:
    :return:
    """
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


def rs_house(request):
    houses = House.objects.all()
    paginator = Paginator(houses, 9)
    page = request.GET.get('page', 1)
    houses_list = paginator.page(page).object_list
    return render(request, 'rs_house.html', {'houses_list': houses_list})


def rs_house_info(request, cid, sid):
    """
    展示小区所有租赁买卖房源
    :param request: GET
    :return: house信息
    :param:cid类型(租赁或买卖){0:租赁,1:买卖}
    :param:sid筛选类型{0:升序,1:降序}
        """
    if request.method == 'GET':
        if cid:
            houses = House.objects.filter(type=cid)
            if sid == 0:
                houses.order_by('price')
            else:
                houses.order_by('-price')
        else:
            houses = House.objects.all()
            if sid == 0:
                houses.order_by('price')
            else:
                houses.order_by('-price')
        paginator = Paginator(houses, 9)
        page = request.GET.get('page', 1)
        houses_list = paginator.page(page).object_list
        return render(request, 'rs_house.html', {'houses_list': houses_list})


def order_house(request):
    """
    预约业主
    :param request: GET
    :return: 预约页面
    :param request: POST
    :return: 产生订单
    """
    if request.method == 'GET':
        return render(request, 'order_house.html')
    if request.method == 'POST':
        owner = request.session['user_id']
        start_time = request.POST.get('start_time')
        days = request.POST.get('days')
        HouseOrderModel.objects.create(owner=owner, start_time=start_time, days=days)
        return redirect('/user/house_order/')


def newhouse(request):
    """
    发布业主个人租赁买卖房源
    :param request: GET
    :return: 发布房源页面
    :param request: POST
    :return: 将房源信息存入数据库,返回业主个人中心页面
    """
    if request.method == 'GET':
        return render(request, 'newhouse.html')
    if request.method == 'POST':
        owner = request.session['user_id']
        address = request.POST.get('address')
        img = request.FILES.get('img')  # 图片
        price = request.POST.get('price')  # 价格
        acreage = request.POST.get('acreage')  # 房屋面积
        unit = request.POST.get('unit')  # 房间单元 如几室几厅
        deposit = request.POST.get('deposit')  # 房屋押金
        House.objects.create(owner=owner, address=address, img=img, price=price, acreage=acreage,unit=unit, deposit=deposit)
        return redirect('/user/index/')


def house_lorder(request):
    """
    展示客户订单
    :param request: GET
    :return: 订单展示
    :param request: POST
    :return: 处理订单,点击处理,状态变为处理中,点击完成或拒单,房源信息从房源展示页面移除
    """
    if request.method == 'GET':
        owner = request.session['user_id']
        houses = House.objects.filter(owner=owner)
        orders = []
        for house in houses:
            orders.extend(HouseOrderModel.objects.filter(house=house))
        return render(request, 'house_lorder.html', {'orders': orders})
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = HouseOrderModel.objects.get(id=order_id)
        order_status = request.POST.get('status')
        if order_status == 0:
            #  订单状态{0:待处理,1:处理中,2:处理完毕, 3:拒单, 4:取消}
            order.status = 1
            order.save()
        if order_status == 1:
            order.status = 2
            order.save()
        return redirect('/user/house_lorder/')


def reject_order(request):
    """
    业主拒单处理
    :param request: POST
    :return: 储存拒单理由,修改订单状态
    """
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = HouseOrderModel.objects.get(id=order_id)
        order.reason = request.POST.get('reason')
        order.status = 3
        order.save()
        return redirect('/user/house_order/')


def house_order(request):
    """
    个人订单
    :param request: GET
    :return: 个人订单展示
    :param request: POST
    :return: order状态修改
    """
    if request.method == 'GET':
        owner = request.session['user_id']
        orders = HouseOrderModel.objects.filter(owner=owner)
        return render(request, 'house_order.html', {'orders': orders})
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = HouseOrderModel.objects.get(id=order_id)
        if order.status != 1:
            order.status = 4
            order.save()
            return redirect('/user/house_order/')


def request_service(request):
    """
        申请物业服务
        :param request: GET
        :return: 填写服务内容
        :param request: POST
        :return: 存入数据库,返回服务订单页面
        """
    if request.method == 'GET':
        return render(request, 'request_service.html')
    if request.method == 'POST':
        owner = request.session['user_id']
        type = request.POST.get('server_project')
        Orders.objects.create(owner=owner, server_project=type)
        return redirect('/user/orders/')


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
    # 门禁卡办理
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

    if request.method == 'GET':
        return render(request, 'request_service.html')
    if request.method == 'POST':
        owner = request.session['user_id']
        type = request.POST.get('server_project')
        Orders.objects.create(owner=owner, server_project=type)
        return redirect('/user/orders/')


def order_to_property(request):
    """
    查看申请服务订单信息,移除订单
    :param request:GET
    :return:订单处理情况信息
    :param request:POST
    :return:移除申请,数据库和页面删除信息
    """
    if request.method == 'GET':
        orders = Orders.objects.all()
        return JsonResponse({'code': 200}, [order.to_dict() for order in orders])
    if request.method == 'POST':
        owner = request.session['user_id']
        server_project = request.POST.get('server_project')
        data = {
            'code': 200,
            'owner': owner,
            'server_project': server_project
        }
        return JsonResponse(data)


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
