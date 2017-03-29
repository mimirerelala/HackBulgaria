from django.shortcuts import render
from .models import User

# Create your views here.
def register(request):
	if request.method == 'POST':
		user_email= request.POST['username_key']
		in_pass = request.POST['password_value']
		new_user_to_register = User(email = user_email, password = in_pass)
		if new_user_to_register not in User.objects.all():
			new_user_to_register.save()
			#auto login in => should refactor to use
			#the same function as the login forms
			request.session['user_id'] = user_email
			return render(request, 'profile.html',locals())
		#create helper, to use User.objects.filter(email = email)
		#filter is changed, dont use it!
		#do try/except
		else:
			error = 'User exists'
	return render(request, 'register.html', locals())



def login(request):
	if request.method == 'POST':
		in_user_name = request.POST['username_key']
		if User.exists(in_user_name):
			m = User.objects.get(email= in_user_name)
			if m.password == request.POST['password_value']:
				user_email = m.email
				request.session['user_id'] = user_email
				return render(request, 'profile.html', locals())
			else:
			 	error = "wrong pass"
		else:
			error = "User does not exist!"
	return render(request, 'login.html',locals())

def logout(request):
    try:
        del request.session['user_id']
        #better flush the session
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def home(request):
	#email = sessions.get..
	#if not - return to login

#check if logged - redirect
#use url names (name in url patern)
#import the django "reverse" module
#then use revers(name) instead ot path


#you can also use tempalte tag url, within the html template
#to get the name/alias from the action tag for example


