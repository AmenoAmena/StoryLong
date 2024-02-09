from django.shortcuts import render,redirect
from .models import story

# Create your views here.
def index(request):
    return render(request, 'LongStoryApp/index.html')

def story_show(request):
    story_model = story.objects.all()
    return render(request, 'LongStoryApp/story.html',{
        'context':story_model
    })  

def contribute(request):
    if request.method == 'POST':
        user_story= request.POST.get('story')
        story.objects.create(story_shown=user_story)
        return redirect('story')
        
    return render(request, 'LongStoryApp/contribute.html')