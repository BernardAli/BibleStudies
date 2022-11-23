from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Title, Entry
from .forms import TopicForm, EntryForm

# Create your views here.


def index_page(request):
    title = "Bible Studies"

    context = {
        'title': title
    }
    return render(request, "index.html", context=context)


@login_required
def topics(request):
    titles = Title.objects.filter(owner=request.user).order_by('date_added')
    context = {
        'titles': titles
    }
    return render(request, 'logs/titles.html', context)


@login_required
def topic(request, title_id):
    title = Title.objects.get(id=title_id)
    if title.owner != request.user:
        raise Http404
    entries = title.entry_set.order_by('date_added')
    context = {
        'title': title,
        'entries': entries
    }
    return render(request, 'logs/title.html', context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()
            form.save()
            return redirect('logs:topics')
    context = {
        'form': form
    }
    return render(request, 'logs/new_topic.html', context)


@login_required
def new_entry(request, title_id):
    """Add a new entry for a particular topic."""
    title = Title.objects.get(id=title_id)
    if title.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.title = title
            new_topic.save()
            return redirect('logs:topic', title_id=title_id)

    # Display a blank or invalid form.
    context = {'title': title, 'form': form}
    return render(request, 'logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    title = entry.title

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('logs:topic', title_id=title.id)

    context = {'entry': entry, 'title': title, 'form': form}
    return render(request, 'logs/edit_entry.html', context)