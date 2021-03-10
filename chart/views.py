from django.shortcuts import render
from django.utils import translation
from .utils import get_y
from django.views.decorators.http import require_POST


def index(request):
    # if "lang" in request.GET:
    #     translation.activate(request.GET.get("lang"))

    return render(request, 'base.html')


@require_POST
def results(request):
    gas = None
    temperature = None
    pressur = None
    if request.method == 'POST':
        pressur = int(request.POST.get('pressure'))
        temperature = int(request.POST.get('temperature'))
        gas = get_y(x=pressur, ser='1/8')
        print(pressur, temperature, gas)
    context = {'pressure': pressur, 'temperature': temperature, 'gas': gas}
    return render(request, 'results.html', context=context)
