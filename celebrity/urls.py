from django.urls import path
from.import views

urlpatterns=[
    path('register/',views.register,name='register'),
    path('login_view/',views.login_view,name='login_view'),
    path('live/',views.live,name='live'),
    path('faq/',views.faq,name='faq'),
    path('contact_view/',views.contact_view,name='contact_view'),
    path('index/',views.index,name='index'),
    path('howitwork/',views.howitwork,name='howitwork'),
    path('celebrityinfo/',views.celebrityinfo,name='celebrityinfo'),
    path('home/',views.home,name='home'),
    path('logout_view/',views.logout_view,name='logout_view'),
]