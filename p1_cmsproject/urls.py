from django.contrib import admin
from django.urls import path
from cmsapp.views import home,dept,adddept,remdept,stu,addstu,remstu

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home, name="home"),
    path("dept",dept, name="dept"),
    path("adddept",adddept,name="adddept"),
    path("remdept/<int:id>",remdept, name="remdept"),
    path("stu",stu,name="stu"),
    path("addstu",addstu,name="addstu"),
    path("remstu/<int:id>",remstu, name="remstu"),
    
]
