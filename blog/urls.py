
from . import views
from django.urls import path


urlpatterns = [
    
    # path('',views.postlist.as_view(),name='home'),
    # path('<slug:slug>/',views.postlist.as_view(),name='postdetail')
    path('',views.index,name="index"),
    path('detailed/',views.index,name='detailed')
    
]
 