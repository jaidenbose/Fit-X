from django.shortcuts import render,redirect     
from Guest.models import *
from Admin.models import *
from User.models import *
from FitnessTrainer.models import *
# Create your views here.


def home(request):
    if 'uid' in request.session:
        usr=URegistration.objects.get(id=request.session['uid'])
        return render(request,"User/HomePage.html",{'USR':usr})
    else:
        return redirect('webguest:Home')


def myprofile(request):
    if 'uid' in request.session:
        usr=URegistration.objects.get(id=request.session['uid'])
        return render(request,"User/MyProfile.html",{'USR':usr})
    else:
        return redirect('webguest:Home')



def editpro(request):
    if 'uid' in request.session:
        usr=URegistration.objects.get(id=request.session['uid'])
        if request.method=="POST":
            usr.user_name=request.POST.get('txt_name')
            usr.user_contact=request.POST.get('txt_contact')
            usr.user_email=request.POST.get('txt_email')
            usr.user_address=request.POST.get('txt_address')
            usr.save()
            return redirect('webuser:EditProfile')
        return render(request,"User/EditProfile.html",{'USR':usr})
    else:
        return redirect('webguest:Home')



def chapas(request):
    if 'uid' in request.session:
        change=URegistration.objects.get(id=request.session['uid'])
        if request.method=="POST":
            pwd=change.user_password
            currnt=request.POST.get('txt_cpassword')
            if pwd == currnt:
                change=URegistration.objects.get(id=request.session['uid'])
                new=request.POST.get('txt_npassword')
                change.user_password=new
                change.save()
                return redirect('webguest:Login')
            else:
                error="Incrrect Password!!"
                return render(request,"User/ChangePasswproserhord.html",{'ER':error})
        else:
            return render(request,"User/ChangePassword.html")
    else:
        return redirect('webguest:Home')


def proserh(request):
    if 'uid' in request.session:
        prod=Product.objects.all()
        if request.method=="POST":
            
            prosearch=Product.objects.filter(product_name=request.POST.get('pdt_search'))
            return render(request,"User/ProductSearch.html",{'PdtSrch':prosearch})
        else:
            return render(request,"User/ProductSearch.html",{'PdtSrch':prod})
    else:
        return redirect('webguest:Home')




def myboo(request):
    if 'uid' in request.session:
        mybooking=Booking.objects.filter(user_vstatus=0)
        return render(request,"User/MyBooking.html",{'PR':mybooking})
    else:
        return redirect('webguest:Home')



def Addtocart(request,pid):
    photo=Product.objects.all()
    if 'uid' in request.session:
        message=""
        prod=Product.objects.get(id=pid)
        userid=URegistration.objects.get(id=request.session["uid"])
        bcount=Booking.objects.filter(user=userid,booking_status=0).count()
        if bcount>0:
            book=Booking.objects.get(user=userid,booking_status=0)
            id=book.id
            bc=Booking.objects.get(id=id)
            bpcount=Cart.objects.filter(booking=bc,product=prod).count()
            if bpcount>0:
                message="AlreadyAddedtoCart"
                return render(request,"User/ProductSearch.html",{"mess":message,'name':photo})
            else:
                Cart.objects.create(product=prod,booking=bc)
                message="AddedtoCart"
                return render(request,"User/ProductSearch.html",{"mess":message,'name':photo})
        else:
            Booking.objects.create(user=userid)
            bid=Booking.objects.filter(user=userid,booking_status=0).count()
            if bid>0:
                b=Booking.objects.get(user=userid,booking_status=0)
                ids=b.id
                bc=Booking.objects.get(id=ids)
                Cart.objects.create(booking=bc,product=prod)
                message="AddedtoCart"
                return render(request,"User/ProductSearch.html",{"mess":message,'name':photo})
            else:
                return render(request,"User/ProductSearch.html",{"mess":message,'name':photo})
    else:
        return redirect("Guest:login")


