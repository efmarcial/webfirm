from django.shortcuts import render, redirect
from .forms import *  # import all forms 
from .models import * # import all models
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # Create a form instance and populate it with data from the request:
        form = QuoteForm(request.POST)
        # Check whether it's valid
        if form.is_valid():
            # proccess the data in form.cleaned_data as requiered
            print("Proccessing Data")
            # Return a sucess message back to page.
            try:
                form.save()
                print("Form saved successfully")
            except Exception as e:
                print(e)
    else:
        form = QuoteForm()
    
    context = {
        'QuoteForm' : form
    }
    
    return render(request, 'main_app/home.html', context=context)

def account(request):
    
    if request.user.is_authenticated:
        current_user = request.user
        try:
            #Get user
            user_object = CustomUser.objects.get(username=current_user)
        except CustomUser.DoesNotExist:
            print(
                "User does not exist"
            )
    
    else:
        
        print("No current user logged in")
        return redirect('Home')
    
    context = {
        "username" : user_object.username,
        "first_name" : user_object.first_name,
        "email" : user_object.email,
    }
    
    
    return render(request, 'main_app/account.html',context=context)

def register(request):
    # Check Post request is true
    if request.method == "POST":
        try:
            form = CustomUserCreationForm(request.POST)
            
            if form.is_valid():
                print("Valid Form")
                user = form.save()
                user.refresh_from_db() # Load the profile instance createdd by the signal
                user.first_name = form.cleaned_data.get('first_name')
                user.email = form.cleaned_data.get('email')
                user.save()
                print("Saved Successfully")
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username = user.username, password=raw_password)
                login(request, user)
                print("Logged In Succecsfully......redirecting to account page")
                return redirect('Account')
        except Exception as e:
            print(e)
    
    else:
        form = CustomUserCreationForm()
        print("Empty Form Created")
        
    content = {
        'form' : form
    }
    
    return render(request, 'main_app/register.html', context=content)


def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect("Account")
    else:
        # Return an "invalid login" error message
        print("Error Login")
        pass
    return render(request, 'main_app/login_page.html')

def logout_user(request):
    """_summary_

    Args:
        request user to Logout.

    Returns:
        after successful logout, redirect to Home page
    """
    try:
        logout(request)
        return redirect('Home')
    except Exception as e:
        print(e)
        

def services(request):
    return render(request, 'main_app/services.html')

def custom_web(request):
    return render(request, 'main_app/custom_web.html')

def seo(request):
    return render(request, 'main_app/seo.html')

def marketing(request):
    return render(request, 'main_app/marketing.html')

def hosting(request):
    return render(request, 'main_app/hosting.html')

def article(request):
    return render(request, 'main_app/articles.html')

def about(request):
    return render(request, 'main_app/about.html')

def blog(request):
    return render(request, 'main_app/blog.html')

def results(request):
    return render(request, 'main_app/results.html')

def contact(request):
    return render(request, 'main_app/contact.html')