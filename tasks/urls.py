from django.urls import path, include # type: ignore
from . import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('helloWorld/', views.helloWorld),
    path('', views.tasklist, name='task-list'),
    path('yourname/<str:name>', views.yourname, name='your-name'),
    path('newtask', views.newtask, name='newtask'),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('edit/<int:id>', views.edittask, name='edittask' ),
    path('delete/<int:id>', views.deletetask, name='delete-task' ),
    path('changestatus/<int:id>', views.changestatus, name='changestatus' ),
    path('tasklistcreate/', views.TaskListCreate.as_view(), name='tasks-view-create-view' ),
    path('tasklistcreate/<int:pk>/', views.TaskListRetrieveUpdateDestroyAPIView.as_view(), name='TaskListRetrieveUpdateDestroyAPIView' ),
]