from django.shortcuts import render,redirect
from Guest.models import *
from .models import *
from User.models import *

# Create your views here.


def home(request):
    if 'fid' in request.session:
        fit=FitnessTrainer.objects.get(id=request.session['fid'])
        return render(request,"FitnessTrainer/HomePage.html",{'FIT':fit})
    else:
        return redirect('webguest:Home')

def myprofile(request):
    if 'fid' in request.session:
        FIT=FitnessTrainer.objects.get(id=request.session['fid'])
        return render(request,"FitnessTrainer/MyProfile.html",{'FIT':FIT})
    else:
        return redirect('webguest:Home')


def editprofile(request):
    if 'fid' in request.session:
        fit=FitnessTrainer.objects.get(id=request.session['fid'])
        if request.method=="POST":
            fit.fitness_name=request.POST.get('txt_name')
            fit.fitness_contact=request.POST.get('txt_contact')
            fit.fitness_email=request.POST.get('txt_email')
            fit.fitness_address=request.POST.get('txt_address')
            fit.save()
            return redirect('webfitness:EditProfile')
        return render(request,"FitnessTrainer/EditProfile.html",{'FIT':fit})
    else:
        return redirect('webguest:Home')


def changepassword(request):
    if 'fid' in request.session:
        change=FitnessTrainer.objects.get(id=request.session['fid'])
        if request.method=="POST":
            pwd=change.fitness_password
            currnt=request.POST.get('txt_cpassword')
            if pwd == currnt:
                change=FitnessTrainer.objects.get(id=request.session['fid'])
                new=request.POST.get('txt_npassword')
                change.fitness_password=new
                change.save()
                return redirect('webguest:Login')
            else:
                error="Incrrect Password!!"
                return render(request,"FitnessTrainer/ChangePassword.html",{'ER':error})
        else:
            return render(request,"FitnessTrainer/ChangePassword.html")
    else:
        return redirect('webguest:Home')


def fitveri(request):
    if 'fid' in request.session:
        fitverify=FitnessTrainer.objects.filter(fitness_vstatus=0)
        return render(request,"FitnessTrainer/FitnessVerification.html",{'FV':fitverify})
    else:
        return redirect('webguest:Home')


def fitnesspackage(request):
    if 'fid' in request.session:
        fittness=FitnessTrainer.objects.get(id=request.session['fid'])
        pac=Package.objects.filter(fitnesstrainer_id=fittness)
        if request.method=="POST" and request.FILES:
            Package.objects.create(package_name=request.POST.get('txt_name'),
            package_details=request.POST.get('txt_details'),
            package_duration=request.POST.get('txt_duration'),
            package_fees=request.POST.get('txt_fees'),
            fitnesstrainer_id=fittness,
            package_photo=request.FILES.get('txt_photo'))
            return render(request,"FitnessTrainer/FitnessPackage.html",{'PA':pac})
        else:
            return render(request,"FitnessTrainer/FitnessPackage.html",{'PA':pac})
    else:
        return redirect('webguest:Home')



def del_package(request,did):
    Package.objects.get(id=did).delete()
    return redirect('webfitness:FitnessPackage')


def add_course(request,pkid):
    pck=Package.objects.get(id=pkid)
    cs=Course.objects.filter(package=pck).order_by('course_day')
    if request.method=="POST" and request.FILES:
        Course.objects.create(package=pck,course_details=request.POST.get('txt_details'),
                              course_video=request.FILES.get('video_file'),course_day=request.POST.get('txt_day'))
        return render(request,"FitnessTrainer/FitnessCourse.html",{'COURSE':cs})
    else:
        return render(request,"FitnessTrainer/FitnessCourse.html",{'COURSE':cs})
    
    
def del_course(request,did):
    Course.objects.get(id=did).delete()
    return redirect('webfitness:FitnessPackage')



def viewbookings(request):
    if 'fid' in request.session:
        fittness=FitnessTrainer.objects.get(id=request.session['fid'])
        bkp=BookPackage.objects.filter(package__fitnesstrainer_id=fittness,booking_status=0)
        return render(request,"FitnessTrainer/ViewBookings.html",{'BKP':bkp})
    else:
        return redirect('webguest:Home')



