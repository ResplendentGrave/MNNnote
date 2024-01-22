from django.shortcuts import render, redirect
from .forms import UploadForm

# Create your views here.
def upload(request):
    forms = UploadForm()

    """もしリクエストがPOSTの場合"""
    if request.method == "POST":
        forms = UploadForm(request.POST or None, request.FILES or None)
        #POST内容が正しい時（バリデーションチェック）
        if forms.is_valid():
            #もしユーザーがログインしていたら
            if request.user.is_authenticated:
                forms.instance.create_user = request.user.username
            else:
                print('ログインしていないユーザーです!')
            forms.save()
        return redirect("/home/#note")
    
    forms.fields['lecture_model'].label = "講義名を選択" 

    return render(request,"upload.html", context={
        'forms': forms,
    })