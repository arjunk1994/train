from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render,redirect

from django.views import generic
from django.contrib.auth.models import User,auth
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from django.views.generic import View
from.forms import UserForm,EditProfile

import cgi
import cgitb
# # Create your views here.
# class IndexView(generic.ListView):
#     template_name = 'login.html'
#
#     def get_queryset(self):
#         return


class UserFormView(View):
    form_class = UserForm
    template_name= 'registration_form.html'

# blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

# process data
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            #cleaning data and normalising it
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('home')
        return render(request, self.template_name, {'form': form})


# class DataUpdate(UpdateView):
#     model = Data
#     fields = ['name','age','address','emailid','mobile']


def home(request):
    return render(request,'Frontpage.html')


def logon(request):
    if request.user.id is not None:
        auth.logout(request)
        return redirect('home')
    else:
        return render(request, 'login.html')


def login(request):
    username = request.POST.get("Username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            return redirect('home')

    return redirect('logon')


def edit_profile(request):
    if request.user.id is not None:
        if request.method == 'POST':
            form = EditProfile(request.POST, instance=request.user)

            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = EditProfile(instance=request.user)
            args = {'form': form}
            return render(request, 'edit.html', args)

    #
    #


    else:
        return render(request, 'login.html')


#
# class UserCreate(CreateView):
#     model = User
#     fields = ["Username","password",'first_name','last_name']
#
# def confirmation(request):
#     return render(request, 'registration.html')