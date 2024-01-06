from . import views
from django.urls import path


urlpatterns = [
    path("", views.emp_home, name="home"),     
    path("add-emp/", views.add_emp, name="add"), 
    path("home/", views.emp_home, name="home"),  
    path("delete-emp/<int:emp_id>",views.delete_emp , name="delete_emp"),  
    path("update-emp/<int:emp_id>",views.update_emp , name="update_emp"),  
    path("do-update-emp/<int:emp_id>",views.do_update_emp , name="do_update_emp"),  
]
