from django.urls import path

from . import views

app_name = 'questans'

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('<int:pk>/', views.detail.as_view(), name='detail'),
    path('<int:pk>/results/', views.results.as_view(), name='results'),
    path('<int:question_id>/answer/', views.answer, name='answer'),
    path('save-upvote',views.save_upvote,name='save-upvote'),
    path('save-downvote',views.save_downvote,name='save-downvote'),
    path('displayaddquestion/', views.displayAddQuestion.as_view(), name='displayaddquestion'),
    path('addquestion/', views.addQuestion, name='addquestion'),
]