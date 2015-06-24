from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Choice(models.Model):
	TYPE_CHOICES = (
		("radio", "radio"),
		("choice", "choice"),
		("open", "open-ended-text"),
	)
	
	name = models.CharField(max_length=30, null=False, unique=True)
	type = models.CharField(max_length=10, choices=TYPE_CHOICES)
	choice1 = models.CharField(max_length=30, null=True)
	choice2 = models.CharField(max_length=30, null=True)
	choice3 = models.CharField(max_length=30, null=True)
	choice4 = models.CharField(max_length=30, null=True)
	choice5 = models.CharField(max_length=30, null=True)
	
	def __unicode__(self):
		return self.name
	

class Question(models.Model):
	
	choice = models.ForeignKey(Choice, null=True, blank=True)
	date_updated = models.DateTimeField(auto_now=True)
	question_text = models.CharField(max_length=255)
	question_cat = models.CharField(max_length=255)
	choice_name = models.CharField(max_length=30, null=True, blank=True)
	order = models.IntegerField(default = 0)
	
	def save(self, *args, **kwargs):
		self.choice_name = self.choice.name
		super(Question, self).save(*args, **kwargs)
		
	def __unicode__(self):
		return self.question_text
		
class Answer(models.Model):
	question = models.ForeignKey(Question)
	username = models.CharField(max_length=255)
	answer = models.IntegerField(null=True, blank=True)
	answer_text = models.TextField(blank=True)
	in_date = models.DateTimeField('date submitted', default=datetime.datetime.now)
	
	def __unicode__(self):
		string = self.username + " answered " + str(self.answer) + " for question: " + str(self.question.id)
		return string

class AdminText(models.Model):
	index = models.TextField(blank=True)
	update1 = models.TextField(blank=True)
	update2 = models.TextField(blank=True)
	update3 = models.TextField(blank=True)
	profile = models.TextField(blank=True)
	comfort = models.TextField(blank=True)
	control = models.TextField(blank=True)

	
			
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	
	username = models.CharField(max_length=20, blank=True)
	room = models.CharField(max_length=10)
	profile_isDone = models.IntegerField(default=0)
	comfort_isDone = models.IntegerField(default=0)
	control_isDone = models.IntegerField(default=0)
	impromptu_count = models.IntegerField(default=0)
	
	remote_use_count = models.IntegerField(default=0)
	
	def save(self, *args, **kwargs):
		self.username = self.user.username
		super(UserProfile, self).save(*args, **kwargs)
                
	def __unicode__(self):
		return self.user.username
		

class LogLux(models.Model):
    time = models.DateTimeField()
    g22 = models.IntegerField(db_column='G22', blank=True, null=True)  # Field name made lowercase.
    g23 = models.IntegerField(db_column='G23', blank=True, null=True)  # Field name made lowercase.
    rpi_0 = models.IntegerField(db_column='RPi_0', blank=True, null=True)  # Field name made lowercase.
    g24 = models.IntegerField(db_column='G24', blank=True, null=True)  # Field name made lowercase.
    g25_1 = models.IntegerField(db_column='G25.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g25_2 = models.IntegerField(db_column='G25.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_1 = models.IntegerField(db_column='G26.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_2 = models.IntegerField(db_column='G26.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g27 = models.IntegerField(db_column='G27', blank=True, null=True)  # Field name made lowercase.
    g31_1 = models.IntegerField(db_column='G31.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g31_2 = models.IntegerField(db_column='G31.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'log_lux'

class LogLighting(models.Model):
    time = models.DateTimeField()
    g22 = models.IntegerField(db_column='G22', blank=True, null=True)  # Field name made lowercase.
    g23 = models.IntegerField(db_column='G23', blank=True, null=True)  # Field name made lowercase.
    rpi_0 = models.IntegerField(db_column='RPi_0', blank=True, null=True)  # Field name made lowercase.
    g24 = models.IntegerField(db_column='G24', blank=True, null=True)  # Field name made lowercase.
    g25_1 = models.IntegerField(db_column='G25.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g25_2 = models.IntegerField(db_column='G25.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_1 = models.IntegerField(db_column='G26.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g26_2 = models.IntegerField(db_column='G26.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g27w = models.IntegerField(db_column='G27W', blank=True, null=True)  # Field name made lowercase.
    g27f = models.IntegerField(db_column='G27F', blank=True, null=True)  # Field name made lowercase.
    g31_1 = models.IntegerField(db_column='G31.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    g31_2 = models.IntegerField(db_column='G31.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'log_lighting'