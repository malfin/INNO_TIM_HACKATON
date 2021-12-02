from django import forms

from mainapp.models import Startup


class StartupForm(forms.ModelForm):
    class Meta:
        model = Startup
        fields = (
            '__all__'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control mt-2'
            item.widget.attrs['style'] = 'resize: none'
            item.help_text = ''
