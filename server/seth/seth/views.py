from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.contrib.auth.models import User
from cropalert.models import UserProfile
from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home/index.html', context_instance=RequestContext(request))


class UserForm(ModelForm):
    class Meta:
        model = User

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']

def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        upf = UserProfileForm(request.POST, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return HttpResponseRedirect("/")
    else:
        uf = UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
    return render_to_response('register/register.html',
                                               dict(userform=uf,
                                                    userprofileform=upf),
                                               context_instance=RequestContext(request))