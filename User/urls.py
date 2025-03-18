from django.urls import path
from User import views
app_name="webuser"

urlpatterns = [
    path('userhome/',views.home,name="Home"),

    path('myprofile/',views.myprofile,name="MyProfile"),
    path('editprofile/',views.editpro,name="EditProfile"),
    path('changepassword/',views.chapas,name="ChangePassword"),

    path('searchtrainers/',views.search_trainers,name="SearchTrainers"),  

    path('fitnesspackages/<int:ftid>',views.fitness_packages,name="FitnessPackage"),  
    path('bookfp/<int:fpid>',views.bookFP,name="bookfpackage"),
    
    path('yogapackages/<int:ygid>',views.yoga_packages,name="YogaPackage"),
    path('bookyp/<int:ypid>',views.bookYP,name="bookypackage"),
    
    path('zumbapackages/<int:zbid>',views.zumba_packages,name="ZumbaPackage"), 
    path('bookzp/<int:zpid>',views.bookZP,name="bookzpackage"),
    
    path('bookings/',views.mybookings,name="MyBookings"),


    path('prosearch/',views.proserh,name="ProductSearch"),
    path('addtocart/<int:pid>',views.Addtocart,name="Addtocart"),
    path('mycart/',views.mycart,name="myCart"),
    path('myOrder/',views.MyOrder,name="Myorder"),
    path('cancelOrder<int:boid>/',views.Cancelorder,name="cancelbooking"),
    path('getqnty/',views.get_qnty,name="GetQty"),
    path('payment/',views.PAYMENT,name="payment"),

    path('processingpayment/',views.processingpayment,name="processingpayment"),
    path('patmentsucessful/',views.paysucess,name="patmentsucessful"),   

    path('paynow/<int:bid>',views.payment,name="paynow"),   
    
    path('viewcourse/<int:pid>',views.viewcourse,name="viewcourse"),
    
    path('complaint/',views.complaint,name="Complaint"),
    path('feedback/',views.feedback,name="Feedback"),
    
    
    path('logout/',views.logout,name="logout"), 


    path('Chat/<int:cid>/', views.chatuser, name="Chat-user"),
    path('loadchat/', views.loadchatuser, name="load-chat"),

    
]