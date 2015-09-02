from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import json, datetime
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
	room2 = user_profile.room
	room = user_profile.room.lower().replace(".", "_")
	
	if "room" in request.GET: #if room exists in GET
		if request.GET["room"]: #if room is not empty
			room = request.GET["room"] #room is already in small and _
			if request.GET["room"] == "rpi_0":
				room2 = "RPi_0"
			else:
				room2 = room.upper().replace("_", ".")

	
	#for debug test other rooms
	#room = "g32_2"
	today = datetime.date.today()
	
	data = {
		"occupancy": [],
		"consumption": [],
		"dates": [],
	}
	
	#number of past days to show: default = 7
	for i in range(0,7) :
		#lighting consumption:
		lighting_list = LogLighting.objects.filter(time__gte= (today-datetime.timedelta(i)))
		lighting_list = lighting_list.filter(time__lt= (today-datetime.timedelta(i-1)))
		lighting_list = lighting_list.filter(**{room: 1})
		consumption = round(len(lighting_list)/60.0, 2)
		data["consumption"].append(consumption)
		
		#occupancy:
		occupancy = []
		try:
			occupancy = LogOccupancy.objects.filter(room = room2).filter(time__gte= (today-datetime.timedelta(i))).filter(time__lt= (today-datetime.timedelta(i-1)))
		
		except:
			pass
		
		time = 0
		
		if occupancy:
			for j in range(0, len(occupancy)-1):
				if occupancy[j].state == 1 and occupancy[j+1].state == 0:
					time += (occupancy[j+1].time - occupancy[j].time).seconds	
					
			time = round( time/3600.0, 2)
		
		data["occupancy"].append(time)
		
		#dates:
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
	user_list = UserProfile.objects.filter(comfort_isDone=0)
	text = []
#	spotMail(user_list[0].user)
	for each in user_list:
		phase2Mail(each.user)
		text.append(each.user.email)
	return HttpResponse(json.dumps(text))

#view to extract live status from db, needs to pass room name with GET
def get_status(request):
	if request.GET:
		room = request.GET["room"].lower().replace(".", "_")
		room2 = request.GET["room"]
	else:
		user_profile = UserProfile.objects.get(user=request.user)
		room = user_profile.room.lower().replace(".", "_")
		room2 = user_profile.room
	
	time = datetime.datetime.now()
	lights = LogLighting.objects.values_list(room, flat=True).order_by('-id')[:1][0]
	lux = LogLux.objects.values_list(room, flat=True).order_by('-id')[:1][0]
	
	setpoints = ControlSetPoints.objects.get(room=room2) 
	td = setpoints.td
	lux_th = setpoints.lux_th
	upp_th = setpoints.upp_th
	
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

