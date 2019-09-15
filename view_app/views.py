from django.shortcuts import render
from .models import studentDB
from .adduser import init_student

def home(request):
    db = studentDB.scan()
    db = list(db)
    if request.method == 'POST':
        init_student(request)
    # if request.method.get('display_studentid_select') == 'GET':
    #     print('option worked')
    # second = request.GET['display_studentid_select']
    # print(second)

    return render(request, 'view_app/home.html', {'database': db})
    
