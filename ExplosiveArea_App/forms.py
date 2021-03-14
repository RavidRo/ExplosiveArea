from django.utils.translation import gettext_lazy as _
from django.forms import CharField, ModelForm, Textarea, ImageField, FileField
from .models import Excercise

class ExcerciseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update(placeholder='משפט הסבר קצר.')

    class Meta:
        model = Excercise
        fields = '__all__'
        # exclude = ['section']
        labels = {
            'title': _('כותרת'),
            'intendedFor': _('מיועד ל'),
            'description': _('תיאור'),
            'instructions': _('הוראות'),
            'section': _('סוג'),
            'image': _('תמונה'),
            'video': _('סרטון'),
        }