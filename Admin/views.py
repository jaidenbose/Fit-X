from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *

# Create your views here.

def home(request):
    if 'aid' in request.session:
        return render(request,"Admin/HomePage.html")
    else:
        return redirect('webguest:Home')

def ttype(request):
    if 'aid' in request.session:
        tty=TrainerType.objects.all()
        if request.method=="POST":
            TrainerType.objects.create(ttype_name=request.POST.get('txt_ttype'))
            return render(request,"Admin/TrainerType.html",{'TT':tty})
        else:
            return render(request,"Admin/TrainerType.html",{'TT':tty})
    else:
        return redirect('webguest:Home')
    
    
def del_ttype(request,did):
    TrainerType.objects.get(id=did).delete()
    return redirect('webadmin:TrainerType')


def subtype(request):
    if 'aid' in request.session:
        tty=TrainerType.objects.all()
        st=Subtype.objects.all()
        if request.method=="POST":
            ttypeid=request.POST.get('sel_ttype')
            tp=TrainerType.objects.get(id=ttypeid)
            Subtype.objects.create(subtype_name=request.POST.get('txt_stype'),ttype=tp)
            return render(request,"Admin/SubType.html",{'TT':tty,'ST':st})
        else:
            return render(request,"Admin/SubType.html",{'TT':tty,'ST':st})
    else:
        return redirect('webguest:Home')
    
def del_stype(request,did):
    Subtype.objects.get(id=did).delete()
    return redirect('webadmin:SubType')


def ptype(request):
    if 'aid' in request.session:
        pty=ProductType.objects.all()
        if request.method=="POST":
            ProductType.objects.create(ptype_name=request.POST.get('txt_ptype'))
            return render(request,"Admin/ProductType.html",{'PT':pty})
        else:
            return render(request,"Admin/ProductType.html",{'PT':pty})
    else:
        return redirect('webguest:Home')


def dist(request):
    if 'aid' in request.session:
        dis=District.objects.all()
        if request.method=="POST":
            District.objects.create(district_name=request.POST.get('txt_distict'))
            return render(request,"Admin/District.html",{'DS':dis})
        else:
            return render(request,"Admin/District.html",{'DS':dis})
    else:
        return redirect('webguest:Home')


def del_dis(request,did):
    District.objects.get(id=did).delete()
    return redirect('webadmin:District')


def pla(request):
    if 'aid' in request.session:
        dis=District.objects.all()
        plc=Place.objects.all()
        if request.method=="POST":
            disid=request.POST.get('sel_district')
            dist=District.objects.get(id=disid)
            Place.objects.create(place_name=request.POST.get('txt_place'),pincode=request.POST.get('txt_pincde'),district=dist)
            return render(request,"Admin/Place.html",{'DS':dis,'PL':plc})
        else:
            return render(request,"Admin/Place.html",{'DS':dis,'PL':plc})
    else:
        return redirect('webguest:Home')

def del_plc(request,plid):
    Place.objects.get(id=plid).delete()
    return redirect('webadmin:Place')



def usrveri(request):
    if 'aid' in request.session:
        usrverify=URegistration.objects.filter(user_vstatus=0)
        return render(request,"Admin/UserVerification.html",{'UV':usrverify})
    else:
        return redirect('webguest:Home')
    
def user_accept(request,auid):
    accept=URegistration.objects.get(id=auid)
    accept.user_vstatus=1
    accept.save()
    return redirect('webadmin:AcceptedUser')

def user_reject(request,ruid):
    reject=URegistration.objects.get(id=ruid)      
    reject.user_vstatus=2
    reject.save()
    return redirect('webadmin:RejectedUser')

def accepted_user(request):
    if 'aid' in request.session:
        usraccepted=URegistration.objects.filter(user_vstatus=1)
        return render(request,"Admin/AcceptedUser.html",{'UV':usraccepted})
    else:
        return redirect('webguest:Home')

def rejected_user(request):
    if 'aid' in request.session:
        usrrejected=URegistration.objects.filter(user_vstatus=2)
        return render(request,"Admin/RejectedUser.html",{'UV':usrrejected})
    else:
        return redirect('webguest:Home')



def fitveri(request):
    if 'aid' in request.session:
        fitverify=FitnessTrainer.objects.filter(fitness_vstatus=0)
        return render(request,"Admin/FitnessVerification.html",{'FV':fitverify})
    else:
        return redirect('webguest:Home')

def fitness_accept(request,afid):
    accept=FitnessTrainer.objects.get(id=afid)
    accept.fitness_vstatus=1
    accept.save()
    return redirect('webadmin:AcceptedFitness')

def fitness_reject(request,rfid):
    reject=FitnessTrainer.objects.get(id=rfid)
    reject.fitness_vstatus=2
    reject.save()
    return redirect('webadmin:RejectedFitness')

def accepted_fitness(request):
    if 'aid' in request.session:
        fitaccepted=FitnessTrainer.objects.filter(fitness_vstatus=1)
        return render(request,"Admin/AcceptedFitness.html",{'FV':fitaccepted})
    else:
        return redirect('webguest:Home')


