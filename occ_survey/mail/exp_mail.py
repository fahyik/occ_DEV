from django.core.mail import EmailMessage, EmailMultiAlternatives

# def mail():
# 	email = EmailMessage('Lighting Control Experiment', 'Testing email', 'Adaptive System Labs',
#     [], ['yongf@ethz.ch', 'adaptive.systems.lab.ethz@gmail.com', ], reply_to=['adaptive.systems.lab.ethz@gmail.com'])
#     email.send()

def startMail(user):
	message = """Dear %s,
	
thank you for agreeing to participate in the lighting control experiment. 

The goal of the experiment is to find out whether an automatic lighting control system can lead to energy savings at zero or negative expense of occupants' comfort. As such, we would be sending out various questionnaires throughout the experiment to assess each individual's level of comfort. 

The experiment will be conducted in two, possibly three phases. You will be informed of the setting at the beginning of each phase. A questionnaire will be sent out at the end of each phase to determine your level of comfort during that particular phase. If the lighting control system was in operation during the phase, you will also be sent another questionnaire to evaluate the control system.

We kindly request that you fill them out promptly, and as accurately as possible. 
Do note that in order for us to derive meaningful results, all answers that you submit will be non-anonymous.

A web interface has been set up to facilitate this study. 
You will have to log into your account to submit the questionnaires. Your login credentials are as follows:
	
	Username: %s
	Password: %s
	
The first phase of the experiment has already begun. During this phase, there will be no lighting control in operation in your offices.

In the meantime, please fill out the first questionnaire regarding your personal preferences. This will allow us to profile all the participants. Please follow the link below to access the questionnaire:
http://asl-lighting-control.info/main/survey/survey/profile

Your "Dashboard" and an "About" page detailing the experiment and the lighting control system can also be found on the same link.

I will be happy to answer any queries you may have with regards to the experiment.
Thank you.
	
Regards,
Fah Yik
""" % (user.first_name, user.username, user.username)

	email = EmailMessage('Lighting Control Experiment | Start of Phase 1', message, 
				'Adaptive System Labs <asl@ethz.ch>', [],
				['adaptive.systems.lab.ethz@gmail.com', ],
				reply_to=['adaptive.systems.lab.ethz@gmail.com'])
	email.send()
	
	print "send to: "+user.email+" completed!"

def reminderMail(user):
	message = """Dear %s,
	
thank you again for agreeing to participate in the lighting control experiment. 
However, it seems that you have yet to complete the first questionnaire. Here's a reminder to fill it out on the link below:
http://asl-lighting-control.info/main/survey/survey/profile

If you have lost the previous email, here are your login credentials again, as follows:
	
	Username: %s
	Password: %s
	
You will also be able to find <strong>more details</strong> on the experiment on the same web page.

Once again, I will be happy to answer any queries you may have with regards to the experiment.
Thank you.
	
Regards,
Fah Yik
""" % (user.first_name, user.username, user.username)

	email = EmailMessage('Lighting Control Experiment | Reminder | Phase 1', message, 
				'Adaptive System Labs <asl@ethz.ch>', [],
				['adaptive.systems.lab.ethz@gmail.com', ],
				reply_to=['adaptive.systems.lab.ethz@gmail.com'])
	#email.content_subtype = "html"  # Main content is now text/html
	email.send()
	
	print "send to: "+user.email+" completed!"

def phase2Mail(user):
	message = """<p>Dear %s,</p>
	
<p>
the first phase of the experiment is now over. We are now starting with the second phase where we will introduce the control system.</p>

<p>
We kindly ask that you read this <a href="http://asl-lighting-control.info/main/buttons">link</a> so that you understand how to properly operate the light switch in your office. <strong>This is very important to the function of the control in your office.</strong>
</p>

<p>
In this phase of the experiment, you will also be provided a control interface on your personal dashboard, on which you can switch on/off the lights, change the control parameters and see the statistics of light use in your office. Before you attempt to make any changes to the control however, please <a href="http://asl-lighting-control.info/main/about/#about-control">familiarise yourself with the system</a>.<br/>
<strong>Please do not make any changes if you are not sure.</strong>
</p>

<p>
In the meantime, we would like to have you fill out the second questionnaire with regards to your comfort during the first phase. We remind you again that the answers for this questionnaire should be <strong>based only on your experiences during the timeframe of 22 June to 9 August 2015</strong>.<br />
You can click on the link below to proceed to the questionnaire:<br/>
<a href="http://asl-lighting-control.info/main/survey/survey/comfort">http://asl-lighting-control.info/main/survey/survey/comfort</a>
</p>

<p>If you have forgotten your password, here are your login credentials again, as follows:</p>
	
<p>	
Username: %s <br/>
Password: %s
</p>

<p>I am looking forward to obtaining some interesting results and sharing them with you!</p>
<p>Once again, I will be happy to answer any queries you may have with regards to the experiment.</p>
<p>Thank you.</p>
	
<p>
Regards,<br/>
Fah Yik
</p>
""" % (user.first_name, user.username, user.username)

	email = EmailMessage('Lighting Control Experiment | Reminder | Phase 2', message, 
				'Adaptive System Labs <asl@ethz.ch>', [user.email],
				['adaptive.systems.lab.ethz@gmail.com', ],
				reply_to=['adaptive.systems.lab.ethz@gmail.com'])
	email.content_subtype = "html"  # Main content is now text/html
	email.send()
	
	print "send to: "+user.email+" completed!"