# urls.py
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from post.views import *

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main, name='Main'),
    path('create/', create, name='create'),
    path('detail/<str:post_id>/', detail, name='detail'),
    path('accounts/', include('accounts.urls')),
    path('mypage/<str:user_id>', mypage, name="mypage"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
