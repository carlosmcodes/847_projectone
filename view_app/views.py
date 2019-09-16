from django.shortcuts import render
from .models import studentDB
from .adduser import init_student, searchuser
from django.middleware import csrf

def home(request):
    db = studentDB.scan()
    db = list(db)
    if request.method == 'POST':
        init_student(request)

    if request.GET.get("display_studentid_select"):
        postsearch = searchuser(value=int(request.GET.get("display_studentid_select")))
        return render(request, 'view_app/index.html', {'postsearch': postsearch })

    elif request.GET.get("display_fname_select"):
        postsearch = searchuser(fname=request.GET.get("display_fname_select"))
        return render(request, 'view_app/index.html', {'postsearch': postsearch })
    
    elif request.GET.get("display_lname_select"):
        postsearch = searchuser(lname=request.GET.get("display_lname_select"))
        return render(request, 'view_app/index.html', {'postsearch': postsearch })
    
    return render(request, 'view_app/index.html', {'database': db})
    
