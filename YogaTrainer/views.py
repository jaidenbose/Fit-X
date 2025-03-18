from django.shortcuts import render,redirect
from Guest.models import *
from FitnessTrainer.models import *
from User.models import *

# Create your views here.

def home(request):
    if 'yid' in request.session:
        yog=YogaTrainer.objects.get(id=request.session['yid'])
        return render(request,"YogaTrainer/HomePage.html",{'YOG':yog}) 
    else:
        return redirect('webguest:Home')

def myprofile(request):
    if 'yid' in request.session:
        yog=YogaTrainer.objects.get(id=request.session['yid'])
        return render(request,"YogaTrainer/MyProfile.html",{'YOG':yog})
    else:
        return redirect('webguest:Home')

def editpro(request):
    if 'yid' in request.session:
        yog=YogaTrainer.objects.get(id=request.session['yid'])
        if request.method=="POST":
            yog.yoga_name=request.POST.get('txt_name')
            yog.yoga_contact=request.POST.get('txt_contact')
            yog.yoga_email=request.POST.get('txt_email')
            yog.yoga_address=request.POST.get('txt_address')
            yog.save()
            return redirect('webyoga:EditProfile')
        return render(request,"YogaTrainer/EditProfile.html",{'YOG':yog})
    else:
        return redirect('webguest:Home')
    

def chngpasrd(request):
    if 'yid' in request.session:
        change=YogaTrainer.objects.get(id=request.session['yid'])
        if request.method=="POST":
            pwd=change.yoga_password
            currnt=request.POST.get('txt_cpassword')
            if pwd == currnt:
                change=YogaTrainer.objects.get(id=request.session['yid'])
                new=request.POST.get('txt_npassword')
                change.yoga_password=new
                change.save()
                return redirect('webguest:Login')
            else:
                error="Incrrect Password!!"
                return render(request,"YogaTrainer/ChangePassword.html",{'ER':error})
        else:
            return render(request,"YogaTrainer/ChangePassword.html")
    else:
        return redirect('webguest:Home')

    
def yogapackage(request):
    if 'yid' in request.session:
        yoga=YogaTrainer.objects.get(id=request.session['yid'])
        pac=Package.objects.filter(yogatrainer_id=yoga)
        if request.method=="POST" and request.FILES:
            Package.objects.create(package_name=request.POST.get('txt_name'),
            package_details=request.POST.get('txt_details'),
            package_duration=request.POST.get('txt_duration'),
            package_fees=request.POST.get('txt_fees'),  
            yogatrainer_id=yoga,
            package_photo=request.FILES.get('txt_photo'))
            return render(request,"YogaTrainer/YogaPackage.html",{'PA':pac})
        else:
            return render(request,"YogaTrainer/YogaPackage.html",{'PA':pac})
    else:
        return redirect('webguest:Home')
    
    
def del_package(request,did):
    Package.objects.get(id=did).delete()
    return redirect('webyoga:YogaPackage')


def add_course(request,pkid):
    pck=Package.objects.get(id=pkid)
    cs=Course.objects.filter(package=pck).order_by('course_day')
    if request.method=="POST" and request.FILES:
        Course.objects.create(package=pck,course_details=request.POST.get('txt_details'),
                              course_video=request.FILES.get('video_file'),course_day=request.POST.get('txt_day'))
        return render(request,"YogaTrainer/YogaCourse.html",{'COURSE':cs})
    else:
        return render(request,"YogaTrainer/YogaCourse.html",{'COURSE':cs})
    
    
    
def del_course(request,did):
    Course.objects.get(id=did).delete()
    return redirect('webyoga:YogaPackage')



def viewbookings(request):
    if 'yid' in request.session:
        yoga=YogaTrainer.objects.get(id=request.session['yid'])
        bkp=BookPackage.objects.filter(package__yogatrainer_id=yoga,booking_status=0)
        return render(request,"YogaTrainer/ViewBookings.html",{'BKP':bkp})
    else:
        return redirect('webguest:Home')


def booking_accept(request,abid):
    acceptb=BookPackage.objects.get(id=abid)
    acceptb.booking_status=1
    acceptb.save()
    return redirect('webyoga:AcceptedBookings')


def booking_reject(request,rbid):
    rejectb=BookPackage.objects.get(id=rbid)
    rejectb.booking_status=2
    rejectb.save()
    return redirect('webyoga:RejectedBookings')



def acceptedbookings(request):
    if 'yid' in request.session:
        yoga=YogaTrainer.objects.get(id=request.session['yid'])
        bkp=BookPackage.objects.filter(package__yogatrainer_id=yoga,booking_status=1)
        return render(request,"YogaTrainer/AcceptedBookings.html",{'BKP':bkp})
    else:
        return redirect('webguest:Home')



def rejectedbookings(request):
    if 'yid' in request.session:
        yoga=YogaTrainer.objects.get(id=request.session['yid'])
        bkp=BookPackage.objects.filter(package__yogatrainer_id=yoga,booking_status=2)
        return render(request,"YogaTrainer/RejectedBookings.html",{'BKP':bkp})
    else:
        return redirect('webguest:Home')



def complaint(request):
    yoga=YogaTrainer.objects.get(id=request.session['yid'])
    seld=Complaint.objects.filter(yogatrainer_id=yoga)
    if request.method=="POST":
        Complaint.objects.create(title=request.POST.get('title'),content=request.POST.get('content'),yogatrainer_id=yoga)
        return render(request,'YogaTrainer/Complaints.html',{'seld':seld})
    else:
        
        return render(request,'YogaTrainer/Complaints.html',{'seld':seld})

def feedback(request):
    yoga=YogaTrainer.objects.get(id=request.session['yid'])
    seld=Feedback.objects.filter(yogatrainer_id=yoga)
    if request.method=="POST":
        Feedback.objects.create(description=request.POST.get('description'),yogatrainer_id=yoga)
        return render(request,'YogaTrainer/Feedbacks.html',{'seld':seld})
    else:
        return render(request,'YogaTrainer/Feedbacks.html',{'seld':seld})




def logout(request):
    del request.session['yid']
    return redirect('webguest:Home')