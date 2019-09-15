from .models import studentDB

new_student = studentDB()

def init_student(request):
    studentid = request.POST.get('studentid')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    address = request.POST.get('address')
    email = request.POST.get('email')
    gpa = request.POST.get('gpa')
    addto_Dynamo(studentid, fname, lname, address,email, gpa)

def addto_Dynamo(studentid, fname, lname, address, email, gpa):
    new_student.studentid = int(studentid)
    new_student.fname = fname
    new_student.lname = lname
    new_student.address = address
    new_student.email = email
    new_student.gpa = float(gpa)
    new_student.save()




