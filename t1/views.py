from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from t1.models import Character


class CharacterListView(ListView):
    model = Character
    # character_list = Character.object.all() #DB에 모델 데이터 다 가져오자
    # return render(request 't1/character_list.html', context={'character_list' : character_list})
    # #모델_list.html에 모델_list라는 키로 DB에서 가져온 데이터 넣어서 render한다.

class CharacterDetailView(DetailView):
    model = Character
    # character = Character.object.get(pk=pk)
    # return render(request, 't1/character_detail.html', context={'character' : character})

class CharacterCreateView(CreateView):
    model = Character
    fields = ['name', 'feature']        #'__all__'
    template_name_suffix = '_create'    #character_form.html -> character_create.html
    success_url = reverse_lazy('t1:character_list')     #만들기 성공할 때 이동할 url

class CharacterUpdateView(UpdateView):
    model = Character
    fields = '__all__' #['name', 'feature']
    template_name_suffix = '_update'    #character_form.html -> character_update.html
    success_url = reverse_lazy('t1:character_list')     #수정 성공할 때 이동할 URL