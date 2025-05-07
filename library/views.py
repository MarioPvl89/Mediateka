from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MediaItem
from .forms import MediaItemForm


def media_list(request):
    return render(request, 'library/media_list.html')

@login_required
def media_list(request):
    # items = MediaItem.objects.filter(user=request.user).order_by('-added_at')
    # return render(request, 'library/media_list.html', {'items': items})
    media_items = MediaItem.objects.filter(user=request.user)

    media_type = request.GET.get('type')
    if media_type in dict(MediaItem.MEDIA_TYPES).keys():
        media_items = media_items.filter(media_type=media_type)

    sort = request.GET.get('sort')
    if sort == 'title':
        media_items = media_items.order_by('title')
    elif sort == 'progress':
        # Сортировка по прогрессу — вручную
        media_items = sorted(media_items, key=lambda item: item.progress_percent(), reverse=True)
    else:
        media_items = media_items.order_by('-added_at')  # по умолчанию

    return render(request, 'library/media_list.html', {
        'media_items': media_items,
        'media_type': media_type,
        'sort': sort,
    })

@login_required
def add_media_item(request):
    if request.method == 'POST':
        form = MediaItemForm(request.POST, request.FILES)
        if form.is_valid():
            media_item = form.save(commit=False)
            media_item.user = request.user
            media_item.save()
            return redirect('media-list')
    else:
        form = MediaItemForm()
    return render(request, 'library/add_media.html', {'form': form})

@login_required
def edit_media_item(request, pk):
    item = get_object_or_404(MediaItem, pk=pk, user=request.user)
    if request.method == 'POST':
        form = MediaItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('media-list')
    else:
        form = MediaItemForm(instance=item)
    return render(request, 'library/edit_media.html', {'form': form, 'item': item})


@login_required
def delete_media_item(request, pk):
    item = get_object_or_404(MediaItem, pk=pk, user=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('media-list')
    return render(request, 'library/delete_media.html', {'item': item})
