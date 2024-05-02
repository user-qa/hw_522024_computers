from django.shortcuts import render
from computer.models import ComputerModel
def ComputerView(request):
    computers_all = ComputerModel.objects.all()
    context = {'computer_list': computers_all}

    return render(request=request, template_name="index.html", context=context)