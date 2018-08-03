from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class UserMiddle(MiddlewareMixin):

    def process_request(self, request):

<<<<<<< HEAD
        need_login = ['/user/mineInfo/', '/user/livingPay/',
                      '/user/updateInfo/']
=======
        need_login = ['/MineInfo/', ]
>>>>>>> zc

        if request.path in need_login:

            if 'user_id' not in request.session:

                return HttpResponseRedirect('/user/login/')
