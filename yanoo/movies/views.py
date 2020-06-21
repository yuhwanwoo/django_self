from django.shortcuts import render,redirect
from movies.models import Movie

# Create your views here.
def index(request):
    # 전체 데이터 가져오기
    # 그 데이터 템플릿에게 넘겨주기
    # 템플릿에서 반복문으로 각각의 게시글 pk, title 보여주기
    movie=Movie.objects.all()
    context={
        'movies': movie
    }
    return render(request,"movies/index.html", context)

def new(request):
    return render(request,'movies/new.html')

def create(request):
    title=request.POST.get('title')
    text=request.POST.get('text')
    Movie.objects.create(title=title,content=text)
    return redirect('movies:index')

def introduce(request):
    return render(request)

def detail(request, movies_pk):
    movie=Movie.objects.get(pk=movies_pk)
    context={
        'movie':movie
    }
    return render(request, 'movies/detail.html',context)

# views.py
# 1. 특정 글 삭제를 위한 경로 작성
# 1.1 /movies/delete/
# 2. 글 삭제 처리를 해주는 view 작성
# 3. 글 삭제 후, index page로 redirect
# 4. 글 삭제를 위한 링크 detail에 작성
def delete(request, movies_pk):
    movie=Movie.objects.get(pk=movies_pk)
    movie.delete()
    return redirect('movies:index')

# 1. 특정 글 수정을 위한 경로 생성
# 1-1. /movies/1/edit
# 2. 글 수정 template를 render하는 edit view 작성
# 2-1. 해당 templateㄹ에 form tag 생성
# 2-2. 각 input tag 내부에 기존 내용이 들어있어야 함.
# 3. edit 보낸 데이터 처리를 위한 경로 생성
# 3-1. /movies/1/update
# 4. 글 수정 처리를 하는 update view 작성
# 5. 해당 글 상세 페이지로 redirect
# 6. 글 수정을 위한 edit 링크 해당 글 상세 페이지에 생성
# 6-1. {% url 'movies:edit' movie.pk %}
def edit(request, movies_pk):
    movie=Movie.objects.get(pk=movies_pk)
    context={
        'movie':movie
    }
    return render(request, 'movies/edit.html', context)

def update(request, movies_pk):
    edit_title=request.POST.get('edit_title')
    edit_content=request.POST.get('edit_content')
    movie=Movie.objects.get(pk=movies_pk)
    movie.title=edit_title
    movie.content=edit_content
    movie.save()
    return redirect('movies:detail',movies_pk)