def rejected_fitness(request):
    if 'aid' in request.session:
        fitrejected=FitnessTrainer.objects.filter(fitness_vstatus=2)
        return render(request,"Admin/RejectedFitness.html",{'FV':fitrejected})
    else:
        return redirect('webguest:Home')



def yogveri(request):
    if 'aid' in request.session:
        yogverify=YogaTrainer.objects.filter(yoga_vstatus=0)
        return render(request,"Admin/YogaVerification.html",{'YV':yogverify})
    else:
        return redirect('webguest:Home')
    

def yoga_accept(request,ayid):
    accept=YogaTrainer.objects.get(id=ayid)
    accept.yoga_vstatus=1
    accept.save()
    return redirect('webadmin:AcceptedYoga')

def yoga_reject(request,ryid):
    reject=YogaTrainer.objects.get(id=ryid)
    reject.yoga_vstatus=2
    reject.save()
    return redirect('webadmin:RejectedYoga')

def accepted_yoga(request):
    if 'aid' in request.session:
        yogaccepted=YogaTrainer.objects.filter(yoga_vstatus=1)
        return render(request,"Admin/AcceptedYoga.html",{'FV':yogaccepted})
    else:
        return redirect('webguest:Home')

def rejected_yoga(request):
    if 'aid' in request.session:
        yogrejected=YogaTrainer.objects.filter(yoga_vstatus=2)
        return render(request,"Admin/RejectedYoga.html",{'FV':yogrejected})
    else:
        return redirect('webguest:Home')



def zumveri(request):
    if 'aid' in request.session:
        zumverify=ZumbaTrainer.objects.filter(zumba_vstatus=0)
        return render(request,"Admin/ZumbaVerification.html",{'ZV':zumverify})
    else:
        return redirect('webguest:Home')

def zumba_accept(request,azid):
    accept=ZumbaTrainer.objects.get(id=azid)
    accept.zumba_vstatus=1
    accept.save()
    return redirect('webadmin:AcceptedZumba')

def zumba_reject(request,rzid):
    reject=ZumbaTrainer.objects.get(id=rzid)
    reject.zumba_vstatus=2
    reject.save()
    return redirect('webadmin:RejectedZumba')

def accepted_zumba(request):
    if 'aid' in request.session:
        zumaccepted=ZumbaTrainer.objects.filter(zumba_vstatus=1)
        return render(request,"Admin/AcceptedZumba.html",{'ZV':zumaccepted})
    else:
        return redirect('webguest:Home')

def rejected_zumba(request):
    if 'aid' in request.session:
        zumrejected=ZumbaTrainer.objects.filter(zumba_vstatus=2)
        return render(request,"Admin/RejectedZumba.html",{'ZV':zumrejected})
    else:
        return redirect('webguest:Home')


def prdt(request):
    if 'aid' in request.session:
        pro=Product.objects.all()
        if request.method=="POST" and request.FILES:
            Product.objects.create(product_name=request.POST.get('txt_pname'),
            product_image=request.FILES.get('FilePhoto'),
            product_details=request.POST.get('txt_pdetails'),
            product_rate=request.POST.get('txt_prate'),
            product_brand=request.POST.get('txt_pbrand'))
            return render(request,"Admin/Product.html",{'PR':pro})
        else:
            return render(request,"Admin/Product.html",{'PR':pro})
    else:
        return redirect('webguest:Home')


def del_pro(request,pid):
    Product.objects.get(id=pid).delete()
    return redirect('webadmin:Product')


def stok(request,pid):
    pdt=Product.objects.get(id=pid)
    sto=Stock.objects.all()
    if request.method=="POST":
        Stock.objects.create(stock_quantity=request.POST.get('txt_squantity'),product=pdt)
        return render(request,"Admin/Stock.html",{'ST':sto})
    else:
        return render(request,"Admin/Stock.html",{'ST':sto})
    
    
    

def viewcomplaint(request):
    user=Complaint.objects.filter(user__gt=0) 
    fitness=Complaint.objects.filter(fitnesstrainer_id__gt=0) 
    yoga=Complaint.objects.filter(yogatrainer_id__gt=0) 
    zumba=Complaint.objects.filter(zumbatrainer_id__gt=0) 
    return render(request,'Admin/View_Complaint.html',{'user':user,'fitness':fitness,'yoga':yoga,'zumba':zumba})

def viewfeedback(request):
    user=Feedback.objects.filter(user__gt=0) 
    fitness=Feedback.objects.filter(fitnesstrainer_id__gt=0) 
    yoga=Feedback.objects.filter(yogatrainer_id__gt=0) 
    zumba=Feedback.objects.filter(zumbatrainer_id__gt=0)
    return render(request,'Admin/View_Feedback.html',{'user':user,'fitness':fitness,'yoga':yoga,'zumba':zumba})

def reply(request,did):
    seld=Complaint.objects.get(id=did)
    if request.method=="POST":
        seld.reply=request.POST.get('reply')
        seld.c_status=1
        seld.save()
        return redirect('webadmin:viewcomplaint')
    else:
        return render(request,'Admin/Reply.html',{'doc':seld})
    

    
    
def logout(request):
    del request.session['aid']
    return redirect('webguest:Home')