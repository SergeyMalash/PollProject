from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from poll.models import Poll, Answer, Question, Choice, StartedPoll
from poll.permisions import IsAdminOrReadOnly
from poll.serializers import PollSerializer, AnswerSerializer, QuestionSerializer, \
    StartedPollsSerializer, ChoiceSerializer, StartPollSerializer


class AllPollsView(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAdminOrReadOnly]


class ActivePollsView(generics.ListAPIView):
    queryset = Poll.objects.filter(finished_at__exact=None)
    serializer_class = PollSerializer
    permission_classes = [IsAdminOrReadOnly]


class PollView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [IsAdminOrReadOnly]


class PollQuestionsView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.filter(poll=self.kwargs['pk'])


class AllQuestionView(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAdminUser]


class QuestionView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class AllChoiceView(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
    permission_classes = [IsAdminUser]


class ChoiceView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class AllAnswerView(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def perform_create(self, serializer):
        if self.request.user and self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()


class AnswerView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Answer.objects.all()


class StartedPollsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StartedPollsSerializer

    def get_queryset(self):
        return StartedPoll.objects.filter(user__pk=self.kwargs['user'])


class StartedPollView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StartedPollsSerializer

    def get_queryset(self):
        return StartedPoll.objects.filter(user__pk=self.kwargs['user'])


class StartPollView(generics.CreateAPIView):
    serializer_class = StartPollSerializer

    def perform_create(self, serializer):
        if self.request.user and self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()
