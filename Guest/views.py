from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *

# Create your views here.

def home(request):
    return render(request,"Guest/Home.html")


def ureg(request):
    dis=District.objects.all()
    if request.method=="POST" and request.FILES:
        plcid=request.POST.get('sel_place')
        plc=Place.objects.get(id=plcid)
        URegistration.objects.create(user_name=request.POST.get('txt_name'),
        user_contact=request.POST.get('txt_contact'),
        user_email=request.POST.get('txt_email'),
        user_gender=request.POST.get('gender'),
        user_photo=request.FILES.get('txt_photo'),
        user_address=request.POST.get('txt_address'),
        user_proof=request.FILES.get('txt_proof'),
        user_age=request.POST.get('txt_age'),
        user_password=request.POST.get('txt_password'),
        place_id=plc)
        return render(request,"Guest/UserRegistration.html",{'DS':dis})
    else:
        return render(request,"Guest/UserRegistration.html",{'DS':dis})

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
def ajax_plc(request):
    dist=request.GET.get('DIST')
    plc=Place.objects.filter(district=dist)
    return render(request,"Guest/AjaxPlace.html",{'PLC':plc})


def log(request):
    if request.method=="POST":
        Email=request.POST.get('txt_email')
        Password=request.POST.get('txt_password')
        ulog=URegistration.objects.filter(user_email=Email,user_password=Password,user_vstatus=1).count()
        flog=FitnessTrainer.objects.filter(fitness_email=Email,fitness_password=Password,fitness_vstatus=1).count()
        ylog=YogaTrainer.objects.filter(yoga_email=Email,yoga_password=Password,yoga_vstatus=1).count()
        zlog=ZumbaTrainer.objects.filter(zumba_email=Email,zumba_password=Password,zumba_vstatus=1).count()
        alog=Admin.objects.filter(admin_email=Email,admin_password=Password).count()
        if ulog > 0:
            user=URegistration.objects.get(user_email=Email,user_password=Password,user_vstatus=1)
            request.session['uid']=user.id
            request.session['uname']=user.user_name
            return redirect('webuser:Home')
        elif flog > 0:
            fitness=FitnessTrainer.objects.get(fitness_email=Email,fitness_password=Password,fitness_vstatus=1)
            print(fitness)
            request.session['fid']=fitness.id
            request.session['fname']=fitness.fitness_name
            return redirect('webfitness:Home')
        elif ylog > 0:
            yoga=YogaTrainer.objects.get(yoga_email=Email,yoga_password=Password,yoga_vstatus=1)
            print(yoga)
            request.session['yid']=yoga.id
            request.session['yname']=yoga.yoga_name
            return redirect('webyoga:HomePage')
        elif zlog > 0:
            zumba=ZumbaTrainer.objects.get(zumba_email=Email,zumba_password=Password,zumba_vstatus=1)
            print(zumba)
            request.session['zid']=zumba.id
            request.session['zname']=zumba.zumba_name
            return redirect('webzumba:HomePage')
        elif alog > 0:
            admin=Admin.objects.get(admin_email=Email,admin_password=Password)
            request.session['aid']=admin.id
            request.session['aname']=admin.admin_name
            return redirect('webadmin:HomePage')
        else:
            error="Invalid Credentials!!"
            return render(request,"Guest/Login.html",{'ER':error})
    else:
        return render(request,"Guest/Login.html")


def fitness(request):
    dis=District.objects.all()
    Ttype=TrainerType.objects.all()
    if request.method=="POST" and request.FILES:
        plcid=request.POST.get('sel_place')
        plc=Place.objects.get(id=plcid)
        ttypeid=request.POST.get('sel_subtype')
        ttype=Subtype.objects.get(id=ttypeid)
        FitnessTrainer.objects.create(fitness_name=request.POST.get('txt_name'),
        fitness_address=request.POST.get('txt_address'),
        fitness_contact=request.POST.get('txt_contact'),
        fitness_email=request.POST.get('txt_email'),
        fitness_qualification=request.POST.get('txt_quali'),
        fitness_certificate=request.FILES.get('txt_certi'),
        fitness_photo=request.FILES.get('txt_photo'),
        fitness_password=request.POST.get('txt_password'),
        subtype=ttype,
        place_id=plc)
        return render(request,"Guest/FitnessTrainer.html",{'TT':Ttype,'DS':dis})
    else:
        return render(request,"Guest/FitnessTrainer.html",{'TT':Ttype,'DS':dis})


def zumba(request):
    dis=District.objects.all()
    Ttype=TrainerType.objects.all()
    if request.method=="POST" and request.FILES:
        plcid=request.POST.get('sel_place')
        plc=Place.objects.get(id=plcid)
        ttypeid=request.POST.get('sel_subtype')
        ttype=Subtype.objects.get(id=ttypeid)
        ZumbaTrainer.objects.create(zumba_name=request.POST.get('txt_name'),
        zumba_address=request.POST.get('txt_address'),
        zumba_contact=request.POST.get('txt_contact'),
        zumba_email=request.POST.get('txt_email'),
        zumba_qualification=request.POST.get('txt_quali'),
        zumba_certificate=request.FILES.get('txt_certi'),
        zumba_photo=request.FILES.get('txt_photo'),
        zumba_password=request.POST.get('txt_password'),
        subtype=ttype,
        place_id=plc)
        return render(request,"Guest/ZumbaTrainer.html",{'TT':Ttype,'DS':dis})
    else:
        return render(request,"Guest/ZumbaTrainer.html",{'TT':Ttype,'DS':dis})



def yoga(request):
    dis=District.objects.all()
    Ttype=TrainerType.objects.all()
    if request.method=="POST" and request.FILES:
        plcid=request.POST.get('sel_place')
        plc=Place.objects.get(id=plcid)
        ttypeid=request.POST.get('sel_subtype')
        ttype=Subtype.objects.get(id=ttypeid)
        YogaTrainer.objects.create(yoga_name=request.POST.get('txt_name'),
        yoga_address=request.POST.get('txt_address'),
        yoga_contact=request.POST.get('txt_contact'),
        yoga_email=request.POST.get('txt_email'),
        yoga_qualification=request.POST.get('txt_quali'),
        yoga_certificate=request.FILES.get('txt_certi'),
        yoga_photo=request.FILES.get('txt_photo'),
        yoga_password=request.POST.get('txt_password'),
        subtype=ttype,
        place_id=plc)
        return render(request,"Guest/YogaTrainer.html",{'TT':Ttype,'DS':dis})
    else:
        return render(request,"Guest/YogaTrainer.html",{'TT':Ttype,'DS':dis})



def ajax_subtype(request):
    ttyp=request.GET.get('TTYPE')
    subt=Subtype.objects.filter(ttype=ttyp)
    return render(request,"Guest/AjaxSubType.html",{'SUBT':subt})