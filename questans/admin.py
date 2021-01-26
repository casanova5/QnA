from django.contrib import admin
from .models import Question, Answer, UpVote, DownVote

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin): #display and filtering of questions
    fieldsets = [
        (None,               {'fields': ['question_name']}),
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # add answers in an inline fashion 
    inlines = [AnswerInline]
    list_display = ('question_name', 'question_text', 'pub_date')
    # filter questions by date published 
    list_filter = ['pub_date']
admin.site.register(Question, QuestionAdmin)

class UpvoteAdmin(admin.ModelAdmin):
    list_display=('question',)
admin.site.register(UpVote,UpvoteAdmin)

class DownvoteAdmin(admin.ModelAdmin):
    list_display=('question',)
admin.site.register(DownVote,DownvoteAdmin)

    
# Add the ability to add questions and answers to the admin view 