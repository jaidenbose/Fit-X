from django.urls import path
from YogaTrainer import views
app_name="webyoga"

urlpatterns = [
    path('home/',views.home,name="HomePage"),
    
    path('myprofile/',views.myprofile,name="MyProfile"),
    path('editprofie/',views.editpro,name="EditProfile"),
    path('changepassword/',views.chngpasrd,name="ChangePassword"),
    
    path('yogapac/',views.yogapackage,name="YogaPackage"),
    path('del_ypackage/<int:did>',views.del_package,name="del_package"),
    
    path('add_ycourse/<int:pkid>',views.add_course,name="add_course"),   
    path('del_course/<int:did>',views.del_course,name="del_course"),
    
    path('bokings/',views.viewbookings,name="ViewBookings"),   
    path('acceptb/,<int:abid>',views.booking_accept,name="accept_booking"), 
    path('rejectb/,<int:rbid>',views.booking_reject,name="reject_booking"), 
    
    path('acceptedbookings/',views.acceptedbookings,name="AcceptedBookings"),
    path('rejectedbookings/',views.rejectedbookings,name="RejectedBookings"),
    
    path('complaint/',views.complaint,name="Complaint"),
    path('feedback/',views.feedback,name="Feedback"),
    
    path('logout/',views.logout,name="logout"), 
]