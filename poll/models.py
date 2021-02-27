from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


TYPE = [
    ('text', 'Ответ текстом'),
    ('single', 'Ответ с выбором одного варианта'),
    ('multiple', 'Ответ с выбором нескольких вариантов')
]


class Question(models.Model):
    """
    Модель вопроса. Поле тип принимает одно из трёх значений.
    Если это 'text', то никакие варианты ответа к модели не прикрепляются.
    Если 'single' или 'multiple', то к модели через ForeignKey прикрепляем варианты ответа (Choice).
    """
    title = models.CharField(max_length=250)
    type = models.CharField(choices=TYPE, max_length=8)
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.title


class Poll(models.Model):
    """Модель опроса"""
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Choice(models.Model):
    """Модель варианта ответа в вопросах (Question) с типом 'single' или 'multiple'"""
    text = models.CharField(max_length=250)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        return self.text


class Answer(models.Model):
    """Модель ответа на вопрос"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    started_poll = models.ForeignKey('StartedPoll', on_delete=models.CASCADE, related_name='answers')
    choice = models.ManyToManyField(Choice, blank=True)
    choice_text = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.question) + str(self.choice)


class StartedPoll(models.Model):
    """Модель процесса прохождения опроса"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.poll)
