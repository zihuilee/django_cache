import time
from random import randrange

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class hello(MiddlewareMixin):
    def process_request(self, request):
        # print(request.META.get('REMOTE_ADDR'))

        ip = request.META.get('REMOTE_ADDR')
        if request.path == '/App/getphone/':
            if ip == '127.0.0.1':
                if randrange(100) > 20:
                    return HttpResponse('恭喜你获得购买资格！')

        elif request.path == '/App/getticket/':
            return HttpResponse('已抢光！')

        elif request.path == '/App/search/':
            result = cache.get(ip)
            if result:
                return HttpResponse('你的访问过于频繁，请十秒后再试！')
            cache.set(ip, ip, timeout=10)

        black_list = cache.get('black', [])

        if ip in black_list:
            return HttpResponse('黑名单！')

        requests = cache.get(ip, [])

        while requests and time.time() - requests[-1] > 60:
            requests.pop()

        requests.insert(0, time.time())
        cache.set(ip, requests, timeout=60)

        if len(requests) > 300:
            black_list.append(ip)
            cache.set('black', black_list, timeout=60*60*24)
            return HttpResponse('请求频繁3')

        if len(requests) > 100:
            return HttpResponse('请求频繁1')
        pass

    # def process_exception(self, request, exception):
    #     print(request, exception)
    #     return redirect('app:index')




