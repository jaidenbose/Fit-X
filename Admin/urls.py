from django.urls import path
from Admin import views
app_name = 'webadmin'

urlpatterns = [
    path('homepage/',views.home,name="HomePage"),

    path('ttype/',views.ttype,name="TrainerType"), 
    path('delttype/<int:did>',views.del_ttype,name="Del_Ttype"),
     
    path('stype/',views.subtype,name="SubType"),
    path('delstype/<int:did>',views.del_stype,name="Del_Stype"),  

    path('ptype/',views.ptype,name="ProductType"), 

    path('district/',views.dist,name="District"),
    path('deldis/<int:did>',views.del_dis,name="Del_Dis"),
    path('place/',views.pla,name="Place"),
    path('delplc/<int:plid>',views.del_plc,name="Del_Plc"),
    path('product/',views.prdt,name="Product"),
    path('delpro/<int:pid>',views.del_pro,name="Del_Pro"),
    path('stock/<int:pid>',views.stok,name="Stock"),


    path('userveri/',views.usrveri,name="UserVerification"),

    path('acceptuser/<int:auid>',views.user_accept,name="accept_user"),
    path('acceptedu/',views.accepted_user,name="AcceptedUser"),

    path('rejectuser/<int:ruid>',views.user_reject,name="reject_user"),
    path('rejectedu/',views.rejected_user,name="RejectedUser"), 



    path('fitveri/',views.fitveri,name="FitnessVerification"), 

    path('acceptfitness/<int:afid>',views.fitness_accept,name="accept_fitness"),
    path('acceptedf/',views.accepted_fitness,name="AcceptedFitness"),
 
    path('rejectfitness/<int:rfid>',views.fitness_reject,name="reject_fitness"),
    path('rejectedf/',views.rejected_fitness,name="RejectedFitness"), 


    
    path('yogveri/',views.yogveri,name="YogaVerification"), 

    path('acceptyoga/<int:ayid>',views.yoga_accept,name="accept_yoga"),
    path('acceptedy/',views.accepted_yoga,name="AcceptedYoga"),  

    path('rejectyoga/<int:ryid>',views.yoga_reject,name="reject_yoga"),
    path('rejectedy/',views.rejected_yoga,name="RejectedYoga"),



    path('zumveri/',views.zumveri,name="ZumbaVerification"),

    path('acceptzumba/<int:azid>',views.zumba_accept,name="accept_zumba"),
    path('acceptedz/',views.accepted_zumba,name="AcceptedZumba"),

    path('rejectzumba/<int:rzid>',views.zumba_reject,name="reject_zumba"),
    path('rejectedz/',views.rejected_zumba,name="RejectedZumba"), 
    
    
    path('viewcomplaint/',views.viewcomplaint,name="viewcomplaint"),
    path('viewfeedback/',views.viewfeedback,name="viewfeedback"),
    path('reply/<int:did>',views.reply,name="reply"),
    
]