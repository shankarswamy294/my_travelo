from django.conf.urls import include,url
from . import views
from .views import Add_upload,Add_User,Wall,Home,Profile_user,Update_upload,Delete_upload



from django.conf.urls import url
from my_travelo import views

urlpatterns = [

    url(r'add_upload/$',Add_upload.as_view()),
    url(r'add_user/$', Add_User.as_view()),
    url(r'wall/$',Wall.as_view()),
    url(r'wall/([A-Za-z]+)/$',views.Per_user_wall),
    url(r'profile/$',views.my_view),
    url(r'update/(?P<pk>[0-9]+)/$',Update_upload.as_view()),
    url(r'delete/(?P<pk>[0-9]+)/$', Delete_upload.as_view()),

    url(r'^new/$', views.User_list),
    url(r'^new/(?P<pk>[0-9]+)/$', views.User_list),
]
