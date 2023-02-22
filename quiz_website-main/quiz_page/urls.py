from django.urls import path,re_path


from . import views


urlpatterns = [
    path("",views.starting_page,name="starting_page"),
    path("login",views.login_user,name="login_user"),
    path("student_dash_board",views.student_dashboard,name="dashboard"),
    path("logout_user",views.logout_user,name="logout"),
    path("register_user",views.register_user,name="register"),
    path('quiz',views.quiz,name="quiz"),
    path('result',views.result,name="result")

    #re_path(r'^register$',views.registerApi),
    #re_path(r'^register/([A-Za-z0-9]+)$',views.registerApi),
    #re_path(r'^login_check$',views.login_check),
    #re_path(r'^login_check/([A-Za-z0-9]+)$',views.login_check)
    #re_path('<uuid:id>',views.registerApi)
]