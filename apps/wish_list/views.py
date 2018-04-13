from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import logout
from datetime import datetime
from .models import *

# Rendered HTML Templates
def index(request):
    return render(request, 'wish_list/index.html')

def dashboard(request):
    context = {
        'items': User.objects.get(id=request.session['user_id']).lists.all(),
        'others': User.objects.exclude(id=request.session['user_id']).all()
    }
    return render(request, 'wish_list/dashboard.html', context)

def create(request):
    return render(request, 'wish_list/create.html')


def listDisplay(request, id):
    context = {
        "displays": List.objects.get(id = id),
        'users': List.objects.get(id=id).users.all()
    }
    return render(request, 'wish_list/product_display.html', context)
# Rendered HTML Templates


def logout_view(request):
    logout(request)
    return redirect('/main')

def register(request):
    print request.POST
    result = User.objects.validate_reg(request.POST)
    if result[0]:

        request.session['user_id'] = result[1].id
        request.session['user_name'] = result[1].name
        return redirect('/dashboard')
    else:
        for error in result[1]:
            messages.add_message(request, messages.INFO, error)

        return redirect('/main')


def login(request):
    result = User.objects.validate_log(request.POST)
    if result[0]:
        # True and we have a new user
        request.session['user_id'] = result[1].id
        print "THE ID:", request.session['user_id']
        request.session['user_name'] = result[1].name
        print "THE NAME:", request.session['user_name']
        return redirect('/dashboard')
    else:
        # False and we have errors to show
        for error in result[1]: # my errors list ['first name required', 'last name required']
            messages.add_message(request, messages.INFO, error)

        return redirect('/main')


def formCreate(request):
    product = request.POST['product']
    print product

    if len(product) < 0:
        messages.warning(request, 'Product must be enerted in')
        return redirect('/wish_list/create')
    elif len(product) < 3:
        messages.warning(request, 'Product must be at least 3 characters')
        return redirect('/wish_list/create')
    else:
        List.objects.create(product=product)

        listing = List.objects.get(product=product)
        this_user = User.objects.get(id=request.session['user_id'])

        this_user.lists.add(listing)

        return redirect('/dashboard')


def addList(request, id):
    wish = List.objects.get(id=id)
    wish_add = User.objects.get(id=request.session['user_id'])
    wish_add.lists.add(wish)
    return redirect('/dashboard')


def delete(request, id):
    List.objects.get(id=id).delete()
    return redirect('/dashboard')
