from django.urls import path
from FitnessTrainer import views
app_name="webfitness"

urlpatterns = [
    path('fitnesshome/',views.home,name="Home"),
    path('myprofile/',views.myprofile,name="MyProfile"),
    path('editprofile/',views.editprofile,name="EditProfile"),
    path('changepassword/',views.changepassword,name="ChangePassword"),
    path('fpackage/',views.fitnesspackage,name="FitnessPackage"),    
    path('del_fpackage/<int:did>',views.del_package,name="del_package"),   
    path('add_fcourse/<int:pkid>',views.add_course,name="add_course"),  
    path('del_course/<int:did>',views.del_course,name="del_course"),  
    path('bokings/',views.viewbookings,name="ViewBookings"),   
    path('acceptb/,<int:abid>',views.booking_accept,name="accept_booking"), 
    path('rejectb/,<int:rbid>',views.booking_reject,name="reject_booking"), 
    path('acceptedbookings/',views.acceptedbookings,name="AcceptedBookings"),
    path('rejectedbookings/',views.rejectedbookings,name="RejectedBookings"),
    
    path('complaint/',views.complaint,name="Complaint"),
    path('feedback/',views.feedback,name="Feedback"),
    
    path('logout/',views.logout,name="logout"),   


    path('Chat/<int:cid>/', views.chat, name="Chat-fitness"),
    path('loadchat/', views.loadchat, name="load-chat")
]