from django import forms
from.models import Question

class QuestForm(forms.ModelForm):
    class Meta:
        model=Question
        fields = ('title','question_text',)