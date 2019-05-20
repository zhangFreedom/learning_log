from django.shortcuts import render,render_to_response

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from .models import Topic, Entry, Img
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404,HttpResponse
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
import json
import time


# Create your views here.
'''该工程主要用于，跳转到url匹配成功的视图函数
试图函数收集数据，并在一定条件下跳转到相应的模板'''

a = [{'type': "笔记本", 'money': 3.5, 'number': 2},
     {'type': "苹果", 'money': 233.3, 'number': 1},{'type': "心相印抽纸", 'money': 2.5, 'number': 1}]


# rlist = [['123456789', '', 5, 2], ['Mike', 'English', 788, 3], ['Bob', 'Math', 4, 5], ['Frank', 'Art', 8, 9],['123456789', '优质牛肉', 5, 2]]
rlist=[]
rlist3=[]


def index(request):
    #学习笔记的主页
    return render(request,'learning_logs/index.html')

@login_required
def topics(request):
    
    """显示所有的主题"""

   
    topics = Topic.objects.order_by('date_added')# 一个上下文字典，传递给模板
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html',context)

@login_required
def topic(request,topic_id):
    """显示单个主题及其所有条目"""
    topic=Topic.objects.get(id=topic_id)
    imgs=Img.objects.all()
    #for i in imgs:
        #print(i.date_added)
# 确认请求的主题属于当前用户
    #if topic.owner != request.user:
        #raise Http404
    entries=topic.entry_set.order_by('-date_added')
    context = {'topic': topic,'entries': entries,'imgs':imgs,}
    return render(request, 'learning_logs/topic.html',context)

#显示空表单，读取用户输入的表单数据，并将用户重定向到topics

@login_required
def new_topic(request):
    """添加新主题"""
    if request.method !='POST':
        #未提交数据，创建一个新表单
        form=TopicForm()
    else:
        #
        form=TopicForm(request.POST)
        if form.is_valid():
            
 # 添加新主题时关联到特定用户
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            # 该类将用户重定向到网页topics，函数reverse()根据指定的URL模型确定URL
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context={'form':form}
    return render(request,'learning_logs/new_topic.html',context)


@login_required
def new_entry(request, topic_id):
    """在特定的主题中添加条目"""

    topic=Topic.objects.get(id=topic_id)
    #提交条目的同时，可以插入图片，实现图片上传
    f1=request.FILES.get('img')
    if request.method == 'POST':
        #如果当前有图片的上传将其存储到本地静态文件中的media中，保证无图片上传时，不影响文本的上传
        if  f1:        
            img = Img(img=request.FILES.get('img'),
                      name=request.FILES.get('img').name,
                      )
            #下面红褐色的为方法二，进行图片上传保存
            #img.pic = settings.MEDIA_ROOT+ f1.name
            img.save()
            
            #fname=settings.MEDIA_ROOT+ f1.name          
            #with open(fname,'wb') as pic:
                #for c in f1.chunks():
                    #pic.write(c)
                   

    if request.method !='POST':
        #未提交数据，创建一个新表单
        form=EntryForm()
        
    else:
        #POST提交的数据，对其进行处理
        form=EntryForm(data=request.POST)
        
# 检查是否填写了所有必不可少的字段。(是否有效)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                kwargs={'topic_id':topic_id}))
    #先用reverse来获取名称为topic的页面的url，并提供其所需的所有参数，来满足url的生成
    context={'topic':topic,'form':form}
    #参数传递错误
    return render(request,'learning_logs/new_entry.html',context)

@login_required        
def edit_entry(request, entry_id):
    #编辑既有的条目
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != "POST":
        form=EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))        
    context={'entry':entry, 'topic':topic, 'form':form}
    return render(request,'learning_logs/edit_entry.html',context)




