from django.conf.urls import url
from django.urls import path
from poll import views

from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
#
# schema_view = get_schema_view(
#    openapi.Info(
#       title="Polls API",
#       default_version='v1',
#       description="Тестовый API для проведения опросов",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="s.mallash.dev@gmail.com"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )


urlpatterns = [
    # url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
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
    # path('my_polls/<pk>', views.CompletedPollsView.as_view()),
    # path('get_anon_user_token/', custom_obtain_token.TokenObtainPairView.as_view())
]
