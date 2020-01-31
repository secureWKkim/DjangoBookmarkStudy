#from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Bookmark


# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
    # 게시판의 페이징 기능(필수). 완전 간단하게 구현 가능! 한 페이지에 몇개씩 출력할지 결정하는 값.
    paginate_by = 6


class BookmarkCreateView(CreateView):
    # 어떤 모델의 입력을 받을 것인지 결정하는 부분
    model = Bookmark
    # 어떤 필드들을 입력받을 것인지 설정하는 부분
    fields = ['site_name','url']
    # 글쓰기를 완료하고 이동할 페이
    success_url = reverse_lazy('list')
    # 사용할 템플릿의 접미사만 변경하는 설정값
    """기본으로 설정되어 있는 템플릿 이름들은 모델명_xxx 형태다.
    CreateView, UpdateView 는 form 이 접미사인데
    이걸 변경해서 bookmark_create 란 이름의 템플릿 파일을 사용하도록 설정한 것."""
    template_name_suffix = '_create'


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    # 목록 페이지로 가도록 한다.
    success_url = reverse_lazy('list')