# #视频还未添加，此处还需要更改
# @login_required
# def videos(request, entry_id):
#     if video.owner != request.user:
#         raise Http404
#     else:
#         videos_list#查看对应文件目录，读取各个视频文件名称，存入列表
#         if videos_list:#视频文件存在
#             #调用人脸识别函数，进行视频处理提取视频中的人物图像
#             #保存人脸图像到服务器对应文件目录，使用数据库记录当前文件的名称，路径
#             #进行人脸图像展示，传递图像路径和文件名称列表到模板
#             return rebder(request,'learning_logs/vieos_pictures.html',context)




#重定向到对应的页面


@login_required
def shop(request):

    # """添加新的商品"""
    # if request.method != 'POST':
    #     # 未提交数据，创建一个新表单
    #     form = TopicForm()
    # else:
    #     #
    #     form = TopicForm(request.POST)
    #     if form.is_valid():
    #         # 添加新主题时关联到特定用户
    #         new_shop = form.save(commit=False)
    #         new_shop.owner = request.users
    #         new_shop.save()
    #         # 该类将用户重定向到网页topics，函数reverse()根据指定的URL模型确定URL
    #         return HttpResponseRedirect(reverse('learning_logs:topics'))


    return render(request, 'learning_logs/shop.html',{'type': a})

@login_required
def confirmation(request):
    return render(request, 'learning_logs/confirmation.html')

#此实例中未用到
@login_required  
def uploadImg(request): # 图片上传函数
    if request.method == 'POST':
        img = Img(img_url=request.FILES.get('img'))
        img.save()
    return render(request, 'learning_logs/new_entry.html')


        
    


@csrf_exempt
def data_fresh(request):

    context = {"data1":8
               }
    if time.sleep(10):
        context.update(data2=89)
        print(context)

    return JsonResponse(context)


sa=0
ind=0


def data(request,id):
    global rlist, rlist3, sa,ind
    aa=len(rlist)
    da=len(rlist3)
    #u = 0
    t = 0
    #此处问题为，当原始没有数据的时候，后面虽然有数据到来，但随着id的增加永远大于a
    #解决方法，使得test中的id不增加，每次使用完rlist的数据，将其清空，判断其是否长度为0，不为0，则进行添加，为零执行下面的else语句

    #   将rlist[int(id)][3]，中的id值改为0即可，不用管 test中i++带来的影响

    if aa ==1:
        rlist2 = []

        # 判断数据是否一样
        if da == 0:
            rlist3.append({"type": rlist[0][0], "amount": rlist[0][3], "id":id})   #rlist[int(id)][0]
            sa=0
        else:

            for item in rlist3:

                if item['type']==rlist[0][0]:
                    rlist[0][3]=item["amount"]+rlist[0][3]
                    item["amount"]=rlist[0][3]
                    print('相同的时候数量为：',rlist[0][3])
                    sa = 1
                    ind=item["id"]
                    t=1

            if t ==0:
                rlist3.append({"type": rlist[0][0], "amount": rlist[0][3], "id":id})
                sa=0

        rlist2.append({"type" : rlist[0][0], "comment" : rlist[0][1],"price":rlist[0][2],"amount":rlist[0][3],"sa": sa ,"ind":ind})
        rjson = json.dumps(rlist2)
        response = HttpResponse()
        response['Content-Type'] = "text/javascript"
        response.write(rjson)
        rlist=[]
        return response
    else:
        b=[{"type" :'',"comment" :'',"price":'',"amount":'',"sa":'',"ind":''}]
        rjson = json.dumps(b)
        response = HttpResponse()
        response['Content-Type'] = "text/javascript"
        response.write(rjson)
        return response


def update(request):

    return render_to_response('learning_logs/test.html')


def deal_data(request):
    global rlist
    typ = request.GET.get('type')
    comment = request.GET.get('comment')
    price= request.GET.get('price')
    amount= request.GET.get('amount')
    rlist.append([typ, comment,eval(price),eval(amount)])
    print(type(eval(price)))
    return HttpResponse("p1 = " + typ+ "; p2 = " + comment)

k=0
def shou_yin(request):
    global k
    k=1
    return HttpResponse("<p1>请您出示收款码</p1>")

def jiesuan(request):
    global k
    return HttpResponse(k)








        


   
