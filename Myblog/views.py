from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from Myblog.models import SiteInfo,Classes,Userinfo

# Create your views here.
def index(request):
    #站点基础信息
    # print('开始读取数据')
    siteinfo = SiteInfo.objects.all()[0]
    # print(siteinfo.title)
    # print(siteinfo.logo)
    #菜单分类
    classes = Classes.objects.all()
    #全部用户
    userlist = Userinfo.objects.all()
    data = {
        "siteinfo":siteinfo,
        "classes":classes,
        "userlist":userlist
        # "userlist":[]
    }
    return render(request,'index.html',data)

def classes(request):
    siteinfo = SiteInfo.objects.all()[0]
    # print(siteinfo.title)
    # print(siteinfo.logo)
    #菜单分类
    classes = Classes.objects.all()
    #用户列表
    try:
        choosed_id = request.GET['id']
        print(choosed_id)
        choosed = Classes.objects.filter(id=choosed_id)
        print(choosed)
    except:
        return redirect('/')
        
    if choosed:
        userlist = Userinfo.objects.filter(belong=choosed[0])
    else:
        userlist = []

    data = {
            "siteinfo":siteinfo,
            "classes":classes,
            "userlist":userlist
            # "userlist":[]
        }

    return render(request,'classes.html',data)