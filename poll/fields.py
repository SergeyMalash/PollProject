from rest_framework.relations import RelatedField
from poll.models import Question, Choice
from django.utils.translation import gettext_lazy as _


class QuestionRelatedField(RelatedField):
    default_error_messages = {
        'question not found': 'There is no such question in the poll you are taking',
        'incorrect_type': _('Incorrect type. Expected pk value, received {data_type}.'),
    }

    def to_internal_value(self, data):
        try:
            return self.queryset.get(pk=data)
        except Question.DoesNotExist:
            self.fail('question not found')
        except (TypeError, ValueError):
            self.fail('incorrect_type', data_type=type(data).__name__)

    def to_representation(self, value):
        from poll.serializers import QuestionSerializer
        question_data = QuestionSerializer(value)
        return question_data.data


class ChoiceRelatedField(RelatedField):
    default_error_messages = {
        'choice not found': 'There is no such choice in the question you are answering',
        'incorrect_type': _('Incorrect type. Expected pk value, received {data_type}.'),
    }

    def to_internal_value(self, data):
        try:
            return self.queryset.get(pk=data)
        except Choice.DoesNotExist:
            self.fail('choice not found')
        except (TypeError, ValueError):
            self.fail('incorrect_type', data_type=type(data).__name__)

    def to_representation(self, value):
        from poll.serializers import ChoiceSerializer
        choice_data = ChoiceSerializer(value)
        return choice_data.data
