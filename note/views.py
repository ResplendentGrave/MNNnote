from django.shortcuts import render
from lecture.models import LectureMpdel
from upload.models import UploadModel
# Create your views here.
def note(request):
    if request.method == "POST":
        print('POSTリクエスト！！')
        print('講義名＞＞', request.POST['buttonText'])
        models = LectureMpdel.objects.filter(name=request.POST["buttonText"])
        note_models = UploadModel.objects.filter(lecture_model=models.first())
        return render(request, "note.html", 
                      context={'models':models,
                               'note_models':note_models})
    return render(request,"note.html")