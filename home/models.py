from django.db import models
from ckeditor.fields import RichTextField


class Maintitle(models.Model):
    title = models.CharField(max_length=100, verbose_name='Solüstbüyükbaşlık')
    title2 = models.CharField(max_length=100, verbose_name='Solüstküçükbaşlık')
    title3 = models.CharField(max_length=100, verbose_name='Anasayfabaşlık')
    def __str__(self):
        return self.title


class Home1(models.Model):
    title = models.CharField(max_length=100, verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    text = RichTextField(verbose_name='Uzun İçerik', null=True)

    def __str__(self):
        return self.title


class Home2(models.Model):
    title = models.CharField(max_length=100, verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    text = RichTextField(verbose_name='Uzun İçerik', null=True)

    def __str__(self):
        return self.title   

        
class Home3(models.Model):
    title = models.CharField(max_length=100, verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    text = RichTextField(verbose_name='Uzun İçerik', null=True)

    def __str__(self):
        return self.title


class Home4(models.Model):
    title = models.CharField(max_length=100, verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    text = RichTextField(verbose_name='Uzun İçerik', null=True)

    def __str__(self):
        return self.title 


class Instagram(models.Model):
    content = models.TextField(verbose_name='İçerik', null=True)

    def __str__(self):
        return self.content  


class Iletisim(models.Model):
    title = models.CharField(max_length=100, verbose_name='Başlık')
    text = RichTextField(verbose_name='Uzun İçerik', null=True) 

    def __str__(self):
        return self.title       


class Foto(models.Model):
    title = models.CharField(max_length=100, verbose_name='FotoBaşlık')
    image = models.ImageField(upload_to='fotolar/', null=True)  

    def __str__(self):
        return self.title  


class Bülten(models.Model):
    title = models.CharField(max_length=100, verbose_name='Bülten Başlık')
    text = RichTextField(verbose_name='Uzun İçerik', null=True)
    üstimage = models.ImageField(upload_to='fotolar/', null=True, blank=True)
    image = models.ImageField(upload_to='fotolar/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']   


class Message(models.Model):
    name = models.CharField(max_length=30, verbose_name='İsim ve Soyisim')
    email = models.CharField(max_length=50, verbose_name='email')
    text = models.TextField(verbose_name='mesaj')

    def __str__(self):
        return self.name


            

            