def mycart(request):
    if 'uid' in request.session:
        userid=URegistration.objects.get(id=request.session["uid"])
        if request.method=="POST":
            return redirect("webuser:payment")
        else:
            bcount=Booking.objects.filter(user=userid,booking_status=0).count()
            if bcount>0:
                bid=Booking.objects.get(user=userid,booking_status=0)
                ids=bid.id
                request.session["bookingsid"]=ids
                bc=Booking.objects.get(id=ids)
                cartob=Cart.objects.filter(booking=bc)
                return render(request,"User/Mycart.html",{'data':cartob})
            else:
                return render(request,"User/Mycart.html")
    else:
        return redirect("webguest:login")
    
def MyOrder(request):
    if 'uid' in request.session:
        usrid=URegistration.objects.get(id=request.session["uid"])
        prdt=Cart.objects.filter(booking__user=usrid,booking__booking_status__gte=1)
        return render(request,"User/myorders.html",{'Prdt':prdt})
    else:
        return redirect("Guest:login")

def Cancelorder(request,boid):
    if 'uid' in request.session:
        bid=Booking.objects.get(id=boid)
        bid.booking_status=4
        bid.save()
        return redirect("webuser:Myorder")
    else:
        return redirect("webguest:login")


def get_qnty(request):
    if 'uid' in request.session:
        qty=request.GET.get('QTY')
        alt=request.GET.get('ALT')
        cart=Cart.objects.get(id=alt)
        cart.cart_quantity=qty
        cart.save()
        return redirect('webuser:myCart')
    else:
        return redirect("webguest:login")


def PAYMENT(request):
    if 'uid' in request.session:
        if request.method=="POST": 
            ids=Booking.objects.get(id=request.session["bookingsid"])
            ids.booking_status=1
            ids.save()
            return redirect("webuser:processingpayment")
        else:
            return render(request,"User/Payment.html")
    else:
        return redirect("webguest:login")




def processingpayment(request):
    if 'uid' in request.session:
        return render(request,"User/runpayment.html")
    else:
        return redirect("Guest:login")
    

def paysucess(request):
    if 'uid' in request.session:
        return render(request,"User/paysucessful.html")
    else:
        return redirect("Guest:login")


def search_trainers(request):
    ttype=TrainerType.objects.all()
    fitness=FitnessTrainer.objects.all()
    yoga=YogaTrainer.objects.all()
    zumba=ZumbaTrainer.objects.all()
    if request.method=="POST":
        check=request.POST.get('trainers')
        if check == "Fitness_Trainer":
            ttype=TrainerType.objects.all()
            fitness=FitnessTrainer.objects.all()
            return render(request,"User/SearchTrainers.html",{'TType':ttype,'FT':fitness})
        elif check == "Yoga_Trainer":
            ttype=TrainerType.objects.all()
            yoga=YogaTrainer.objects.all()
            return render(request,"User/SearchTrainers.html",{'TType':ttype,'YG':yoga})
        elif check == "Zumba_Trainer":
            ttype=TrainerType.objects.all()
            zumba=ZumbaTrainer.objects.all()
            return render(request,"User/SearchTrainers.html",{'TType':ttype,'ZB':zumba})
    else:
        return render(request,"User/SearchTrainers.html",{'TType':ttype,'FT':fitness,'YG':yoga,'ZB':zumba})
        


def fitness_packages(request,ftid):
    ft=FitnessTrainer.objects.get(id=ftid) 
    pk=Package.objects.filter(fitnesstrainer_id=ft) 
    return render(request,"User/FitnessPackages.html",{'PK':pk})

def bookFP(request,fpid):
    pk=Package.objects.get(id=fpid)
    usr=URegistration.objects.get(id=request.session['uid'])
    BookPackage.objects.create(package=pk,user=usr)
    return redirect('webuser:Home')    



def yoga_packages(request,ygid):
    yg=YogaTrainer.objects.get(id=ygid)
    pk=Package.objects.filter(yogatrainer_id=yg) 
    return render(request,"User/YogaPackages.html",{'PK':pk})


