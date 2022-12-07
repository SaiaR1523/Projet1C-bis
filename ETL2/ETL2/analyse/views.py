from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from django.http import HttpResponseRedirect

from .handle_uploaded_file import handle_uploaded_file

# Create your views here.
@login_required (login_url='login')
def db(request):
  return render(request, 'dashboard.html', {})

@login_required (login_url='login')
def importF (request):
      if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
      else:
          form = UploadFileForm()
      return render(request, 'import.html', {'form': form})