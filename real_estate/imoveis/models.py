from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver


class Anuncio(models.Model):
    TIPOS_DE_ANUNCIO = (('Venda', 'Venda'),
                        ('Aluguel', 'Aluguel'),
                        ('Aluguel e Venda', 'Aluguel e Venda'))

    TIPOS_DE_IMOVEIS = (('Apartamento', 'Apartamento'),
                        ('Casa', 'Casa'),
                        ('Comercial', 'Comercial'),
                        ('Fazenda/Sítio', 'Fazenda/Sítio'),)
    CIDADES = (('Macaé', 'Macaé'), ('Rio das Ostras', 'Rio das Ostras'),
               ('Campos', 'Campos'), ('Búzios', 'Búzios'))

    # Detalhes do usuario
    nome_contato = models.CharField(max_length=50)
    telefone_contato = models.CharField(max_length=50)
    email_contato = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='anuncios_do_usuario')

    # Detalhes do anúncio
    tipo_anuncio = models.CharField(max_length=40, choices=TIPOS_DE_ANUNCIO)
    created = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=300)
    descricao = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    imagem_principal = models.ImageField(upload_to='anuncios/%Y/%m/%d')

    # Detalhes do tipo_imovel
    quartos = models.IntegerField()
    banheiros = models.IntegerField()
    suites = models.IntegerField()
    area_construida = models.DecimalField(max_digits=9, decimal_places=2)
    area_total = models.DecimalField(max_digits=9, decimal_places=2)
    tipo_imovel = models.CharField(max_length=30, choices=TIPOS_DE_IMOVEIS)
    data_construcao = models.DateField()
    preco_venda = models.DecimalField(max_digits=9, decimal_places=2)
    preco_aluguel = models.DecimalField(max_digits=9, decimal_places=2)

    # Localização do imovel
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50,choices=CIDADES)
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    cep = models.CharField(max_length=50)

    # Publicacao do anuncio
    pagamento = models.BooleanField(default=False)
    destaque = models.BooleanField(default=False)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('imoveis:anuncio', args=[self.slug])


class ImagensAnuncio(models.Model):
    anuncio = models.ForeignKey(Anuncio, related_name='imagens')
    imagem = models.ImageField(upload_to='anuncios/%Y/%m/%d')


# Função que utiliza um tipo de sinal do django, post_save, para atualizar o slug depois que o objeto é criado.
# então atualizamos seu slug para utilizar na url

@receiver(post_save, sender=Anuncio)
def criar_slug(sender, instance, created, **kwargs):
    if created:
        string = (instance.cidade + " " +
                  instance.titulo + " " + str(instance.id))
        instance.slug = slugify(string)
        instance.save()

"""
anuncio = Anuncio.objects.get(pk=1)
image_list = anuncio.images.all()

"""
