from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password,make_password
from Myblog.models import Classes,Userinfo,SiteInfo
from Myblog.tojson import Classes_data,Userinfo_data
import json


@api_view(['GET','POST'])
def api_test(request):
    classes = Classes.objects.all()
    # print(classes_list)
    # classes_data = Classes_data(classes_list,many=True)
    # userlist = Userinfo.objects.all()
    # userlist_data = Userinfo_data(userlist,many=True)

    # data = {
    #     'classes':classes_data.data, 
    #     'userlist':userlist_data.data
    # }

    data = {
        'classes' : []
    }
    for c in classes:
        data_item = {
            'id': c.id,
            'text':c.text,
            'userlist':[]
        }
        userlist = c.userinfo_classes.all()
        for user in userlist:
            user_data = {
                    'id':user.id,
                    'nickName':user.nickName,
                    'headImg':str(user.headImg)
            }
            data_item['userlist'].append(user_data)
        data['classes'].append(data_item)
    # data = json.dumps(data)
    return Response(data)

@api_view(['GET'])
def getMenuList(request):
    allClasses = Classes.objects.all()
    siteinfo = SiteInfo.objects.get(id=1)
    siteinfo_data = {
        'sitename':siteinfo.title,
        'logo':'http://127.0.0.1:9000/upload/'+str(siteinfo.logo)
    }


    #整理数据为Json
    menu_data = []
    for c in allClasses:
        #设计单条数据的结构
        data_item = {
            'id':c.id,
            'text':c.text
        }
        menu_data.append(data_item)

    data = {
         'menu_data':menu_data,
         'siteinfo':siteinfo_data
    }
    return Response(data)

@api_view(['GET'])
def getUserList(request):
    menuId = request.GET['id']
    print(menuId)
    menu = Classes.objects.get(id=menuId)
    print(menu)
    userlist = Userinfo.objects.filter(belong=menu)
    print(userlist)

    #开始整理数据列表
    data =[]
    for user in userlist:
        data_item = {
            'id':user.id,
            'headImg':str(user.headImg),
            'nickName':user.nickName
        }
        data.append(data_item)
    return Response(data)

@api_view(['POST'])
def toLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username,password)
    #查询用户数据库
    user = User.objects.filter(username=username)
    if len(user)>0:
        # auth_user = authenticate(username=username,password=password)
        # print(auth_user)
        # if auth_user:
        #     return Response('登录成功')
        # else:
        #     return Response('密码错误')
        user_pwd = user[0].password
        auth_pwd = check_password(password,user_pwd)
        print(auth_pwd)
        if auth_pwd:
            token = Token.objects.update_or_create(user=user[0])
            token = Token.objects.get(user=user[0])
            print(token.key)
            data = {
                'token':token.key
            }
            return Response(data)
        else:
            return Response('pwderr')
    else:
        return Response('None!')

@api_view(['GET','POST'])
def toRegister(request):
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    # print(username,password,password2)
    user = User.objects.filter(username=username)
    if len(user)>0:
        return Response('Same User Name')
    else:
        newPwd = make_password(password,username)
        newUser = User(username=username,password=newPwd)
        newUser.save()
    return Response('收到注册')

@api_view(['POST','PUT'])
def uploadLogo(request):
    if request.method == "PUT":
        sitename = request.POST['sitename']
        print(sitename)
        # logo = request.POST.logo
        old_info = SiteInfo.objects.get(id=1)
        old_info.title = sitename
        new_info = SiteInfo.objects.get(id=3)
        old_info.logo = new_info.logo
        old_info.save()
        return Response('PUT OK')
    img = request.FILES['logo']
    print(img)
    test_siteLogo = SiteInfo.objects.get(id=3)
    test_siteLogo.logo = img
    test_siteLogo.save()
    data = {
        'img':str(test_siteLogo.logo)
    }
    return Response(data)