from rest_framework.decorators import api_view
from rest_framework.response import Response
from Myblog.models import Classes,Userinfo
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

    #整理数据为Json
    data = []
    for c in allClasses:
        #设计单条数据的结构
        data_item = {
            'id':c.id,
            'text':c.text
        }
        data.append(data_item)
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