def booking_accept(request,abid):
    acceptb=BookPackage.objects.get(id=abid)
    acceptb.booking_status=1
    acceptb.save()
    return redirect('webfitness:AcceptedBookings')


def booking_reject(request,rbid):
    rejectb=BookPackage.objects.get(id=rbid)
    rejectb.booking_status=2
    rejectb.save()
    return redirect('webfitness:RejectedBookings')



def acceptedbookings(request):
    if 'fid' in request.session:
        fittness=FitnessTrainer.objects.get(id=request.session['fid'])
        bkp=BookPackage.objects.filter(package__fitnesstrainer_id=fittness,booking_status=1)
        return render(request,"FitnessTrainer/AcceptedBookings.html",{'BKP':bkp})
    else:
        return redirect('webguest:Home')




def rejectedbookings(request):
    if 'fid' in request.session:
        fittness=FitnessTrainer.objects.get(id=request.session['fid'])
        bkp=BookPackage.objects.filter(package__fitnesstrainer_id=fittness,booking_status=2)
        return render(request,"FitnessTrainer/RejectedBookings.html",{'BKP':bkp})
    else:
        return redirect('webguest:Home')
    
    
    
def complaint(request):
    fittness=FitnessTrainer.objects.get(id=request.session['fid'])
    seld=Complaint.objects.filter(fitnesstrainer_id=fittness)
    if request.method=="POST":
        Complaint.objects.create(title=request.POST.get('title'),content=request.POST.get('content'),fitnesstrainer_id=fittness)
        return render(request,'FitnessTrainer/Complaints.html',{'seld':seld})
    else:
        
        return render(request,'FitnessTrainer/Complaints.html',{'seld':seld})

def feedback(request):
    fittness=FitnessTrainer.objects.get(id=request.session['fid'])
    seld=Feedback.objects.filter(fitnesstrainer_id=fittness)
    if request.method=="POST":
        Feedback.objects.create(description=request.POST.get('description'),fitnesstrainer_id=fittness)
        return render(request,'FitnessTrainer/Feedbacks.html',{'seld':seld})
    else:
        return render(request,'FitnessTrainer/Feedbacks.html',{'seld':seld})



def logout(request):
    del request.session['fid']
    return redirect('webguest:Home')




# ---------------------------


def chat(request, cid):
    chatobj = BookPackage.objects.get(id=cid)
    if request.method == "POST":
        cied = request.POST.get("cid")
        # print(cied)
        ciedobj = URegistration.objects.get(id=cied)
        sobj = FitnessTrainer.objects.get(id=request.session["fid"])
        content = request.POST.get("msg")
        # print(cied)
        print(content)
        Chat.objects.create(
            from_fitness=sobj, to_user=ciedobj, content=content, from_user=None, to_fitness=None)
        return render(request, 'FitnessTrainer/Chat.html', {"chatobj": chatobj})
    else:
        return render(request, 'FitnessTrainer/Chat.html', {"chatobj": chatobj})


def loadchat(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid

    cid1 = request.session["cid"]
    # print(cid1)

    # print(cid)
    shopobj = URegistration.objects.get(id=cid)
    # print(userobj)
    sid = request.session["fid"]
    # print(sid)
    suserobj = FitnessTrainer.objects.get(id=request.session["fid"])
    # chatobj1 = Chat.objects.filter(Q(to_user=suserobj) | Q(
    #     from_user=suserobj), Q(to_shop=shopobj) | Q(from_shop=shopobj))
    # print(chatobj1)  # send message

    # print(chatobj2)  # recived msg
    chatobj = Chat.objects.raw(
        "select * from User_chat c inner join Guest_fitnesstrainer u on (u.id=c.from_fitness_id) or (u.id=c.to_fitness_id) WHERE  c.from_user_id=%s or c.to_user_id=%s order by c.date", params=[(cid1), (cid1)])

    print(chatobj.query)

    return render(request, 'FitnessTrainer/Load.html', {"obj": chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})
