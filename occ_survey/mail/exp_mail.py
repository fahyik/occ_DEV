from django.core.mail import EmailMessage

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
	
You will also be able to find more details on the experiment on the same web page.

Once again, I will be happy to answer any queries you may have with regards to the experiment.
Thank you.
	
Regards,
Fah Yik
""" % (user.first_name, user.username, user.username)

	email = EmailMessage('Lighting Control Experiment | Reminder | Phase 1', message, 
				'Adaptive System Labs <asl@ethz.ch>', [],
				['adaptive.systems.lab.ethz@gmail.com', ],
				reply_to=['adaptive.systems.lab.ethz@gmail.com'])
	email.send()
	
	print "send to: "+user.email+" completed!"