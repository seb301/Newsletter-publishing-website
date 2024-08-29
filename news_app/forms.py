from django import forms
from .models import Submission



class PostForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[f"name"].label='Name'
        self.fields[f"name"].widget.attrs.update({"class": "form-control mt-1 mb-3",'placeholder':'Enter Name'})
        self.fields[f"email"].label='Email:'
        self.fields[f"email"].widget.attrs.update({"class": "form-control mt-1 mb-3",'placeholder':'Enter Email'})
        self.fields[f"category"].label='Category'
        self.fields[f"category"].widget.attrs.update({"class": "form-control mt-1 mb-3",'placeholder':'Enter Category'})
        self.fields[f"postTitle"].label='Title'
        self.fields[f"postTitle"].widget.attrs.update({"class": "form-control mt-1 mb-3",'placeholder':'Enter Title'})
        self.fields[f"postDetails"].label='Details'
        self.fields[f"postDetails"].widget.attrs.update({"class": "form-control mt-1 mb-3",'placeholder':'Enter Details'})
        self.fields[f"postingDate"].label='Date'
        self.fields[f"postingDate"].widget.attrs.update({"class": "form-control-sm mt-1 mb-3",'placeholder':'Enter Date','type':'date'})
        self.fields[f"postImage"].label='Choose Image'
        self.fields[f"postImage"].widget.attrs.update({"class": "form-control mt-1 mb-3",'type':'image'})


#use summernote API for postDetails

# <label for="formFileMultiple" class="form-label">Multiple files input example</label>
#   <input class="form-control" type="file" id="formFileMultiple" multiple>



























# class PostForm(forms.ModelForm):

    # name=forms.CharField(label='Enter name here:',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}))

    # class Meta:
    #     model = Submission
    #     fields="__all__"

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for i in self.fields:
    #         self.fields[f'{i}'].widget.attrs.update({"class": "form-control",'placeholder':f'Enter {i}'})        
    #         print(i)



#https://www.youtube.com/watch?v=quJzUzCs6Q0

# add css styling to modelForms method1: https://www.youtube.com/watch?v=uJp4PaDkux0
# widgets={'(field_name)' : forms.TextInput(attrs={'class':'form-control'})}

# add css styling to modelForms method2: https://www.youtube.com/watch?v=ynToND_xOAM 
# pip install django-widget-tweaks, INSTALLED_APPS+='widget-tweaks'
# docs:https://pypi.org/project/django-widget-tweaks/