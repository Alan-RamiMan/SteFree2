from django.shortcuts import render
from store.models import Product	
from store.forms import ContactoForms



def Home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }

    return render(request, 'home.html', context)



def contact(request):
    data = {
        'form': ContactoForms()
        # se instacia la clase forms del formulario
    }
    if request.method== 'POST':
        formulario=ContactoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["Mensaje"] = "    Su consulta fue enviada."
        else:
            data["form"]= formulario
    return render(request,'contact.html',data)