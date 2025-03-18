from django.urls import path
from Guest import views
app_name="webguest"

urlpatterns = [
    path('UserReg/',views.ureg,name="UserRegistration"),
    path('ajaxplc/',views.ajax_plc,name="Ajax_Place"),    
    path('Login/',views.log,name="Login"),
    path('fitness/',views.fitness,name="FitnessTrainer"),
    path('Yoga/',views.yoga,name="YogaTrainer"),
    path('Zumba/',views.zumba,name="ZumbaTrainer"),

    path('ajax_subtype/',views.ajax_subtype,name="Ajax_Subtype"),

    path('',views.home,name="Home"),
]