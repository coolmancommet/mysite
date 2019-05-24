from django.shortcuts import render,redirect
from django.contrib import messages
from .form import URF,U_U_f,P_U_f
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog.models import post

def suc(request):
    return render(request,'cu/sucess.html')

def signup(request):
    if request.method=='POST':
        form=URF(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'account created for {username} !')
            return redirect('suc')

    else:
        form=URF()
    return render(request,'cu/hello.html',{'form':form})

@login_required
def Profile(request):
    au=request.user.username

    if request.method=='POST':
        u_form=U_U_f(request.POST,instance=request.user)
        p_form=P_U_f(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'profile is Successfully updated for {request.user.username}!!!')
            return redirect('profile')

    else:

         u_form=U_U_f(instance=request.user)
         p_form=P_U_f(instance=request.user.profile)

    content={
    'p_form':p_form,
    'u_form':u_form,
    'post':post.objects.filter(author__in=User.objects.filter(username=au)),
     }
    return render(request,'log/profile.html',content)
