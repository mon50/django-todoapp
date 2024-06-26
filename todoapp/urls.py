from django.urls import path
from . import views
from .views import TaskList
from .views import TaskDetail
from .views import TaskCreate
from .views import TaskUpdate
from .views import TaskDelete
from .views import TaskListLoginView
from django.contrib.auth.views import LogoutView
from .views import RegisterTodoApp


urlpatterns = [
    path("", TaskList.as_view(),name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("create-task/", TaskCreate.as_view(), name="create-task"),
    path("edit-task/<int:pk>/", TaskUpdate.as_view(), name="edit-task"),
    path("delete-task/<int:pk>/", TaskDelete.as_view(), name="delete-task"),
    path("login/", TaskListLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterTodoApp.as_view(), name="register"),
]


