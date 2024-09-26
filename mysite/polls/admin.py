from django.contrib import admin
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]

    list_display = ("question_text", "pub_date")

class ChoiceAdmin(admin.ModelAdmin):
    #fieldsets are for post forms
    fieldsets = [
        ("Question", {"fields": ["question"]}),
        ("Choice", {"fields": ["choice_text"]}),
        ("Vote", {"fields": ["votes"]})
    ]

    #list_display is for get requesta
    list_display = ("question", "choice_text", "votes")

# Register your models here.
#admin.site.register(Question) Default UI provided by django below QuestionAdmin is customized Question

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice,  ChoiceAdmin)
