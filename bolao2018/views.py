from django.shortcuts import render, get_object_or_404
from .models import Time
from django.http import Http404

def times(request):

  time_exemplo = get_object_or_404(Time, sigla=”AAA”)
  times = Time.objects.all()
  contexto = {'times': times}
  return render(request, 'times.html', contexto)