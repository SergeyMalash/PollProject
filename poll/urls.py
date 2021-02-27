from django.urls import path
from poll import views


urlpatterns = [
    path('polls/', views.AllPollsView.as_view()),
    path('polls/active/', views.ActivePollsView.as_view()),
    path('polls/<pk>/', views.PollView.as_view()),
    path('polls/<pk>/questions/', views.PollQuestionsView.as_view()),
    path('questions/', views.AllQuestionView.as_view()),
    path('questions/<pk>/', views.QuestionView.as_view()),
    path('choices/', views.AllChoiceView.as_view()),
    path('choices/<pk>/', views.ChoiceView.as_view()),
    path('answers/', views.AllAnswerView.as_view()),
    path('answers/<pk>/', views.AnswerView.as_view()),
    path('start_poll/', views.StartPollView.as_view()),
    path('started_polls/<user>/', views.StartedPollsView.as_view()),
    path('started_polls/<user>/<pk>/', views.StartedPollView.as_view()),
]
