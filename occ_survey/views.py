from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import json
from .mail.exp_mail import *
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
	return render(request, 'occ_survey/base.html', {"text": "Thank you for submitting!", "homelink": True, })
	
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
					return HttpResponseRedirect(reverse("index"))
			
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
	return redirect('index')

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
	
	if "room" in request.GET: #if room exists in GET
		if request.GET["room"]: #if room is not empty
			room = request.GET["room"]

	
	#for debug test other rooms
	#room = "g32_2"
	today = datetime.date.today()
	
	data = { 
		"consumption": [],
		"dates": [],
	}
	
	#number of past days to show: default = 7
	for i in range(0,7) :
		lighting_list = LogLighting.objects.filter(time__gte= (today-datetime.timedelta(i)))
		lighting_list = lighting_list.filter(time__lt= (today-datetime.timedelta(i-1)))
		lighting_list = lighting_list.filter(**{room: 1})
		consumption = round(len(lighting_list)/60.0, 2)
		data["consumption"].append(consumption)
		if i == 0 :
			data["dates"].append("Today")
		else:
			data["dates"].append((today - datetime.timedelta(i)).strftime("%d-%b"))
	
	return HttpResponse(json.dumps(data))

#view to explain the experiment
def about(request):
	return render(request, 'occ_survey/about.html', {})

#view to explain how the buttons function	
def buttons(request):
	return render(request, 'occ_survey/buttons.html', {})

def mail(request):
	user_list = UserProfile.objects.filter(profile_isDone=0)
	text = []
	for each in user_list:
		reminderMail(each.user)
		text.append(each.user.email)
	return HttpResponse(json.dumps(text))

#view to extract live status from db, needs to pass GET with room
def get_status(request):
	if request.GET:
		room = request.GET["room"].lower().replace(".", "_")
		room2 = request.GET["room"]
	else:
		user_profile = UserProfile.objects.get(user=request.user)
		room = user_profile.room.lower().replace(".", "_")
		room2 = user_profile.room
	
	time = LogLighting.objects.values_list("time", flat=True).order_by('-id')[:1][0]
	lights = LogLighting.objects.values_list(room, flat=True).order_by('-id')[:1][0]
	lux = LogLux.objects.values_list(room, flat=True).order_by('-id')[:1][0]
	
	td = ControlTd1.objects.values_list(room, flat=True).order_by('-id')[:1][0]
	lux_th = ControlLuxThreshold.objects.values_list(room, flat=True).order_by('-id')[:1][0]
	upp_th = ControlLuxUpperThreshold.objects.values_list(room, flat=True).order_by('-id')[:1][0]
	
	data = {
		"ok": True,
		"res": {
			"room": room2,
			"time": time.strftime("%c"),
			"lights": lights,
			"lux": lux,
		},
		"res2": {
			"td": td,
			"lux_th": lux_th,
			"upp_th": upp_th,
		},
	}
	return HttpResponse(json.dumps(data, sort_keys=True))

def remote(request):
	if request.method == "GET":
		if "switch" in request.GET:
			user_profile = UserProfile.objects.get(user=request.user)
			user_profile.remote_switch_count += 1
			user_profile.save()
			return HttpResponse("switched from remote")
		
		return HttpResponse("no changes")
		
	elif request.method =="POST":
		return HttpResponse("change settings")





		
		