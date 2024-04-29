from django.shortcuts import render,reverse
from django.views import View
from .forms import LoginForm,RegisterForm,CheckOtpForm,AddressCreationForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from random import randint
from .models import Otp,User
from django.utils.crypto import get_random_string
from uuid import uuid4
# Create your views here.
import ghasedakpack


SMS=ghasedakpack.Ghasedak("4fbaf42afdf8f35b6279b118b949e34d9a3acef5c54cf121bff6935633dafe3b")








class UserLogin(View):
    def get(self,request):
        form=LoginForm()
        return render(request,"account/login.html",{"form":form})


    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            print(f'{cd["username"]},{cd["password"]}')
            user=authenticate(username=cd["username"],password=cd["password"])
            print(user)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                form.add_error("phone","dorost vared kon")
        else:
            form.add_error("phone","cheteeeee")
        return render(request,"account/login.html",{'form':form})


class RegisterView(View):
    def get(self,request):
        form=RegisterForm()
        return render(request,"account/register.html",{"form":form})
    def post(self,request):
        form=RegisterForm(request.POST)
        if form.is_valid():
            randcod=randint(1000,9999)
            cd=form.cleaned_data
            SMS.verification({'receptor':cd["phone"], 'type': '1', 'template': 'randcode', 'param1': randcod})
            # token=get_random_string(length=100)
            token=str(uuid4())
            print(randcod)
            Otp.objects.create(phone=cd['phone'],code=randcod,token=token)
            return redirect(reverse("account:Checkotp")+f"?token={token}")

        else:
            form.add_error("phone","cheteeeee")
        return render(request,"account/register.html",{'form':form})



class ChckOtpView(View):
    def get(self,request):
        form=CheckOtpForm()
        return render(request,"account/check_otp.html",{"form":form})
    def post(self,request):
        token=request.GET.get('token')
        form=CheckOtpForm(request.POST)
        if form.is_valid():

            cd=form.cleaned_data
            if Otp.objects.filter(token=token,code=cd['code']).exists():
                otp=Otp.objects.get(token=token)
                user,is_created=User.objects.get_or_create(phone=otp.phone)
                user.backend="django.contrib.auth.backends.ModelBackend"
                login(request,user)
                otp.delete()
                return redirect("/")
            else:
                form.add_error("code","amoo codet eshtebas")
        else:
            form.add_error("code","cheteeeee")
        return render(request,"account/check_otp.html",{'form':form})

def user_logout(request):
    logout(request)
    return redirect("/")


class AddAddressView(View):
    def post(self,request):
        form=AddressCreationForm(request.POST)
        if form.is_valid():
            address=form.save(commit=False)
            address.user=request.user
            address.save()
            next_page=request.GET.get('next')
            if next_page:
                return redirect(next_page)
        return render(request,'account/add_address.html',{'form':form})
    def get(self,request):
        form=AddressCreationForm()
        return render(request,'account/add_address.html',{'form':form})


