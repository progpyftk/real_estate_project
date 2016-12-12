from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from imoveis.forms import AnuncioForm, ImagensForm
from imoveis.models import Anuncio, ImagensAnuncio
from account.models import Perfil
from account.forms import PerfilEditForm, UserEditForm
from django.forms import modelformset_factory

# Create your views here.


def dashboard_home(request):
    return render(request, 'dashboard/dashboard_home.html')


def dashboard_meus_anuncios(request):
    anuncios = request.user.anuncios_do_usuario.all()
    return render(request, 'dashboard/dashboard_anuncios.html', {'anuncios': anuncios})


def dashboard_meus_dados(request):
    return render(request, 'dashboard/dashboard_meus_dados.html')


def dashboard_deletar_anuncio(request):
    if request.method == "POST":
        anuncio_id = request.POST['anuncio_id']
        anuncio = Anuncio.objects.get(id=anuncio_id)
        anuncio.delete()
        return redirect("/dashboard/meus-anuncios")

# agora devo ver como vou passar o pk


def dashboard_editar_anuncio(request, id=None):
    obj = get_object_or_404(Anuncio, id=id)
    form = AnuncioForm(request.POST or None,
                       request.FILES or None, instance=obj)

    imagens_do_anuncio = obj.imagens.all()
    # cria formset
    ImageFormSet = modelformset_factory(ImagensAnuncio,
                                        form=ImagensForm, extra=0)
    # popula o formset
    formset = ImageFormSet(request.POST or None,
                           request.FILES or None, queryset=imagens_do_anuncio)
    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('/dashboard/home')
    return render(request, 'dashboard/dashboard_editar_anuncio.html', {'form': form, 'formset': formset})


def dashboard_editar_perfil(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        perfil_form = PerfilEditForm(instance=request.user.perfil,
                                     data=request.POST,
                                     files=request.FILES)
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            return redirect('/dashboard/home')
    else:
        user_form = UserEditForm(instance=request.user)
        perfil_form = PerfilEditForm(instance=request.user.perfil)
    return render(request, 'dashboard/dashboard_editar_perfil.html', {'user_form': user_form, 'perfil_form': perfil_form})
