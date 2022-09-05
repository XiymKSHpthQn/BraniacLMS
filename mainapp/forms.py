from django import forms

from mainapp import models as mainapp_models


class CourseFeedbackForm(forms.ModelForm):
    def __init__(self, *args, course=None, user=None, **kwargs):
        ret = super().__init__(*args, **kwargs)
        if course and user:
            self.fields["course"].initial = course.pk
            self.fields["user"].initial = user.pk
        return ret

    class Meta:
        model = mainapp_models.CourseFeedback
        fields = ("course", "user", "feedback", "rating")
        widgets = {
            "course": forms.HiddenInput(),
            "user": forms.HiddenInput(),
            "rating": forms.RadioSelect(),
        }
