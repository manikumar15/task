
from django.shortcuts import render

from django.http.response import HttpResponse

from .models import Register,ProductData
from .forms import regform,logform,InsertingDataForm, UpdateDataForm, DeleteDataForm

def index(request):
    if request.method=="POST":
        lform=logform(request.POST)
        if lform.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            data=Register(
                username=username,
                password=password
                )


            uname=Register.objects.filter(username=username)
            pwd=Register.objects.filter(password=password)

            if uname and pwd:
                return render(request,'home.html')
            else:
                return HttpResponse("fail")
        else:
            return HttpResponse("invalid")
    else:
        lform=logform()
        return render(request, 'index.html',{'lform': lform})

def register(request):
    if request.method == "POST":
        fform=regform(request.POST)
        if fform.is_valid():
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
          
            data=Register(
                username=username,
                email=email,
                password=password
                )
            data.save()
            fform=regform()
            fdata = Register.objects.all()
            return render(request,'register.html',{'fform': fform,'fdata': fdata})
        else:
            return HttpResponse('Invalid User Data')
    else:
        fform = regform()
        fdata = Register.objects.all()
    return render(request, 'register.html',{'fform': fform,'fdata': fdata})






def homeView(request):
    return render(request,'home.html')


def createView(request):
    if request.method == 'POST':
        iform = InsertingDataForm(request.POST)
        try:
            if iform.is_valid():
                id = request.POST.get('id')
                name = request.POST.get('name')
                role = request.POST.get('role')

                data = ProductData(
                    id=id,
                    name=name,
                    role=role,
                   
                )
                data.save()

                iform = InsertingDataForm()
                return render(request, 'create.html', {'iform': iform})
        except:
            return HttpResponse("IntegrityError!!! Data is Already Available🛑🤚🛑")

        else:
            return HttpResponse('Invalid Data')

    else:
        iform = InsertingDataForm()
        return render(request,'create.html',{'iform':iform})


def retrieveView(request):
    pdata = ProductData.objects.all()
    return render(request,'retrieve.html',{'pdata':pdata})


def updateView(request):
    if request.method == 'POST':
        uform = UpdateDataForm(request.POST)
        if uform.is_valid():
            id = request.POST.get('id')
            name = request.POST.get('name')
            role = request.POST.get('role')
            id = ProductData.objects.filter(id=id)
            if not id:
                return HttpResponse('Invalid Employee Id')
            else:
                id.update(role= role)
                id.update(name= name)
                uform = UpdateDataForm()
                return render(request,'update.html',{'uform':uform})
        else:
            msg = "🤚🚫 Please Fill The Form  "
            uform = UpdateDataForm()
            return render(request,'update.html',{'uform':uform,'msg':msg})
    else:
        uform = UpdateDataForm()
        return render(request,'update.html',{'uform':uform})


def deleteView(request):
    if request.method == 'POST':
        dform = DeleteDataForm(request.POST)
        if dform.is_valid():
            id = request.POST.get('id')
            id = ProductData.objects.filter(id=id)
            if not id:
                return HttpResponse('Invalid Employee Id')
            else:
                id.delete()
                dform = DeleteDataForm
                return render(request,'delete.html',{'dform':dform})
        else:
            dform = DeleteDataForm()
            msg = "🤚🚫 Please Fill The Form  "
            return render(request,'delete.html',{'msg':msg,'dform':dform})

    else:
        dform = DeleteDataForm()
        return render(request,'delete.html',{'dform':dform})