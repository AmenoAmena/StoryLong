from django.shortcuts import render,redirect
from .models import story
from .utils import translate_text

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
        if user_story == "":
            return render(request, 'LongStoryApp/contribute.html',{
                'message': "Please write anything to contribute"
            })
        else:
            translated_story = translate_text(user_story,target_language='en')
            story.objects.create(story_shown=translated_story)
            return redirect('story')
        
    return render(request, 'LongStoryApp/contribute.html')


