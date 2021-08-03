from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class App(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='main_web/static/img/appcenter', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='app'
        verbose_name_plural='apps'

    def __str__(self):
        return self.titulo

class Record(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='main_web/static/img/recordcenter', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='record'
        verbose_name_plural='records'

    def __str__(self):
        return self.titulo

class Datatable(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='main_web/static/img/datacenter', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='datatable'
        verbose_name_plural='datatables'

    def __str__(self):
        return self.titulo