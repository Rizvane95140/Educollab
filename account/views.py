from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from account.forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from django.contrib import messages

# from blog.models import BlogPost
def infos(request):
	context = {}
	context['user'] = request.user
	return render(request, 'infos.html', context)
	
def discussion(request):
	context = {}
	context['user'] = request.user
	return render(request, 'discussion.html', context)

def exercer(request):
    return render(request, "exercer.html")
 
def corriger(request):
    return render(request, "correction.html")

def evaluation(request):
    return render(request, "evaluation.html")

def correction_prof(request):
    return render(request, "correction_prof.html")

def modification(request):
    return render(request, "modification.html")

def add_exo(request):
    return render(request, "add_exo.html")
	
def add_ctrl(request):
    return render(request, "add_ctrl.html")

@login_required
def home_account(request):	
	context = {}
	context['user'] = request.user


	#if request.user.statut == 'PROFESSOR':
	#	return render(request, 'account/PROFESSOR/home.html', context)
	#elif request.user.statut == 'STUDENT':
	#	return render(request, 'account/STUDENT/home.html', context)

	return render(request, 'base.html', context)

	# Si c'est un prof, l'empecher de voir la page student
	# Si c'est un étudiant, l'empecher de voir la page professeur

    # Requete pour récupérer l'utilisateur

	# Variable que passe dans la vue
	
	# Tu récupère le compte ici et tu fais une condition

	# Si c'est student 
	# return render(request, "account/home_student.html", context)
	# Si c'est prof
	# return render(request, "account/home_professor.html", context)

def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)


def logout_view(request):
	logout(request)
	return redirect('/')


def login_view(request):

	context = {}

	user = request.user

	if user.is_authenticated: 
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				messages.success(request, 'Bienvenue %s !' % user.username)
				return redirect("home")

	else:
    		
		form = AccountAuthenticationForm()

	context['login_form'] = form

	# print(form)
	return render(request, "account/login.html", context)


def account_view(request):

	if not request.user.is_authenticated:
			return redirect("login")

	context = {}
	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
					"email": request.POST['email'],
					"username": request.POST['username'],
			}
			form.save()
			context['success_message'] = "Updated"
	else:
		form = AccountUpdateForm(

			initial={
					"email": request.user.email, 
					"username": request.user.username,
				}
			)

	context['account_form'] = form

	blog_posts = BlogPost.objects.filter(author=request.user)
	context['blog_posts'] = blog_posts

	return render(request, "account/account.html", context)


def must_authenticate_view(request):
	return render(request, 'account/must_authenticate.html', {})
