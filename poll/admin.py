from django.contrib import admin

from poll.models import Poll, Question, Choice, Answer, StartedPoll


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(StartedPoll)
class StartedPollAdmin(admin.ModelAdmin):
    pass
