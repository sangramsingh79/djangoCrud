
from django.urls import include, path
from employee import views 
urlpatterns = [
    path('',views.addshow,name="addshow"),
    path('update',views.update),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
]
