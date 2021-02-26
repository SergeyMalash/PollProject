from rest_framework import serializers
from poll.fields import QuestionRelatedField, ChoiceRelatedField
from poll.models import Poll, Answer, Question, Choice, StartedPoll


class ChoiceSerializer(serializers.ModelSerializer):
    """Сериализатор конкретного варианта ответа"""

    class Meta:
        model = Choice
        fields = '__all__'

    def validate_question(self, value):
        if value.type == 'text':
            raise serializers.ValidationError("Choices cannot be specified in a question type with text")
        return value


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'poll', 'title', 'type', 'choices', ]


class PollSerializer(serializers.ModelSerializer):
    """Сериализатор опроса"""

    class Meta:
        model = Poll
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    """Сериализатор ответа на вопрос"""
    question = QuestionRelatedField(queryset=Question.objects.all())
    choice = ChoiceRelatedField(queryset=Choice.objects.all(), many=True, required=False)

    class Meta:
        model = Answer
        fields = ('id', 'user', 'started_poll', 'question', 'choice', 'choice_text')
        read_only_fields = ('id', 'user')

    def validate(self, attrs):
        if attrs['question'] not in attrs['started_poll'].poll.questions.all():
            raise serializers.ValidationError("there is no such question in the selected poll")
        if attrs['question'].type == 'text':
            attrs.pop('choice', None)
        if attrs['question'].type != 'text':
            attrs.pop('choice_text', None)
            if 'choice' not in attrs or attrs['choice'] == []:
                raise serializers.ValidationError("Specify choice")
            for choice in attrs['choice']:
                if choice not in attrs['question'].choices.all():
                    raise serializers.ValidationError("There is no such choice in the question you are answering")
        if Answer.objects.filter(started_poll=attrs['started_poll'], question=attrs['question']).exists():
            raise serializers.ValidationError("You have already answered the question")
        return attrs


class QuestionWithAnswerSerializer(serializers.ModelSerializer):
    """
    Сериализатор вопроса и ответа на него.
    """
    question = serializers.CharField(source='question.title')
    choice = serializers.StringRelatedField(many=True, )
    choice_text = serializers.CharField()

    class Meta:
        model = Answer
        fields = ['question', 'choice', 'choice_text']


class StartedPollsSerializer(serializers.ModelSerializer):
    """
    Сериализатор опросов, вопросов и ответов. Выводит информацию только по одному пользователю, id которого указан в
    запросе
    """
    poll = PollSerializer()
    answers = QuestionWithAnswerSerializer(many=True)

    class Meta:
        model = StartedPoll
        fields = ('id', 'poll', 'answers')


class StartPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartedPoll
        fields = ('id', 'poll', 'user')
        extra_kwargs = {'user': {'read_only': True}}
