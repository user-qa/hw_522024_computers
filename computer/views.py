from django.http import HttpResponse
from django.shortcuts import render
from computer.models import ComputerModel
def ComputerView(request):
    computers_all = ComputerModel.objects.all()
    q = request.GET.get('q')
    if q:
        computers_all = computers_all.filter(model__icontains=q)
    context = {'computer_list': computers_all}

    return render(request=request, template_name="index.html", context=context)

def ComputerDetailView(request, pk):
    computer = ComputerModel.objects.filter(id=pk).first()
    if computer:
        context = {'computer':computer}
        return render(request, template_name='detail.html', context=context)
    else:
        return HttpResponse('Computer Not Found')


def DownloadBookView(request, pk):
    computer = ComputerModel.objects.filter(id=pk).first()
    if computer:
        file_path = computer.computer_picture.path
        print(file_path)
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='image/png')
            response['Content-Disposition'] = f'attachment; filename="{computer.model}.png"'
            return response
    else:
        HttpResponse('Computer Not Found')

