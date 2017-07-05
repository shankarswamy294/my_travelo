from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# Create your views here.
from django.http import HttpResponse
from .models import User,Upload
from django.views import generic,View
from django.template import loader
from django.contrib.auth.views import logout,login
from  django.shortcuts  import render_to_response,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


class Home(View):
    def get(self, request):
        return render_to_response('my_travelo/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'my_travelo/signup.html', {'form': form})


class Add_User(LoginRequiredMixin,CreateView):
    model = User
    context_object_name = "all_upload"
    fields = ["name","location_from"]
    success_url = "http://127.0.0.1:8000/travelo"

class Add_upload(LoginRequiredMixin,CreateView):
    model = Upload
    context_object_name = "all_upload"
    fields = ["pic","description","name"]
    success_url = "http://127.0.0.1:8000/travelo/wall"


class Update_upload(LoginRequiredMixin,UpdateView):
    model = Upload
    context_object_name = "all_upload"
    template_name = "my_travelo/upload_form.html"
    fields = ["pic","description","name"]
    success_url = "http://127.0.0.1:8000/travelo/wall"



class Delete_upload(LoginRequiredMixin,DeleteView):
    model = Upload
    context_object_name = "all_upload"
    template_name = "my_travelo/upload_delete.html"
    success_url = "http://127.0.0.1:8000/travelo/wall"


class Wall(LoginRequiredMixin,generic.ListView):
    template_name = 'my_travelo/wall.html'
    context_object_name = 'all_wall'

    def get_queryset(self):
        return Upload.objects.all()

def Per_user_wall(request,name):
    result = Upload.objects.filter(name__name__startswith=name)
    template = loader.get_template("my_travelo/per_user_wall.html")
    context={
        'result':result,
    }
    return HttpResponse(template.render(context,request))




class Profile_user(LoginRequiredMixin,View):
    template_name='my_travelo/profile.html'
    context_object_name = 'all_wall'

    def get_queryset(self):
        username = None
        if self.user.is_authenticated():
            return Upload.objects.filter(name=View.user.username)




def my_view(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username

    result = Upload.objects.filter(name__name=username)
    template = loader.get_template("my_travelo/profile.html")
    context = {
        'result': result,
    }
    return HttpResponse(template.render(context, request))