from django.shortcuts import render,redirect
from Guest.models import *
from FitnessTrainer.models import *
from User.models import *
# Create your views here.


def home(request):
    if 'zid' in request.session:
        zum=ZumbaTrainer.objects.get(id=request.session['zid'])
        return render(request,"ZumbaTrainer/HomePage.html",{'ZUM':zum}) 
    else:
        return redirect('webguest:Home')


def myprofile(request):
    if 'zid' in request.session:
        zum=ZumbaTrainer.objects.get(id=request.session['zid'])
        return render(request,"ZumbaTrainer/MyProfile.html",{'ZUM':zum})
    else:
        return redirect('webguest:Home')


def editpro(request):
    if 'zid' in request.session:
        zum=ZumbaTrainer.objects.get(id=request.session['zid'])
        if request.method=="POST":
            zum.zumba_name=request.POST.get('txt_name')
            zum.zumba_contact=request.POST.get('txt_contact')
            zum.zumba_email=request.POST.get('txt_email')
            zum.zumba_address=request.POST.get('txt_address')
            zum.save()
            return redirect('webzumba:EditProfile')
        return render(request,"ZumbaTrainer/EditProfile.html",{'ZUM':zum})
    else:
        return redirect('webguest:Home')

def chapas(request):
    if 'zid' in request.session:
        change=ZumbaTrainer.objects.get(id=request.session['zid'])
        if request.method=="POST":
            pwd=change.zumba_password
            currnt=request.POST.get('txt_cpassword')
            if pwd == currnt:
                change=ZumbaTrainer.objects.get(id=request.session['zid'])
                new=request.POST.get('txt_npassword')
                change.zumba_password=new
                change.save()
                return redirect('webguest:Login')
            else:
                error="Incrrect Password!!"
                return render(request,"ZumbaTrainer/ChangePassword.html",{'ER':error})
        else:
            return render(request,"ZumbaTrainer/ChangePassword.html")
    else:
        return redirect('webguest:Home')


def zumbapackage(request):
    if 'zid' in request.session:
        zumba=ZumbaTrainer.objects.get(id=request.session['zid'])
        pac=Package.objects.filter(zumbatrainer_id=zumba)
        if request.method=="POST" and request.FILES:
            Package.objects.create(package_name=request.POST.get('txt_name'),
            package_details=request.POST.get('txt_details'),
            package_duration=request.POST.get('txt_duration'),
            package_fees=request.POST.get('txt_fees'),
            zumbatrainer_id=zumba,
            package_photo=request.FILES.get('txt_photo'))
            return render(request,"ZumbaTrainer/ZumbaPackage.html",{'PA':pac})
        else:
            return render(request,"ZumbaTrainer/ZumbaPackage.html",{'PA':pac})
    else:
        return redirect('webguest:Home')
    
    
    
def del_package(request,did):
    Package.objects.get(id=did).delete()
    return redirect('webzumba:ZumbaPackage')



def add_course(request,pkid):
    pck=Package.objects.get(id=pkid)
    cs=Course.objects.filter(package=pck).order_by('course_day')
    if request.method=="POST" and request.FILES:
        Course.objects.create(package=pck,course_details=request.POST.get('txt_details'),
                              course_video=request.FILES.get('video_file'),course_day=request.POST.get('txt_day'))
        return render(request,"ZumbaTrainer/ZumbaCourse.html",{'COURSE':cs})
    else:
        return render(request,"ZumbaTrainer/ZumbaCourse.html",{'COURSE':cs})
    
    
def del_course(request,did):
    Course.objects.get(id=did).delete()
    return redirect('webzumba:ZumbaPackage')




def viewbookings(request):
    if 'zid' in request.session:
        zumba=ZumbaTrainer.objects.get(id=request.session['zid'])
        bkp=BookPackage.objects.filter(package__zumbatrainer_id=zumba,booking_status=0)
        return render(request,"ZumbaTrainer/ViewBookings.html",{'BKP':bkp})
    else:
        return redirect('webguest:Home')


def booking_accept(request,abid):
    acceptb=BookPackage.objects.get(id=abid)
    acceptb.booking_status=1
    acceptb.save()
    return redirect('webzumba:AcceptedBookings')


def booking_reject(request,rbid):
    rejectb=BookPackage.objects.get(id=rbid)
    rejectb.booking_status=2
    rejectb.save()
    return redirect('webzumba:RejectedBookings')


def acceptedbookings(request):
    if 'zid' in request.session:
        zumba=ZumbaTrainer.objects.get(id=request.session['zid'])
        bkp=BookPackage.objects.filter(package__zumbatrainer_id=zumba,booking_status=1)
        return render(request,"ZumbaTrainer/AcceptedBookings.html",{'BKP':bkp})
    else:
        return redirect('webguest:Home')


def rejectedbookings(request):
    if 'zid' in request.session:
        zumba=ZumbaTrainer.objects.get(id=request.session['zid'])
        bkp=BookPackage.objects.filter(package__zumbatrainer_id=zumba,booking_status=2)
        return render(request,"ZumbaTrainer/RejectedBookings.html",{'BKP':bkp})
    else:
        return redirect('webguest:Home')


def complaint(request):
    zumba=ZumbaTrainer.objects.get(id=request.session['zid'])
    seld=Complaint.objects.filter(zumbatrainer_id=zumba)
    if request.method=="POST":
        Complaint.objects.create(title=request.POST.get('title'),content=request.POST.get('content'),zumbatrainer_id=zumba)
        return render(request,'ZumbaTrainer/Complaints.html',{'seld':seld})
    else:
        
        return render(request,'ZumbaTrainer/Complaints.html',{'seld':seld})

def feedback(request):
    zumba=ZumbaTrainer.objects.get(id=request.session['zid'])
    seld=Feedback.objects.filter(zumbatrainer_id=zumba)
    if request.method=="POST":
        Feedback.objects.create(description=request.POST.get('description'),zumbatrainer_id=zumba)
        return render(request,'ZumbaTrainer/Feedbacks.html',{'seld':seld})
    else:
        return render(request,'ZumbaTrainer/Feedbacks.html',{'seld':seld})




def logout(request):
    del request.session['zid']
    return redirect('webguest:Home')