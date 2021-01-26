from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from .models import Answer, Question
from django.urls import reverse
from questans import models
from django.views import generic
from django.utils import timezone
from django.db.models import Q
#from taggit.models import Tag

class index(generic.ListView):
    template_name = 'questans/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self): #most recent 5 que view 
        return Question.objects.filter(
            pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class detail(generic.DetailView):
    model = Question
    template_name = 'questans/detail.html'    
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


def save_upvote(request):
    if request.method =='POST':
        questionid=request.POST['questionid']
        question=Question.objects.get(pk=questionid)
        check=UpVote.objects.filter(question=question).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            UpVote.objects.create(
                question=question)
            return JsonResponse({'bool':True})

def save_downvote(request):
    if request.method =='POST':
        questionid=request.POST['questionid']
        question=Question.objects.get(pk=questionid)
        check=DownVote.objects.filter(question=question).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            DownVote.objects.create(
                question=question)
            return JsonResponse({'bool':True}) 


def answer(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        answer_text = request.POST.get('answertext')
        if answer_text: 
            answer = models.Answer.objects.create(question_id=question.pk, 
                                                  answer_text=request.POST.get('answertext'))
            answer.save()
    except (KeyError, Answer.DoesNotExist):
        return HttpResponseRedirect(reverse('questans:index'))
    return HttpResponseRedirect(reverse('questans:results', args=(question.id,)))

class results(generic.DetailView): #after adding ans successfully
    model = Question
    template_name = 'questans/results.html'

class displayAddQuestion(generic.ListView):
    model = Question
    template_name = 'questans/displayAddQuestion.html'

def addQuestion(request):
    question_name=request.POST.get('questionname')
    question_text=request.POST.get('questiontext')
    question = models.Question.objects.create(question_name=question_name,
                                              question_text=question_text,
                                              pub_date=timezone.now(),
                                              votes=0)
    question.save()
    return HttpResponseRedirect(reverse('questans:index'))