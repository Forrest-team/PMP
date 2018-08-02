from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class UserMiddle(MiddlewareMixin):

    def process_request(self, request):

        need_login = ['/MineInfo/', ]

        if request.path in need_login:

            if 'user_id' not in request.session:

                return HttpResponseRedirect('/user/login/')
