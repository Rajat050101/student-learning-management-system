from django import forms
from .models import Lesson,Comment,Reply

class LessonForm(forms.ModelForm):
    class Meta:
        model=Lesson
        fields=('lesson_id','name','position','video','Notes','ppt')

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('body',)
        labels={"body":"Comment:"}
        widgets={
            'body':forms.Textarea(attrs={'class':'form-control','rows':5,'cols':70,'placeholder':"Leave your comment here"}),
        }
    
   

class ReplyForm(forms.ModelForm):
    class Meta:
        model=Reply
        fields=('reply_body',)
        widggets={
            'reply_body':forms.Textarea(attrs={'class':'form-control','rows':2,'cols':20})
        }