def bookYP(request,ypid):
    pk=Package.objects.get(id=ypid)
    usr=URegistration.objects.get(id=request.session['uid'])
    BookPackage.objects.create(package=pk,user=usr)
    return redirect('webuser:Home') 


def zumba_packages(request,zbid):
    zb=ZumbaTrainer.objects.get(id=zbid)
    pk=Package.objects.filter(zumbatrainer_id=zbid) 
    return render(request,"User/ZumbaPackages.html",{'PK':pk})



def bookZP(request,zpid):
    pk=Package.objects.get(id=zpid)
    usr=URegistration.objects.get(id=request.session['uid'])
    BookPackage.objects.create(package=pk,user=usr)
    return redirect('webuser:Home') 



def payment(request,bid):
    pay=BookPackage.objects.get(id=bid)
    if request.method=="POST":
        pay.payment_status=1
        pay.save()
        return redirect('webuser:processingpayment')
    else:
        return render(request,"User/Payment.html")
        
        
        
def mybookings(request):
    if 'uid' in request.session:
        usr=URegistration.objects.get(id=request.session['uid'])
        bkp=BookPackage.objects.filter(user=usr)
        return render(request,"User/MyBookings.html",{'BKP':bkp})
    else:
        return redirect('webguest:Home')
        
        
        
def viewcourse(request,pid):
    pk=Package.objects.get(id=pid)
    cour=Course.objects.filter(package=pk).order_by('course_day')
    return render(request,"User/ViewCourses.html",{'COUR':cour})



def complaint(request):
    usr=URegistration.objects.get(id=request.session['uid'])
    seld=Complaint.objects.filter(user=usr)
    if request.method=="POST":
        Complaint.objects.create(title=request.POST.get('title'),content=request.POST.get('content'),user=usr)
        return render(request,'User/Complaints.html',{'seld':seld})
    else:
        
        return render(request,'User/Complaints.html',{'seld':seld})

def feedback(request):
    usr=URegistration.objects.get(id=request.session['uid'])
    seld=Feedback.objects.filter(user=usr)
    if request.method=="POST":
        Feedback.objects.create(description=request.POST.get('description'),user=usr)
        return render(request,'User/Feedbacks.html',{'seld':seld})
    else:
        return render(request,'User/Feedbacks.html',{'seld':seld})





def logout(request):
    del request.session['uid']
    return redirect('webguest:Home')



# -------------------------------------------------





def chatuser(request, cid):
    chatobj = BookPackage.objects.get(id=cid)
    if request.method == "POST":
        cied = request.POST.get("cid")
        # print(cied)
        ciedobj = FitnessTrainer.objects.get(id=cied)
        sobj = URegistration.objects.get(id=request.session["uid"])
        content = request.POST.get("msg")
        # print(cied)
        # print(content)
        Chat.objects.create(
            from_user=sobj, to_fitness=ciedobj, content=content, from_fitness=None, to_user=None)
        return render(request, 'User/Chat.html', {"chatobj": chatobj})
    else:
        return render(request, 'User/Chat.html', {"chatobj": chatobj})


def loadchatuser(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid

    cid1 = request.session["cid"]
    # print(cid1)

    # print(cid)
    shopobj = FitnessTrainer.objects.get(id=cid)
    # print(userobj)
    sid = request.session["uid"]
    # print(sid)
    suserobj = URegistration.objects.get(id=request.session["uid"])
    # chatobj1 = Chat.objects.filter(Q(to_user=suserobj) | Q(
    #     from_user=suserobj), Q(to_shop=shopobj) | Q(from_shop=shopobj))
    # print(chatobj1)  # send message

    # print(chatobj2)  # recived msg
    chatobj = Chat.objects.raw(
        "select * from User_chat c inner join Guest_uregistration u on (u.id=c.from_user_id) or (u.id=c.to_user_id) WHERE  c.from_fitness_id=%s or c.to_fitness_id=%s order by c.date", params=[(cid1), (cid1)])

    print(chatobj.query)

    return render(request, 'User/Load.html', {"obj": chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})
