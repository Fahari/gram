from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    caption = models.TextField(max_length =120)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def search_by_user(cls,search_term):
        users = cls.objects.filter(title__icontains=search_term)
        return users
