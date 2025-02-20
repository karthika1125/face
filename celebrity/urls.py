from django.urls import path
from.import views

urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('live/',views.live,name='live'),
    path('faq/',views.faq,name='faq'),
    path('contact/',views.contact,name='contact'),
    path('index/',views.index,name='index'),
    path('howitwork/',views.howitwork,name='howitwork'),
    path('celebrityinfo/',views.celebrityinfo,name='celebrityinfo'),
]