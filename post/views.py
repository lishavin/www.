from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Scrap
from accounts.models import Users
from datetime import datetime, timedelta,date
import datetime

def Main(request):
    origin_post=Post.objects.all()
    posts_scrap = origin_post.order_by('-scrap')
    posts_liked = origin_post.order_by('-liked')
    startdate = date.today()
    enddate = startdate + timedelta(days=1)
    post = Post.objects.filter(created_at__range=[startdate, enddate])
    #mypost = post.order_by('-liked')[0]
    mypost = None  # Initialize mypost to None by default

    if post.exists():  # Check if there are any elements in the queryset
        mypost = post.order_by('-liked')[0]
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    hour = int(now.strftime("%H"))
    return render(request, 'Main.html', {"mypost":mypost, 'now':current_time, 'hour':hour, 'posts_scrap':posts_scrap, 'posts_liked':posts_liked, 'origin_post':origin_post})

def create(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    else:
        post = Post()
        post.image = request.POST.get('image',False)
        post.weather = request.POST['weather']
        post.weather_desc = request.POST['weather_desc']
        post.temp = request.POST['temp']
        post.temp_desc = request.POST['temp_desc']
        post.finedust =request.POST['finedust']
        post.finedust_desc =request.POST['finedust_desc']
        post.tmi =request.POST['tmi']
        post.wear_tag1 =request.POST['wear_tag1']
        post.wear_tag2 =request.POST['wear_tag2']
        post.wear_tag3 =request.POST['wear_tag3']
        post.today_tag1 =request.POST['today_tag1']
        post.today_tag2 =request.POST['today_tag2']
        post.today_tag3 =request.POST['today_tag3']
        post.user = request.user
        post.save()
    return redirect('home')


def detail(request, post_id):
    post_detail = get_object_or_404(Post, id=post_id)
    weather_index = 0
    weather_max = 0
    finedust_index = 0
    finedust_max = 0
    if weather_index == 0:
        weather_status =  '#맑음'
    elif weather_index == 1:
        weather_status =  '#흐림'
    elif weather_index == 2:
        weather_status =  '#비'
    elif weather_index == 3:
        weather_status =  '#눈'
    else : 
        weather_status =  '#바람'
        
    if finedust_index == 0:
        finedust_status =  '#좋음'
    elif finedust_index == 1:
        finedust_status =  '#조금좋음'
    elif finedust_index == 2:
        finedust_status =  '#보통'
    elif finedust_index == 3:
        finedust_status =  '#조금나쁨'
    else : 
        finedust_status =  '#나쁨'
    return render(request, 'detail.html', {'post_detail':post_detail, 'weather' : weather_status, 'finedust': finedust_status})

def mypage(request,user_id):
    #wear_tag = {}
    weather_avg = [0,0,0,0,0]
    finedust_avg = [0,0,0,0,0]

    temp = 0
    post_num = 0
    user = get_object_or_404(Users, id = user_id)
    post_detail = Post.objects.filter(user = user)
    for post in post_detail:

        weather_avg[int(post.weather)] = weather_avg[int(post.weather)]+1
        finedust_avg[int(post.finedust)] = finedust_avg[int(post.finedust)]+1
        temp = temp + int(post.temp)
        post_num = post_num + 1
        # try :
        #     wear_tag[str(weather.wear_tag1)] = int(wear_tag[weather.wear_tag1]) +1
        # except :
        #     wear_tag[str(weather.wear_tag1)] = 1

    # for post in post_detail :
    #     post
    # #sorted_dict = sorted(wear_tag.items(), key = lambda item: item[1])
    # wear = list(sorted_dict.keys())
    # my_wear = []
    # my_wear.append(wear[0])
    # my_wear.append(wear[1])
    # my_wear.append(wear[2])
    weather_index = 0
    weather_max = 0
    finedust_index = 0
    finedust_max = 0
    for i in range(5):
        if weather_avg[i] > weather_max:
            weather_max = weather_avg[i]
            weather_index = i
        if finedust_avg[i] > finedust_max:
            finedust_max = finedust_avg[i]
            finedust_index = i

    if weather_index == 0:
        weather_status =  '#맑음'
    elif weather_index == 1:
        weather_status =  '#흐림'
    elif weather_index == 2:
        weather_status =  '#비'
    elif weather_index == 3:
        weather_status =  '#눈'
    else : 
        weather_status =  '#바람'
        
    if finedust_index == 0:
        finedust_status =  '#좋음'
    elif finedust_index == 1:
        finedust_status =  '#조금좋음'
    elif finedust_index == 2:
        finedust_status =  '#보통'
    elif finedust_index == 3:
        finedust_status =  '#조금나쁨'
    else : 
        finedust_status =  '#나쁨'

        ('0', '#좋음'),
        ('1', '#조금좋음'),
        ('2', '#보통'),
        ('3', '#조금나쁨'),
        ('4', '#나쁨'),

 
    temp_avg = temp/post_num
    my_info = {'weather' : weather_status, 'finedust' : finedust_status, 'temp_avg' : temp_avg  }


    return render(request,'mypage.html', {'post_detail' : post_detail, 'user_detail' : user, 'weather' : weather_status, 'finedust' : finedust_status, 'temp_avg' : temp_avg })