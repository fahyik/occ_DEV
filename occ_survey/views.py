from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import json
# Create your views here.

def index(request):
	a = AdminText.objects.get(pk=1)
	adminText = [
		a.update1,
		a.update2,
		a.update3,
	]
	
	context = {"adminText": adminText, }
	try:
		del request.session['redirect_logout']
		context = {"logged_out": 1,}
	except KeyError:
		pass

	return render(request, 'occ_survey/index.html', context)

@login_required
def survey(request, survey_name):
	#get userprofile
	user_profile = UserProfile.objects.get(user=request.user)
	a = AdminText.objects.get(pk=1)
	
	allow = False
	
	if survey_name == "profile":
		if user_profile.profile_isDone == 0:
			allow = True
			survey_cat ={"desc": a.profile}
	elif survey_name =="comfort":
		if user_profile.comfort_isDone == 0:
			allow = True
			survey_cat ={"desc": a.comfort}
	elif survey_name =="control":
		if user_profile.control_isDone == 0:
			allow = True
			survey_cat ={"desc": a.control}
	
	if allow:
		question_list = Question.objects.filter(question_cat=survey_name).order_by("order")
		for question in question_list:
			question.choices = [ 
				question.choice.choice1,
				question.choice.choice2,
				question.choice.choice3,
				question.choice.choice4,
				question.choice.choice5,
			]
			
		survey_cat.update({ 
			"cat": question_list[0].question_cat, 
			"title": question_list[0].question_cat.title(), 
		})
		
		context = { "question_list": question_list, "survey_cat": survey_cat, }
		return render(request, 'occ_survey/survey.html', context)
	else:
		return render(request, 'occ_survey/base.html', {"text": "You have already completed this survey!",})

def submit_survey(request):
	question_count = int(request.POST["question_count"])
	
	for x in range(1, question_count+1):
		question_id = request.POST["Q"+str(x)+"_id"]
		answer = request.POST["Q"+str(x)]
		
		#foreign key
		q = Question.objects.get(id=question_id)
		
		#new Answer object
		a = Answer()
		a.question = q
		a.username = request.user.username
		try:
			a.answer  = int(answer)
		except:
			a.answer = None
			a.answer_text = answer
		
		a.save()
		
	#get UserProfile
	u = UserProfile.objects.get(username=request.user.username)
	if request.POST["survey_cat"] == "profile" :
		u.profile_isDone = 1
	elif request.POST["survey_cat"] == "comfort" :
		u.comfort_isDone = 1
	elif request.POST["survey_cat"] == "control" :
		u.control_isDone = 1
	
	u.save()
	
	#return HttpResponse("Answer to question: " + question_id + " is " + answer)
	return render(request, 'occ_survey/base.html', {"text": "Thank you for submitting!",})
	
def user_login(request):
	
	if request.user.is_authenticated():
		print request.user
		return render(request, 'occ_survey/index.html', {"logged_out": 2,})
	
	elif request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		
		user = authenticate(username=username, password=password)
		
		if user:
			if user.is_active:
			
				login(request, user)
				if "next" in request.POST:
					return HttpResponseRedirect(request.POST["next"])
				else:
					return HttpResponseRedirect(reverse("occ_survey:index"))
			
			else:
				
				return HttpResponse("Your account was disabled.")
		
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return render(request, "occ_survey/login.html", {"login": "failed"})
	
	else:
		if request.method == 'GET' and 'next' in request.GET:
			next = request.GET["next"]
			return render(request, "occ_survey/login.html", {"next": next})
		else:
			return render(request, "occ_survey/login.html", {})

	
@login_required
def user_logout(request):
	logout(request)
	request.session['redirect_logout'] = True
	return redirect('occ_survey:index')

@login_required
def dashboard(request, username):
	if request.user.username != username:
		return render(request, 'occ_survey/base.html', {"text": "You do not have access to this page!",})
	else:
		user = User.objects.get(username=username)
		user_profile = UserProfile.objects.get(user=user)
	
		return render(request, 'occ_survey/dashboard.html', {"user1": user, "user_profile": user_profile, })

@login_required
def chart_daily_consumption(request):
	user_profile = UserProfile.objects.get(user=request.user)
	room = user_profile.room.lower().replace(".", "_")
	today = datetime.date.today()
	day = today.day
	month = today.month
	year = today.year
	
	data = { 
		"consumption": [],
		"dates": [],
	}
	
	for i in range(0,7) :
		data["consumption"].append(len(LogLighting.objects.filter(time__year=year).filter(time__month=month).filter(time__day=day-i).filter(**{room: 1})))	
		if i == 0 :
			data["dates"].append("Today")
		else:
			data["dates"].append((today - datetime.timedelta(i)).strftime("%d-%b"))
	
	return HttpResponse(json.dumps(data))

def about(request):
	return render(request, 'occ_survey/about.html', {})		
		
		