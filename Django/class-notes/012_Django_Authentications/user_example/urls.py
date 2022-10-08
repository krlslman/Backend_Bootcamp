from django.urls import path, include
from .views import (
    home,
    special,
    register
    )
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('special/', special, name="special"),
    path('register/', register, name="register"),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name="registration/password_change.html"), name="password_change")
]

""" 
4 ÜNCÜ PATHDE NE YAPTIK?
- password_change adında bir end-point belirledik. 
- Bu endpoint'e istek geldiğinde beni django tarafından verilen default "auth_views.PasswordChangeView.as_view"üne yönlendir,
- Ama django tarafından verilen default template yerine "registration/password_change.html" isimli template'imi kullan 

""" 