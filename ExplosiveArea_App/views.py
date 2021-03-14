from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Excercise
from .forms import ExcerciseForm

# Create your views here.
def home_view(request, *args, **kargs):
    context = {
        'athelete_section' : Excercise.ATHLETIC_FOR_ATHLETICS,
        'olympic_section' : Excercise.ATHLETIC_FOR_OLYMPICS,
        'gym_section' : Excercise.GYM
    }
    return render(request, 'ExplosiveArea_App/home.html', context)

def section_view(request, section, *args, **kargs):
    # request.GET['basketball']
    context = {
        'excercises': Excercise.objects.filter(section = section),
        'section': section,
        'section_name': Excercise.sections[section],
        'basketball_section': 'basketball' in request.GET.keys()
    }
    return render(request, 'ExplosiveArea_App/section.html', context)

def excercise_view(request, section, title, id, *args, **kargs):
    context = {
        'excercise': Excercise.objects.get(id=id),
        'section': section,
        'basketball_section': 'basketball' in request.GET.keys()
    }
    return render(request, 'ExplosiveArea_App/excercise.html', context)

@login_required(login_url='')
def excercise_delete(request, section, id, *args, **kargs):
    Excercise.objects.get(id=id).delete()
    return redirect('section', section)

@login_required(login_url='')
def excercise_edit_view(request, section, title, id, *args, **kargs):
    excercise = Excercise.objects.get(id=id)
    form = ExcerciseForm(instance=excercise)

    if request.method == 'POST':
        form = ExcerciseForm(request.POST, request.FILES, instance=excercise)
        if form.is_valid():
            form.save()
            return redirect('excercise', section, title, id)

    context = {
        'form': form,
        'excercise': Excercise.objects.get(id=id),
        'section': section,
        'basketball_section': 'basketball' in request.GET.keys()
    }
    return render(request, 'ExplosiveArea_App/excercise_edit.html', context)

@login_required(login_url='')
def excercise_add_view(request, section, *args, **kargs):
    form = ExcerciseForm()
    if request.method == 'POST':
        form = ExcerciseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('section', section)

    context = {
        'form': form,
        'section': section,
        'section_name': Excercise.sections[section],
        'basketball_section': 'basketball' in request.GET.keys()
    }
    return render(request, 'ExplosiveArea_App/excercise_add.html', context)

def basketball_view(request, *args, **kargs):
    context = {
        'planner_section' : Excercise.BASKETBALL_PLANNER,
        'excercises_section' : Excercise.BASKETBALL_EXCERCISES,
        'moves_section' : Excercise.BASKETBALL_MOVES,
        'defence_section' : Excercise.BASKETBALL_DEFENCE
    }
    return render(request, 'ExplosiveArea_App/basketball.html', context)

def login_view(request, *args, **kargs):
    username = request.GET['username']
    password = request.GET['password']

    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return JsonResponse({'success': True, 'error': ''})
    else:
        return JsonResponse({'success': False, 'error': 'שם משתמש או סיסמא לא נכונים'})

def logout_view(request, *args, **kargs):
    logout(request)
    return redirect('home')

        

 