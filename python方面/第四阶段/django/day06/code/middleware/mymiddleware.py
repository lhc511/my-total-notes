from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse,Http404

#该中间件在settings文件中注册之后就可以生效
class MyMW(MiddlewareMixin):
    #在浏览器作任何请求路由的时候将其拦截，可返回none请求原路由，也可以返回response对象来指向新路由
    def process_request(self,request):
        print("中间件process_request被调用")
        print("路由是:",request.path)
        print("请求方式:",request.method)
        # 此处在满足条件后会返回新对象，不会调用原有任何视图函数
        # if request.path=="/":
        #     return HttpResponse('当前路由是:/')

    #倘若调用的是/note/del/1这个路由对应的函数,相当于:
    # mw.process_view(request,views.del_view,'1',{})
    # def process_view(self,request,callback):
    #     pass

#每当用户访问该网站的时候，就会进入一次该类中的函数，从而使得变量 加1
class VisitLimit(MiddlewareMixin):
    visit_times={}#存{ip地址:ip地址访问次数}

    def process_request(self,request):
        #得到来访ip的ip地址
        ip=request.META['REMOTE_ADDR']
        print(ip)
        if request.path_info!='/test':
            return None
        #获取以前的访问次数，若没有则默认设置为0
        times=self.visit_times.get(ip,0)
        print("IP",ip,'已访问过/test',times,'次')

        self.visit_times[ip]=times+1
        if times<5:
            # return None 表示不再中间件中作拦截，继续执行下面的步骤并在最终返回功能页面
            return None
        return HttpResponse("您以访问过："+str(times)+"次")