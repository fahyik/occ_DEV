from django.contrib import admin
from .models import *

class AnswerAdmin(admin.ModelAdmin):
	list_display = ("in_date", "username", "answer", "question")

class QuestionAdmin(admin.ModelAdmin):
	list_display = ("order", "question_text", "question_cat")

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ("username", "room", "profile_isDone", "comfort_isDone", "control_isDone")

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Choice)
admin.site.register(AdminText)