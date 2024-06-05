from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),

    path(
        'task/api/v1/',
        views.api.task_api_list,
        name = "task_api_list",
    ),

    path(
        'task/api/v1/<int:pk>/',
        views.api.task_api_detail,
        name = "task_api_detail",
    ),
]