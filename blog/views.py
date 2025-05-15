from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Q

from .forms import WordForm
from .models import Word


def post_list(request, pk=-1):
    query = request.GET.get('q')
    if query:
        words = Word.objects.filter(Q(word__icontains=query) | Q(description__icontains=query))
    else:
        words = Word.objects.all()

    if pk != -1:
        word = get_object_or_404(Word, pk=pk)
        return render(request, 'blog/blog.html', {'words': words, 'word': word, 'query': query})
    else:
        return render(request, 'blog/blog.html', {'words': words, 'word': -1, 'query': query})


def word_new(request):
    if request.method == "POST":
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            word.author = request.user
            word.published_date = timezone.now()
            word.save()
            return redirect('post_list')
    else:
        form = WordForm()
    return render(request, 'blog/word_edit.html', {'form': form})


def word_edit(request, pk):
    word = get_object_or_404(Word, pk=pk)
    if request.method == "POST":
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            word = form.save(commit=False)
            word.author = request.user
            word.published_date = timezone.now()
            word.save()
            return redirect('post_list')
    else:
        form = WordForm(instance=word)
    return render(request, 'blog/word_edit.html', {'form': form})