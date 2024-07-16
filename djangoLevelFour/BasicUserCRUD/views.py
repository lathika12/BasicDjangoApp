from django.shortcuts import render
from BasicUserCRUD.models import UserProfile
from . import forms
# Create your views here.

def index(request):
    return render(request,'BasicUserCRUD/index.html')

def users_profile(request):
    userprofile = forms.UserForm()

    if request.method == 'POST':
        userform = forms.UserForm(request.POST, request.FILES)

        if userform.is_valid():
            userform.save()
            print(userform.cleaned_data['first_name'])
            print(userform.cleaned_data['last_name'])
            print(userform.cleaned_data['email'])
            print(userform.cleaned_data['phone'])
            print(userform.cleaned_data['about'])



    return render(request,'BasicUserCRUD/userprofile.html',{'userprofile':userprofile})

def view_user_data(request):
    usersls = UserProfile.objects.order_by('first_name')
    return render(request,'BasicUserCRUD/allusers.html',{'usersls':usersls})