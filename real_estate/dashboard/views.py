from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from imoveis.forms import AnuncioForm
from imoveis.models import Anuncio
# Create your views here.


def dashboard_home(request):
	return render(request, 'dashboard/dashboard_home.html')

def dashboard_meus_anuncios(request):
	anuncios = request.user.anuncios_do_usuario.all()
	return render(request, 'dashboard/dashboard_anuncios.html', {'anuncios':anuncios})

def dashboard_meus_dados(request):
	return render(request, 'dashboard/dashboard_meus_dados.html')

def dashboard_deletar_anuncio(request):
    if request.method == "POST":
        print(request.POST['anuncio_id'])
        anuncio_id = request.POST['anuncio_id']
        anuncio = Anuncio.objects.get(id=anuncio_id)
        anuncio.delete()
        messages.success(request, "Estate deleted successfully!")
        return redirect("/dashboard/meus-anuncios")

# agora devo ver como vou passar o pk
def dashboard_editar_anuncio(request, id=None):
    obj = get_object_or_404(Anuncio, id=id)
    form = AnuncioForm(request.POST or None,
                        request.FILES or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/dashboard/home')
    return render(request, 'dashboard/dashboard_editar_anuncio.html', {'form': form})