# if request = GET, updates remote switch count, if = POST, updates control set points
def remote(request):
	if request.method == "GET":
		if "switch" in request.GET:
			user_profile = UserProfile.objects.get(user=request.user)
			user_profile.remote_switch_count += 1
			user_profile.save()
			return HttpResponse("switched from remote")
		
		return HttpResponse("no changes")
		
	elif request.method == "POST":
		#post the changes into control_changes and run sort control_adjustments
		err_msg = ""
		room = request.POST["room"]
		room2 = request.POST["room"].lower().replace(".", "_")
		td_new = int(request.POST["td_setting_new"])
		lux_th_new = int(request.POST["lux_th_new"])
		upp_th_new = int(request.POST["upp_th_new"])
		setpoints = ControlSetPoints.objects.get(room=room)
		luxWLights = ControlLuxWLights.objects.values_list(room2, flat=True).order_by('-id')[:1][0]
		
		#boundaries
		if upp_th_new > 1500:
			upp_th_new = 1500
		
		if lux_th_new > 500:
			lux_th_new = 500
		
		if lux_th_new < 0:
			lux_th_new = 0
		
		if td_new < 0:
			td_new = 1
		elif td_new > 15:
			td_new = 15
		
		#make sure new values respect the original difference which is luxWLights
		del_lux_th = lux_th_new - setpoints.lux_th
		del_upp_th = upp_th_new - setpoints.upp_th
		del_th = upp_th_new - lux_th_new
		
		#first check if del_th < luxWLights
		if (del_th < luxWLights):		
			#del_upp_th has to be larger or equal than del_lux_th
			if (del_upp_th < del_lux_th):
				#if delta upp th is smaller, then set delta upp th to delta lux th and change upp_th_new
				del_upp_th = del_lux_th
				upp_th_new = del_upp_th + setpoints.upp_th
				err_msg = "The difference between the your new min. illuminance threshold and max. illuminance threshold is too small. It has been automatically changed for you."
		
		
		#insert new changes object
		changes = ControlChanges(room=room)
		# new set points
		changes.lux_th_new = lux_th_new
		changes.upp_th_new = upp_th_new
		changes.td_new = td_new
		# current set points at time of change
		changes.lux_th = setpoints.lux_th
		changes.upp_th = setpoints.upp_th
		changes.td = setpoints.td
		changes.save()
		
		#update current setpoints
 		setpoints.td = td_new
 		setpoints.lux_th = lux_th_new
 		setpoints.upp_th = upp_th_new
 		setpoints.override = 1
 		setpoints.save()
 		
		#update adjustments
		adj = ControlAdjustments.objects.get(room=room)
		change_list = ControlChanges.objects.filter(room=room).filter(date__gte= today-datetime.timedelta(14))
		sum_lux = 0
		sum_upp = 0
		sum_td = 0
		size = len(change_list)
		for each in change_list:
			sum_lux += each.lux_th_new - each.lux_th
			sum_upp += each.upp_th_new - each.upp_th
			sum_td += each.td_new - each.td	
		# save adjustment as mean of all previous adjustments
		adj.lux_th = sum_lux / size
		adj.upp_th = sum_upp / size
		adj.td = sum_td / size
		adj.save()
		
		user_profile = UserProfile.objects.get(user=request.user)
		user_profile.remote_change_count += 1
		user_profile.save()
		
		postreturn = {
			"success": "success",
			"error": err_msg,
		}
		
		return HttpResponse(json.dumps(postreturn))
     	
#called together with control_adapt to update set points in control_set_points
def update_set_points(request):
	room_list = Structure.objects.values_list("room", flat=True)
	for room in room_list:
		#get current set points for each room
		setpoints = ControlSetPoints.objects.get(room=room)
		#only update set points if there is NO override
		if setpoints.override == 0:
			room = room.lower().replace(".", "_")
			td = ControlTd1.objects.values_list(room, flat=True).order_by('-id')[:1][0]
			lux_th = ControlLuxThreshold.objects.values_list(room, flat=True).order_by('-id')[:1][0]
			upp_th = ControlLuxUpperThreshold.objects.values_list(room, flat=True).order_by('-id')[:1][0]
			setpoints.td = td
			setpoints.lux_th = lux_th
			setpoints.upp_th = upp_th
			setpoints.save()
		elif setpoints.override == 1:
			#add to current set points the changes linearly
			adj = ControlAdjustments.objects.get(room=room)
			room = room.lower().replace(".", "_")
			setpoints.td = ControlTd1.objects.values_list(room, flat=True).order_by('-id')[:1][0]
			setpoints.lux_th = ControlLuxThreshold.objects.values_list(room, flat=True).order_by('-id')[:1][0]
			setpoints.upp_th = ControlLuxUpperThreshold.objects.values_list(room, flat=True).order_by('-id')[:1][0]
			lights_lux = setpoints.upp_th - setpoints.lux_th

			setpoints.lux_th += adj.lux_th
			if setpoints.lux_th < 0:
				setpoints.lux_th = 0

			setpoints.upp_th += adj.upp_th
			if setpoints.upp_th < lights_lux:
				setpoints.lux_th = lights_lux

			setpoints.td += adj.td
			if setpoints.td <= 0:
				setpoints.td = 0
			
			setpoints.save()
	
	return HttpResponse("update set points Successful")

def get_override_status(request):
	if request.method == "GET":
		room = request.GET["room"]
		setpoints = ControlSetPoints.objects.get(room=room)
		override = setpoints.override
	
		data = {
			"override": override,
		}
	
		return HttpResponse(json.dumps(data))
	# to disable override
	elif request.method == "POST":
		setpoints = ControlSetPoints.objects.get(room=request.POST["room"])
		setpoints.override = 0
		setpoints.save()
		update_set_points(request)
		
		return HttpResponse("disable")

		
		