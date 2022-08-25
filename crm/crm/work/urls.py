from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from crm import settings
from django.urls import path
from .views import *

urlpatterns = [
    path('staf/<int:id>', staf, name='staf'),
    path('create_user/', create_user, name='create_user'),
    path('user/<int:id>', user_page, name='user'),
    path('create_staf/', create_staf, name='create_staf'),
    path('create_channel/', create_channel_view, name='create_channel'),
    path('channel/<int:id>', channel_view, name='channel'),
    path('create_chat/', create_chat_view, name='create_chat'),
    path('add_ivent/', add_ivent, name='add_ivent'),
    path('ivent/<int:id>', add_ivent, name='ivent'),
    path('add_mailing/', add_mailing, name='add_mailing'),
    path('mailing/<int:id>', add_mailing, name='mailing'),
    # path('content_page/', content_page, name='content_page'),
    path('delete_chat/<str:id>', delete_chat, name='delete_chat'),
    path('task_connect/<str:id>', task_connect, name='task_connect'),
    path('<str:page>', main, name='main'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
