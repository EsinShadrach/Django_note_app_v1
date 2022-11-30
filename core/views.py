from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Note, Tag

# Create your views here.


def homepage(request):
    q = request.GET.get('search') if request.GET.get('search') != None else ''
    page_identity = 'home'

    if (q.lower() == 'all'):
        notes = Note.objects.all()

    else:
        notes = Note.objects.filter(
            Q(name__icontains=q) |
            Q(tag__tag1__icontains=q) |
            Q(tag__tag2__icontains=q) |
            Q(tag__tag3__icontains=q)
        )

    context = {
        'notes': notes,
        'identity': page_identity,
    }
    return render(request, 'index.html', context)


def detailed(request, pk):
    page_identity = 'detailed'
    detailed_note = Note.objects.get(unique_identity=pk)

    if request.method == "POST":
        detailed_note.delete()
        return redirect('home')

    context = {
        'detailed': detailed_note,
        'identity': page_identity,
    }
    return render(request, 'detailed.html', context)

def create(request):
    page_identity = 'create'
    if request.method == "POST":
        note_name = request.POST["note_name"]
        tag_1 = request.POST["tag1"]
        tag_2 = request.POST["tag2"]
        tag_3 = request.POST["tag3"]
        note_content = request.POST["note_content"]

        if (note_name != '' and note_content != ''):
            note = Note.objects.create(
                name=note_name,
                note=note_content,
                # tag=note_name
            )
            # tag = Tag.objects.create(
            #     tag1=f'{tag_1}',
            #     tag2= f'{tag_2}',
            #     tag3=f'{tag_3}',
            # )
            # tag = note_name
            return redirect('home')

        elif note_name == '':
            err = True
            err1 = True
            message = 'name appears to be empty, try filling that up'
            context = {
                'error': err,
                'error_1': err1,
                'error_message': message,
                'identity': page_identity
            }
            return render(request, 'create.html', context)

        elif note_content == '':
            err = True
            err1 = False
            message = 'note appears to be empty, try filling that up'
            context = {
                'error': err,
                'error_message': message,
                'error_1': err1,
                'identity': page_identity,
            }
            return render(request, 'create.html', context)

    context = {
        'identity': page_identity
    }
    return render(request, 'create.html', context)
