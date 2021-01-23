from django.urls import path

from . import views

app_name = 'questans'

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('<int:pk>/', views.detail.as_view(), name='detail'),
    path('<int:pk>/results/', views.results.as_view(), name='results'),
    path('<int:question_id>/answer/', views.answer, name='answer'),
    path('voteup/', views.voteup, name='voteup'),
    path('votedown/', views.votedown, name='votedown'),
    path('displayaddquestion/', views.displayAddQuestion.as_view(), name='displayaddquestion'),
    path('addquestion/', views.addQuestion, name='addquestion'),
]