from django.urls import path
from . import views

urlpatterns = [
    # path('', include('taskApp.urls'))
    path('login/', views.LoginView.as_view(), name='Login'),
    path('logout/', views.LogoutView.as_view(), name='Logout'),
    path('signup/', views.SignupView.as_view(), name='SignUp'),
    path('addTodo/', views.AddTodoView.as_view(), name='Add'),
    path('getTodo/<int:id>', views.getTodos.as_view(), name='GetTodo'),
    path('editTodo/<int:id>', views.editTodo.as_view(), name='EditTodo'),
    path('getTypes/<int:id>', views.getTypes.as_view(), name='GetTypes'),
    path('addType/', views.addType.as_view(), name='AddTypes'),
    path('userDetails/<int:id>', views.getUserDetails.as_view(), name='Details')
]
